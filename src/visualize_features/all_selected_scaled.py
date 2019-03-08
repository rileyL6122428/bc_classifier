from sklearn.preprocessing import RobustScaler, StandardScaler
from load_data.breast_cancer_raw import malignant_indices, benign_indices, breast_cancer_df
from visualize_utils.draw_class_dispersion import draw_dispersion_by_class
from visualize_features.selected_features import selected_features
import pandas as pd

scaler = StandardScaler()

for feature_name in selected_features:
    if feature_name in selected_features:
        feature = breast_cancer_df[[feature_name]]
        scaled_feature = pd.Series(scaler.fit_transform(feature).flatten())
        scaled_feature_benign = scaled_feature.iloc[benign_indices]
        scaled_feature_malignant = scaled_feature.iloc[malignant_indices]

        draw_dispersion_by_class(
            series=scaled_feature,
            affirmative_series=scaled_feature_benign,
            negative_series=scaled_feature_malignant,
            affirmative_label='benign',
            negative_label='malignant',
            title=feature_name
        )

