from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, precision_score, recall_score
from models.test_train_split import X_test, X_train, y_test, y_train

pipeline = Pipeline([
    ('standard_scaler', StandardScaler()),
    ('k_neighbors_classifier', KNeighborsClassifier())
])

param_grid = {
    'k_neighbors_classifier__n_neighbors': [ 3, 5, 7 ],
    'k_neighbors_classifier__weights': [ 'uniform', 'distance' ],
    'k_neighbors_classifier__algorithm': [ 'ball_tree', 'kd_tree', 'brute' ],
}

classifier = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring='f1',
    cv=5
)

classifier.fit(X_train, y_train)

y_predictions = classifier.predict(X_test)

print('classifier.best_params_', classifier.best_params_)
    #  {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'}
print('classifier.best_score_', classifier.best_score_)
    #  0.9624757831604963
print(
    'test f1_score',
    f1_score(
        y_true=y_test,
        y_pred=y_predictions
    )
)  # 0.954954954954955

print(
    'test precision_score',
    precision_score(
        y_true=y_test,
        y_pred=y_predictions
    )
)  # 0.9298245614035088

print(
    'test recall_score',
    recall_score(
        y_true=y_test,
        y_pred=y_predictions
    )
)  # 0.9814814814814815
