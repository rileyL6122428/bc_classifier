from sklearn.preprocessing import RobustScaler, StandardScaler
from load_data.breast_cancer_raw import malignant, benign
from visualize_utils.draw_dispersion_by_class import draw_dispersion_by_class

selected_features = {
    'worst_radius',
    'worst_perimeter',
    'worst_area',
    'worst_concave_points'
}

# scaler = RobustScaler()
scaler = StandardScaler()

malignant_scaled = malignant.copy()
malignant_scaled[malignant_scaled.columns] = scaler.fit_transform(
    malignant[malignant_scaled.columns]
)

benign_scaled = benign.copy()
benign_scaled[benign_scaled.columns] = scaler.fit_transform(
    benign_scaled[benign_scaled.columns]
)

for feature_name in selected_features:
    if feature_name in selected_features:
        draw_dispersion_by_class(
            affirmative_series=benign_scaled[feature_name],
            negative_series=malignant_scaled[feature_name],
            affirmative_label='benign',
            negative_label='malignant',
            title=feature_name + ' SCALED'
        )

