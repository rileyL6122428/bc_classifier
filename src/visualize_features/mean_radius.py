from load_data.breast_cancer_raw import X, y, breast_cancer_df, malignant, benign
from visualize_utils.draw_dispersion import draw_dispersion

# mean_radii = X.mean_radius

# print('\n', 'MEAN RADIUS STATS', '\n')

# print('MIN MEAN RADIUS =', mean_radii.min())
# print('(MEAN - 1 STD DEV) MEAN RADIUS =', mean_radii.mean() - mean_radii.std())
# print('MEAN MEAN RADIUS =', mean_radii.mean())
# print('(MEAN + 1 STD DEV) MEAN RADIUS =', mean_radii.mean() + mean_radii.std())
# print('MAX MEAN RADIUS =', mean_radii.max(), '\n')

# print('MIN MEAN RADIUS =', mean_radii.min())
# print('15% QUANTILE MEAN RADIUS =', mean_radii.quantile(.15))
# print('MEDIAN MEAN RADIUS =', mean_radii.median())
# print('85% QUANTILE MEAN RADIUS =', mean_radii.quantile(.85))
# print('MAX MEAN RADIUS =', mean_radii.max())

draw_dispersion(
    affirmative_series=benign.mean_radius,
    affirmative_label='Benign',
    negative_series=malignant.mean_radius,
    negative_label='Malignant'
)
