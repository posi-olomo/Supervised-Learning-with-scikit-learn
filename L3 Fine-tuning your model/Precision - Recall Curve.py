"""
A recall of 1 corresponds to a classifier with a low threshold in which all females
who contract diabetes were correctly classified as such, at the expense of many
misclassifications of those who did not have diabetes.

Precision is undefined for a classifier which makes no positive predictions, that is, classifies
everyone as not having diabetes.

When the threshold is very close to 1, precision is also 1, because the classifier is absolutely
certain about its predictions.

The above are all true.
"""