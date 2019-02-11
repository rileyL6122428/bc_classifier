from load_data.breast_cancer_raw import X, y, breast_cancer_df, malignant, benign
from matplotlib import pyplot as plt
import numpy as np
from pandas import Series

mean_radii = X.mean_radius

print('\n', 'MEAN RADIUS STATS', '\n')

print('MIN MEAN RADIUS =', mean_radii.min())
print('(MEAN - 1 STD DEV) MEAN RADIUS =', mean_radii.mean() - mean_radii.std())
print('MEAN MEAN RADIUS =', mean_radii.mean())
print('(MEAN + 1 STD DEV) MEAN RADIUS =', mean_radii.mean() + mean_radii.std())
print('MAX MEAN RADIUS =', mean_radii.max(), '\n')

print('MIN MEAN RADIUS =', mean_radii.min())
print('15% QUANTILE MEAN RADIUS =', mean_radii.quantile(.15))
print('MEDIAN MEAN RADIUS =', mean_radii.median())
print('85% QUANTILE MEAN RADIUS =', mean_radii.quantile(.85))
print('MAX MEAN RADIUS =', mean_radii.max())

plt.scatter(
    x=malignant.mean_radius,
    y=np.zeros(malignant.mean_radius.size),
    marker='d'
)

plt.scatter(
    x=benign.mean_radius,
    y=np.ones(benign.mean_radius.size),
    marker='d'
)

plt.text(
    benign.mean_radius.mean(),
    0.8,
    'µ',
    color='#FFAA00'
)

plt.text(
    benign.mean_radius.median(),
    0.7,
    '˜µ',
    color='#FFAA00'
)



plt.legend(('malignant', 'benign'))
plt.title('MEAN RADIUS')
plt.show()

# print(X[:5])
