from load_data.breast_cancer_raw import benign, malignant
from visualize_utils.draw_dispersion import draw_dispersion

draw_dispersion(
    affirmative_series=benign.mean_perimeter,
    affirmative_label='benign',
    negative_series=malignant.mean_perimeter,
    negative_label='malignant',
    title='MEAN PERIMETER'
)
