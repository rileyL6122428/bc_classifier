from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, precision_score, recall_score
from models.test_train_split import X_test, X_train, y_test, y_train

pipeline = Pipeline([
    ('standar_scaler', StandardScaler()),
    ('logistic_regressor', LogisticRegression())
])

param_grid = {
    'logistic_regressor__C': [ 1, 3, 5, 7, 9, 10 ],
    'logistic_regressor__random_state': [ 42 ],
    'logistic_regressor__dual': [ False ],
    'logistic_regressor__max_iter': [ 100, 500, 1000 ],
}

classifier = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring='f1',
    cv=5
)

classifier.fit(X_train, y_train)

test_predictions = classifier.predict(X_test)

print('classifier.best_params_', classifier.best_params_)
    # {'logistic_regressor__C': 1, 'logistic_regressor__dual': False, 'logistic_regressor__max_iter': 100, 'logistic_regressor__random_state': 42}
print('classifier.best_score_', classifier.best_score_)
    # 0.9587195514016732
print(
    'f1 score on train set',
    f1_score(
        y_true=y_test,
        y_pred=test_predictions
    )
)
print(
    'precision score on train set',
    precision_score(
        y_true=y_test,
        y_pred=test_predictions
    )
)
print(
    'recall score on train set',
    recall_score(
        y_true=y_test,
        y_pred=test_predictions
    )
)

