from matplotlib import pyplot as plt
import numpy as np

def draw_dispersion(affirmative_series, negative_series, affirmative_label='', negative_label='', title=''):
    negative_color = '#007acc'
    affirmative_color = '#ff8000'
    text_alignment = 'center'

    plt.scatter(
        x=negative_series,
        y=np.zeros(negative_series.size),
        marker='d'
    )

    plt.text(
        negative_series.mean() - negative_series.std(),
        0.1,
        '-σ',
        color=negative_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        negative_series.mean(),
        0.1,
        'µ',
        color=negative_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        negative_series.mean() + negative_series.std(),
        0.1,
        '+σ',
        color=negative_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        negative_series.quantile(.15),
        0.2,
        '.15',
        color=negative_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        negative_series.quantile(.5),
        0.2,
        '.5',
        color=negative_color,
        horizontalalignment=text_alignment
    )

    plt.text(
        negative_series.quantile(.85),
        0.2,
        '.85',
        color=negative_color,
        horizontalalignment=text_alignment
    )

    plt.scatter(
        x=affirmative_series,
        y=np.ones(affirmative_series.size),
        marker='d'
    )

    plt.text(
        affirmative_series.mean() - affirmative_series.std(),
        0.8,
        '-σ',
        color=affirmative_color,
        horizontalalignment='center'
    )

    plt.text(
        affirmative_series.mean(),
        0.8,
        'µ',
        color=affirmative_color,
        horizontalalignment='center'
    )

    plt.text(
        affirmative_series.mean() + affirmative_series.std(),
        0.8,
        '+σ',
        color=affirmative_color,
        horizontalalignment='center'
    )

    plt.text(
        affirmative_series.quantile(.15),
        0.7,
        '.15',
        color=affirmative_color,
        horizontalalignment='center'
    )

    plt.text(
        affirmative_series.median(),
        0.7,
        '.5',
        color=affirmative_color,
        horizontalalignment='center'
    )

    plt.text(
        affirmative_series.quantile(.85),
        0.7,
        '.85',
        color=affirmative_color,
        horizontalalignment='center'
    )


    plt.legend((negative_label, affirmative_label))
    plt.title(title)
    plt.show()

# print(X[:5])
