from regression import best_fit
from regression import predict 
import numpy as np

# an example showing how the functions are meant to be used
# like everything, numpy arrays will come handy when it comes to data crunching 
x = np.array([1,5,7,9,11,12,15],dtype=np.float64)
y = np.array([2,4,6,9,12,14,18],dtype = np.float64)

slope, intercept = best_fit(x,y)
print(slope) #1.1985
print(predict(17,slope, intercept)) #19.3872
