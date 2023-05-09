import pandas as pd
import numpy as np
import warnings

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

import plotly.graph_objects as go


from scipy.stats import zscore

font = {'size'   :      14}

matplotlib.rc('font', **font)

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 100

sns.set(rc={"figure.dpi":100, 'savefig.dpi':300})
sns.set_theme(style='whitegrid')

random_seed = 31415926

np.random.seed(random_seed)

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


def create_plots(comps_or, comps_sy, labels_or, labels_sy, output=None):
    nrows = 2
    ncols = 2
    if output is None:
        nrows = 1
    fig = plt.figure(figsize=(10, 10))
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)

    with sns.axes_style("whitegrid"):
        ax = fig.add_subplot(nrows, ncols, 1)
        sns.scatterplot(x=comps_or[:, 0],
                        y=comps_or[:, 1],
                        ax=ax,
                        hue=labels_or,
                        palette="Set2",
                        s=50)
        ax.set_title("Real Data", fontsize=20)
        ax.set(xticks=[], yticks=[])

        ax = fig.add_subplot(nrows, ncols, 2)
        sns.scatterplot(x=comps_sy[:, 0],
                        y=comps_sy[:, 1],
                        ax=ax,
                        hue=labels_sy,
                        palette="Set2",
                        s=50)
        ax.set_title("synthetic Data", fontsize=20)
        ax.set(xticks=[], yticks=[])

        if output is not None:
            ax = fig.add_subplot(nrows, ncols, 3)
            sns.scatterplot(x=comps_or[:, 0],
                            y=comps_or[:, 1],
                            ax=ax,
                            hue=output,
                            palette="Set1",
                            s=50)
            ax.set_title("Real Data", fontsize=20)
            ax.set(xticks=[], yticks=[])

            ax = fig.add_subplot(nrows, ncols, 4)
            sns.scatterplot(x=comps_sy[:, 0],
                            y=comps_sy[:, 1],
                            ax=ax,
                            hue=output,
                            palette="Set1",
                            s=50)

            ax.set_title("synthetic Data", fontsize=20)
            ax.set(xticks=[], yticks=[])

    plt.subplots_adjust(wspace=0.10)
    plt.subplots_adjust(hspace=0.20)

    return fig

def plot_dfs_2d(comps_or, comps_sy):
    layout = go.Layout(width=600, height=600, template="simple_white")

    fig = go.Figure(layout=layout)
    fig.add_scatter(x=comps_or[:, 0], y=comps_or[:, 1], mode="markers", name="Real")
    fig.add_scatter(x=comps_sy[:, 0], y=comps_sy[:, 1], mode="markers", name="synthetic")

    return fig