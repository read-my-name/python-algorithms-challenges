import numpy as np
from pylab import plt,mpl
import seaborn as sns

# Apply seaborn style
sns.set()

mpl.rcParams['font.family'] = 'serif'

def f(x):
    return np.sin(x) + 0.5 * x

def create_plot(x, y, styles, labels, axlabels):
    plt.figure(figsize=(10, 6))
    for i in range(len(x)):
        plt.plot(x[i], y[i], styles[i], label=labels[i])
        plt.xlabel(axlabels[0])
        plt.ylabel(axlabels[1])
    
    plt.legend(loc=0)
    plt.show()

# Create a plot with a single curve
x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

# # create_plot([x], [f(x)], ['b'], ['f(x)'], ['x', 'f(x)'])

# # Create a plot with linear regression
# res = np.polyfit(x, f(x), deg=1, full=True) # deg=1 for linear regression
# ry = np.polyval(res[0], x)
# create_plot([x, x], [f(x), ry], ['b', 'r.'], 
#             ['f(x)', 'regression'], ['x', 'f(x)'])
# print(res) # res[0] contains the regression coefficients

# # Higher order polynomial regression with monomials up to order 5
# reg = np.polyfit(x, f(x), deg=5)
# ry = np.polyval(reg, x)
# create_plot([x, x], [f(x), ry], ['b', 'r.'], 
#             ['f(x)', 'regression'], ['x', 'f(x)'])

# # Fit a higher-degree polynomial
# degree = 12 # increased the polynomial degree for a more complex fit.
# reg = np.polyfit(x, f(x), degree)
# ry = np.polyval(reg, x)
# # is_close = np.allclose(f(x), ry)
# is_close = np.allclose(f(x), ry, atol=1e-2) # increased the tolerance to 1e-2
# print("Is close:", is_close) # True if the regression line is close to the original function
# print("Mean Squared Error:", np.mean((f(x) - ry) ** 2)) # Mean squared error
# create_plot([x, x], [f(x), ry], ['b', 'r.'], 
#             ['f(x)', 'regression'], ['x', 'f(x)'])

# # Individual basis functions
# matrix = np.zeros( (3+1, len(x)) ) # 3+1 because we want to fit a polynomial of degree 3
# matrix[3, :] = x ** 3 # x^3
# matrix[2, :] = x ** 2 # x^2
# matrix[1, :] = x # x
# matrix[0, :] = 1 # 1
# # reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0] # Least squares solution
# # reg.round(4) # The coefficients of the polynomial
# # ry = np.dot(reg, matrix) # The regression line
# # create_plot([x, x], [f(x), ry], ['b', 'r.'], 
# #             ['f(x)', 'regression'], ['x', 'f(x)'])
# matrix[3, :] = np.sin(x) # sin(x)
# reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0] # Least squares solution
# reg.round(4) # The coefficients of the polynomial
# ry = np.dot(reg, matrix) # The regression line
# is_close = np.allclose(f(x), ry)
# print("Is close:", is_close) # True if the regression line is close to the original function
# print("Mean Squared Error:", np.mean((f(x) - ry) ** 2)) # Mean squared error
# create_plot([x, x], [f(x), ry], ['b', 'r.'], 
#             ['f(x)', 'regression'], ['x', 'f(x)'])

# # Noisy Data
# xn = np.linspace(-2 * np.pi, 2 * np.pi, 50) # 50 points
# xn = xn + 0.15 * np.random.standard_normal(len(xn)) # Add noise
# yn = f(xn) + 0.25 * np.random.standard_normal(len(xn)) # Add noise
# reg = np.polyfit(xn, yn, 7) # Fit a polynomial of degree 7
# ry = np.polyval(reg, xn) # The regression line
# create_plot([x, x], [f(x), ry], ['b', 'r.'], 
#             ['f(x)', 'regression'], ['x', 'f(x)'])

# Unsorted data
xu = np.random.rand(50) * 4 * np.pi - 2 * np.pi # 50 random points in [-2pi, 2pi]
yu = f(xu) # The function values at the random points
print("xu:", xu[:10].round(2)) # Unsorted x values
print("yu:", yu[:10].round(2)) # Unsorted y values
reg = np.polyfit(xu, yu, 5) # Fit a polynomial of degree 5
ry = np.polyval(reg, xu) # The regression line
create_plot([xu, xu], [yu, ry], ['b.', 'ro'], 
            ['f(x)', 'regression'], ['x', 'f(x)'])
