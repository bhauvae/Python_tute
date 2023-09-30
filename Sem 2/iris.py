import numpy as np
import pandas
from sklearn.datasets import load_iris
from tabulate import tabulate
from statistics import mode, median, correlation, covariance, stdev

iris_obj = load_iris()
iris = pandas.DataFrame(iris_obj.data, columns=iris_obj.feature_names)

# Displaying up the top rows of the dataset with their columns
# print(iris.iloc[0:10])

# Displaying names of the columns.
print(iris.columns)

# Displaying the shape of the dataset.
# print(iris.shape)

# Displaying only specific columns.
# print(iris['sepal length (cm)'])

# Slicing the rows - show rows 10to 20
# print(iris.iloc[10:21])

# Compute mean, mode, median, standard deviation of all features
print("Mean")
mean = [['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
        [np.mean(np.array(iris['sepal width (cm)'])), np.mean(np.array(iris['sepal length (cm)'])),
         np.mean(np.array(iris['petal length (cm)'])), np.mean(np.array(iris['petal width (cm)']))]]
print(tabulate(mean))

print("Mode")
mode = [['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
        [mode(np.array(iris['sepal width (cm)'])), mode(np.array(iris['sepal length (cm)'])),
         mode(np.array(iris['petal length (cm)'])), mode(np.array(iris['petal width (cm)']))]]
print(tabulate(mode))

print("Median")
median = [['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
          [median(np.array(iris['sepal width (cm)'])), median(np.array(iris['sepal length (cm)'])),
           median(np.array(iris['petal length (cm)'])), median(np.array(iris['petal width (cm)']))]]
print(tabulate(median))

print("Standard Deviation")
std_div = [['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
           [stdev(np.array(iris['sepal width (cm)'])), stdev(np.array(iris['sepal length (cm)'])),
            stdev(np.array(iris['petal length (cm)'])), stdev(np.array(iris['petal width (cm)']))]]
print(tabulate(std_div))

# Find covariance between length of sepal and petal
covariance = covariance(np.array(iris['sepal length (cm)']), np.array(iris['petal length (cm)']))
print("covariance between length of sepal and petal ", covariance)

# Compute correlation coefficients between each pair of features and plot heatmap
s_wid = np.array(iris['sepal width (cm)'])
s_len = np.array(iris['sepal length (cm)'])
p_wid = np.array(iris['petal width (cm)'])
p_len = np.array(iris['petal length (cm)'])
correlation = [[correlation(s_wid, s_wid), correlation(s_wid, s_len), correlation(s_wid, p_wid),
                correlation(s_wid, p_len)],
               [correlation(s_len, s_wid), correlation(s_len, s_len), correlation(s_len, p_wid),
                correlation(s_len, p_len)],
               [correlation(p_wid, s_wid), correlation(p_wid, s_len), correlation(p_wid, p_wid),
                correlation(p_wid, p_len)],
               [correlation(p_len, s_wid), correlation(p_len, s_len), correlation(p_len, p_wid),
                correlation(p_len, p_len)]]
print(tabulate(correlation))

iris['new column'] = np.random.rand(150)
print(iris)

print((iris.mean(axis=0)))
