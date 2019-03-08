from load_data.breast_cancer_raw import formatted_col_names as feature_names, malignant, benign, breast_cancer_df
from visualize_utils.draw_class_dispersion import draw_dispersion_by_class
from visualize_features.selected_features import selected_features

for feature_name in feature_names:
    if feature_name in selected_features:
        draw_dispersion_by_class(
            series=breast_cancer_df[feature_name],
            affirmative_series=benign[feature_name],
            affirmative_label='Benign',
            negative_series=malignant[feature_name],
            negative_label='Malignant',
            title=feature_name.upper()
        )
