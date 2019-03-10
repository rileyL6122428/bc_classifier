from models.test_train_split import X_test, X_train, y_test, y_train
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

classifier_pipeline = Pipeline([
    ('standard_scaler', StandardScaler()),
    ('svm', LinearSVC())
])

params_grid = {
    'svm__dual': [True, False],
    'svm__random_state': [42],
    'svm__C': [1, 2, 3, 4, 5, 6]
}

classifier = GridSearchCV(
    classifier_pipeline,
    param_grid=params_grid,
    cv=5,
    scoring='f1'
)

classifier.fit(X_train, y_train)


print('BEST PARAMS', classifier.best_params_) # {'svm__C': 4, 'svm__dual': True, 'svm__random_state': 42}
print('BEST ESTIMATOR F1 SCORE', classifier.best_score_) # 0.9624233268956405

y_predictions = classifier.predict(X_test)
print(
    'F1 ON TEST SET',
    f1_score(
        y_true=y_test,
        y_pred=y_predictions
    )
) # 0.9818181818181818
