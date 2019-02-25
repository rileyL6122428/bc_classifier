from load_data.breast_cancer_raw import X, y, breast_cancer_df, malignant, benign
from visualize_utils.draw_dispersion import draw_dispersion

draw_dispersion(
    affirmative_series=benign.mean_texture,
    affirmative_label='Benign',
    negative_series=malignant.mean_texture,
    negative_label='Malignant'
)
