# Import scale
from sklearn.preprocessing import scale

# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(X.mean()))
print("Standard Deviation of Unscaled Features: {}".format(X.std()))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(X_scaled.mean()))
print("Standard Deviation of Scaled Features: {}".format(X_scaled.std()))
