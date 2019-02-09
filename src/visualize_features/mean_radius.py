from load_data.breast_cancer_raw import X, y

mean_radii = X.mean_radius

print('\n', 'MEAN RADIUS STATS', '\n')

print('MEAN MEAN RADIUS =', mean_radii.mean())
print('MIN MEAN RADIUS =', mean_radii.min())
print('MAX MEAN RADIUS =', mean_radii.max())

# print(X[:5])
