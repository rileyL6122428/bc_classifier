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

# malignant -> 0, benign -> 1
y = pd.DataFrame(
    data=raw_data_set.target,
    columns=['label']
)

breast_cancer_df = pd.concat([X, y], axis=1)

malignant_indices = breast_cancer_df.index[breast_cancer_df.label == 0].tolist()
malignant = breast_cancer_df[breast_cancer_df.label == 0]

benign_indices = breast_cancer_df.index[breast_cancer_df.label == 1].tolist()
benign = breast_cancer_df[breast_cancer_df.label == 1]

