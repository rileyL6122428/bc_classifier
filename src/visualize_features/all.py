from load_data.breast_cancer_raw import formatted_col_names as feature_names, malignant, benign
from visualize_utils.draw_dispersion import draw_dispersion

for feature_name in feature_names:
    if feature_name in { 'worst_concave_points', 'mean_concave_points' }:
        draw_dispersion(
            affirmative_series=benign[feature_name],
            affirmative_label='Benign',
            negative_series=malignant[feature_name],
            negative_label='Malignant',
            title=feature_name.upper()
        )
