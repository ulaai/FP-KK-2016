from sklearn.cluster import KMeans
from matplotlib import pyplot
import numpy as np
import csv

with open("votes.csv", 'rb') as csvfile:
	lines = csv.reader(csvfile)
	headers = lines.next()
	dataset = list(lines)

kmeans = KMeans(n_clusters = 2, random_state = 0)
kmeans.fit(dataset)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
ds = np.array(dataset)

for i in range(2):
	ds = ds[np.where(labels==i)]
	print len(ds)
	pyplot.plot(ds[:,0], ds[:,1], 'o')
	lines = pyplot.plot(centroids[i,0], centroids[i,1], 'kx')
	pyplot.setp(lines,ms=15.0)
	pyplot.setp(lines,mew=2.0)
pyplot.title('Votes')
pyplot.show()
#pyplot.savefig('allattributes.png')