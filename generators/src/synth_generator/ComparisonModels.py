from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, GridSearchCV
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from numpy import mean
import matplotlib.pyplot as plt
from sdv.tabular import CTGAN
from sdv.tabular import CopulaGAN
from sdv.tabular import GaussianCopula
from sdv.tabular import TVAE
from sdv.evaluation import evaluate
import pandas as pd
import warnings
import operator

class ComparisonModels:
    def __init__(self, original_data, algorithm, par):
        self.original_data = original_data
        self.algorithm = algorithm
        self.par = par

    def Arrange_parameters(self):
        col = list(self.original_data.columns)
        arg_dic = dict()
        for i in col:
            arg_dic[i] = self.par
        return arg_dic

    def GenerateSynth(self, param):
        if self.algorithm == GaussianCopula():
            model = GaussianCopula(field_distributions=param)
        elif self.algorithm == CopulaGAN():
            model = CopulaGAN(field_distributions=param)
        else:
            model = self.algorithm
        model.fit(self.original_data)
        new_data = model.sample(num_rows=len(self.original_data.index))
        score = evaluate(new_data, self.original_data)
        return new_data, score

    def InvestigateModels(self):
        algo = [CTGAN(), CopulaGAN(), GaussianCopula(), TVAE()]
        arguments = ['gaussian', 'gamma', 'beta', 'student_t', 'gaussian_kde', 'truncated_gaussian']
        col = list(self.original_data.columns)
        param = []
        for i in arguments:
            temp_dic = dict()
            for j in col:
                temp_dic[j] = i
            param.append(temp_dic)
        results = dict()
        synth_collection = dict()
        for x in algo:
            if x == CTGAN():
                model = x
                model.fit(self.original_data)
                new_data = model.sample(num_rows=len(self.original_data.index))
                synth_collection[x] = new_data
                score = evaluate(new_data, self.original_data)
                warnings.filterwarnings('ignore')
                results[x] = score

            elif x == TVAE():
                model = x
                model.fit(self.original_data)
                new_data = model.sample(num_rows=len(self.original_data.index))
                synth_collection[str(x)] = new_data
                score = evaluate(new_data, self.original_data)
                warnings.filterwarnings('ignore')
                results[str(x)] = score

            else:
                for i in param:
                    if x == GaussianCopula():
                        model = GaussianCopula(field_distributions=i)
                    else:
                        model = CopulaGAN(field_distributions=i)
                    model.fit(self.original_data)
                    new_data = model.sample(num_rows=len(self.original_data.index))
                    score = evaluate(new_data, self.original_data)
                    warnings.filterwarnings('ignore')
                    argument_name = str(list(i.values())[0])
                    arg_model = str(x) + '_' + argument_name
                    results[arg_model] = score
                    synth_collection[arg_model] = new_data

        best_model = max(results.items(), key=operator.itemgetter(1))[0]
        synth_best_model = synth_collection[best_model]
        return results, synth_best_model


    def plot_model_comparison(self, results):
        plt.xlabel("Evaluation Score")
        plt.ylabel("Generating models")
        plt.title('Comparison Between Synthetic Generation Models')
        plt.barh(range(len(results)), list(results.values()), align='center')
        plt.yticks(range(len(results)), list(results.keys()))
        plt.tight_layout()
        plt.show()

    def RF_classifier(self, X, Y):
        cv_outer = KFold(n_splits=10, shuffle=True, random_state=1)
        test_acc = []
        val_acc = []
        outer_results = list()

        for train_ix, test_ix in cv_outer.split(X):
            x_train, x_test = X[train_ix, :], X[test_ix, :]
            y_train, y_test = Y[train_ix], Y[test_ix]
            cv_inner = KFold(n_splits=3, shuffle=True, random_state=1)
            model = RandomForestClassifier(random_state=1)
            space = dict()
            space['criterion'] = ['gini', 'entropy']
            space['max_features'] = ['auto', 'sqrt', 'log2']
            search = GridSearchCV(model, space, scoring='accuracy', cv=cv_inner, refit=True)
            result = search.fit(x_train, y_train)
            best_model = result.best_estimator_
            yhat = best_model.predict(x_test)
            acc = accuracy_score(y_test, yhat)
            outer_results.append(acc)
            test_acc.append(acc)
            val_acc.append(result.best_score_)
        return test_acc, val_acc

    def plot_classifier(self, org_avg_test, org_avg_val, synth_avg_test, synth_avg_val):
        plt.xlabel("10 Folds")
        plt.ylabel("Accuracy")
        plt.title('Random Forest Cross-fold Validation')
        plt.plot(list(range(1, 11)), org_avg_test, label='Train org')
        plt.plot(list(range(1, 11)), org_avg_val, label='Test org')
        plt.plot(list(range(1, 11)), synth_avg_test, label='Train synth')
        plt.plot(list(range(1, 11)), synth_avg_val, label='Test synth')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    data = pd.read_csv('breast_cancer.csv', sep=',')
    data = data.dropna(how='all', axis=1)
    data = data.drop(['id'], axis=1)
    label_encoder = preprocessing.LabelEncoder()
    data['diagnosis'] = label_encoder.fit_transform(data['diagnosis'])
    algo = CTGAN()
    par = 'beta'
    # algo = ['CTGAN', 'CopulaGAN', 'GaussianCopula', 'TVAE']
    # par = ['gaussian', 'gamma', 'beta', 'student_t', 'gaussian_kde', 'truncated_gaussian']

    cm = ComparisonModels(data, algo, par)
    parameters = cm.Arrange_parameters()
    new_data, score = cm.GenerateSynth(parameters)
    print("Evaluation Score:", score)
    print(new_data.head())

    # res, best_data = cm.InvestigateModels()
    # cm.plot_model_comparison(res)
    #
    # y = data['diagnosis'].to_numpy()
    # data = data.drop(['diagnosis'], axis=1)
    # x = data.to_numpy()
    # y_new = new_data['diagnosis'].to_numpy()
    # new_data = new_data.drop(['diagnosis'], axis=1)
    # x_new = new_data.to_numpy()
    # org_train, org_test = cm.RF_classifier(x, y)
    # syn_train, syn_test = cm.RF_classifier(x_new, y_new)
    # cm.plot_classifier(org_train, org_test, syn_train, syn_test)



