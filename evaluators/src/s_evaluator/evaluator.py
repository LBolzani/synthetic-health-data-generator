from s_evaluator.preprocessing import *
from s_evaluator.rf_visual_evaluator import *
from s_evaluator.ploting import *

from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans

class Evaluator:

    def __init__(self, df_or, df_sy, output):
        self.df_or = df_or
        self.df_sy = df_sy
        self.output = output
        self.random_seed = 31415926

    def preprocess(self):
        le, df_enc_or, df_enc_sy = get_encoded_df(
            self.df_or, self.df_sy)

        self.label_encoder = le
        self.df_encoded_or = df_enc_or
        self.df_encoded_sy = df_enc_sy

        pca = PCA(n_components=2)
        self.pca_comps_or = pca.fit_transform(df_enc_or)

        pca = PCA(n_components=2)
        self.pca_comps_sy = pca.fit_transform(df_enc_sy)

        svd = TruncatedSVD(n_components=2)
        self.svd_comps_or = svd.fit_transform(df_enc_or)

        svd = TruncatedSVD(n_components=2)
        self.svd_comps_sy = svd.fit_transform(df_enc_or)

    def do_clustering(self):
        kmean = KMeans(n_clusters=5, n_init=100,
                       max_iter=1000,
                       random_state=self.random_seed)
        kmean.fit(self.df_encoded_or)
        self.df_or["cluster"] = ["C" + str(i) for i in (kmean.labels_ + 1)]
        self.k_clusters_or = kmean.labels_ + 1

        kmean = KMeans(n_clusters=5, n_init=100,
                       max_iter=1000,
                       random_state=self.random_seed)
        kmean.fit(self.df_encoded_sy)
        self.df_sy["cluster"] = \
            ["C" + str(i) for i in (kmean.labels_ + 1)]
        self.k_clusters_sy = kmean.labels_ + 1

    def plot_pca(self):
        return create_plots(self.pca_comps_or,
                            self.pca_comps_sy,
                            self.k_clusters_or,
                            self.k_clusters_sy,
                            self.output)

    def plot_svd(self):
        return create_plots(
            self.svd_comps_or,
            self.svd_comps_sy,
            self.k_clusters_or,
            self.k_clusters_sy,
            self.output)

    def plot_random_forest(self):
        return plot_random_forest(
            self.df_encoded_or,
            self.df_encoded_sy,
            self.k_clusters_or,
            self.k_clusters_sy,
            self.output
        )

    def plot_correlation(self):
        corr = self.df_encoded_or.corrwith(self.df_encoded_sy).abs()
        return corr.plot.bar()

    def plot_data_2dims(self):
        return plot_dfs_2d(self.pca_comps_or, self.pca_comps_sy)
