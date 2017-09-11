from statistics import mean
import numpy as np

# HELPER FUNCTION CONCERNING LINEAR REGRESSION



def best_fit(x,y):
# this is a simple function which returns the slope and intercept
# of a best fit line that could classify the given linear data
# the input is a np.array of the values of ordinate and mantissa

	slope = (((mean(x)*mean(y)) - mean(x*y)) /
		((mean(x)**2) - mean(x*x)))

	intercept = mean(y)-slope*(mean(x))

	return slope, intercept

def predict(x_predict,slope,intercept):
	# a function that would predict and return value of y after 
	# passing through best fit

	return ((slope*x_predict)+intercept)


