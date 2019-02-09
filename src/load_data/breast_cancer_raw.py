from sklearn.datasets import load_breast_cancer
import pandas as pd

raw_data_set = load_breast_cancer()

formatted_col_names = [
    name.replace(' ', '_')
    for name
    in raw_data_set.feature_names
]

X = pd.DataFrame(
    data=raw_data_set.data,
    columns=formatted_col_names
)

y = raw_data_set.target  # malignant -> 0, benign -> 1
