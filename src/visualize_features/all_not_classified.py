from load_data.breast_cancer_raw import formatted_col_names as feature_names, X as breast_cancer_features
from visualize_utils.draw_dispersino_unclassified import draw_dispersion

for feature_name in feature_names:
    if feature_name in {'worst_radius', 'worst_perimeter', 'worst_area', 'worst_concave_points'}:
        draw_dispersion(
            feature_series=breast_cancer_features[feature_name],
            feature_name=feature_name
        )
