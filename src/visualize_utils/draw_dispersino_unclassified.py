from matplotlib import pyplot as plt
import numpy as np


def draw_dispersion(feature_series, feature_name=''):
    feature_color = '#33cc33'
    text_alignment = 'center'
    mean_std_label_height = 0.01
    quantile_label_height = 0.005

    plt.scatter(
        x=feature_series,
        y=np.zeros(feature_series.size),
        marker='d',
        alpha=0.1,
        color=feature_color
    )

    plt.text(
        feature_series.mean() - feature_series.std(),
        mean_std_label_height,
        '-σ',
        color=feature_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        feature_series.mean(),
        mean_std_label_height,
        'µ',
        color=feature_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        feature_series.mean() + feature_series.std(),
        mean_std_label_height,
        '+σ',
        color=feature_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        feature_series.quantile(.15),
        quantile_label_height,
        '.15',
        color=feature_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        feature_series.median(),
        quantile_label_height,
        '.5',
        color=feature_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        feature_series.quantile(.85),
        quantile_label_height,
        '.85',
        color=feature_color,
        horizontalalignment=text_alignment
    )

    plt.legend((feature_name))
    plt.title(feature_name)
    plt.show()
