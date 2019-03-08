from sklearn.model_selection import train_test_split
from visualize_features.selected_features import selected_features
from load_data.breast_cancer_raw import breast_cancer_df

X, y = breast_cancer_df[list(selected_features)], breast_cancer_df[['label']]
y.columns = ['benign']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.15,
    random_state=42
)
