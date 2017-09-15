import matplotlib.pyplot as plt
from matplotlib import style
import cluster 
style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]
# [[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
# same as:
for i in dataset:
	for ii in dataset[i]:
		plt.scatter(ii[0],ii[1],s=100,color=i)
        
plt.scatter(new_features[0], new_features[1], s=100)

result = cluster.k_nearest_neighbors(dataset, new_features,3)
plt.scatter(new_features[0], new_features[1], s=100, color = result)  
plt.show()