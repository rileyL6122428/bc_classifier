from load_data.breast_cancer_raw import malignant, benign
from visualize_utils.draw_dispersion import draw_dispersion

draw_dispersion(
    affirmative_series=benign.mean_area,
    affirmative_label='Benign',
    negative_series=malignant.mean_area,
    negative_label='Malignant',
    title='MEAN AREA'
)

import pdb; pdb.set_trace()
