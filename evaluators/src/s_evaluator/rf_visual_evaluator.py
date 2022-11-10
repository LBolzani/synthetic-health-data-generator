import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

def plot_random_forest_single_df(df, labeles, ax):
    rf = RandomForestClassifier()
    rf.fit(df, y=labeles)

    support_features = pd.Series(rf.feature_importances_, index=df.columns)
    support_features = support_features.sort_values(ascending=False)

    support_features_top = support_features.head(20)

    sns.barplot(x = support_features_top.values,
                y = support_features_top.index,
                ax = ax)


def plot_random_forest(df_or, df_sy, label_or, label_sy, output):
    nrows = 2
    ncols = 2
    if output is None:
        nrows = 1
    fig = plt.figure(figsize=(16, 16))
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)

    ax = fig.add_subplot(nrows, ncols, 1)
    plot_random_forest_single_df(df_or, label_or, ax)
    ax.set_title("Real Data with Clusters", fontsize=20)

    ax = fig.add_subplot(nrows, ncols, 2)
    plot_random_forest_single_df(df_sy, label_sy, ax)
    ax.set_title("Synthatic Data with Clusters", fontsize=20)

    if output is not None:
        ax = fig.add_subplot(nrows, ncols, 3)
        plot_random_forest_single_df(df_or, output, ax)
        ax.set_title("Real Data with Output", fontsize=20)

        ax = fig.add_subplot(nrows, ncols, 4)
        plot_random_forest_single_df(df_sy, output, ax)
        ax.set_title("Synthatic Data with Clusters", fontsize=20)

    plt.subplots_adjust(wspace=1.0)
    plt.subplots_adjust(hspace=0.20)
    plt.tight_layout()
    return fig
