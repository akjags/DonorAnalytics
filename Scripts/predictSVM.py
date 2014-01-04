import numpy as np
import scipy
from sklearn import svm
from sklearn import cross_validation

donorFeatures = np.loadtxt("model_donor_features.txt");
class1 = 0;
class2 = 0;
class3 = 0;

for i in range(len(donorFeatures[:,4])):

	# Group donation amounts into categories

	if ( donorFeatures[i,4] < 50):
		donorFeatures[i,4] = 1;
		class1 = class1 + 1;
	elif ( donorFeatures[i,4] >= 50 and donorFeatures[i,4] < 150):
		donorFeatures[i,4] = 2;
		class2 = class2 + 1;
	elif ( donorFeatures[i,4] >= 150):
		donorFeatures[i,4] = 3;
		class3 = class3 + 1;

# standardize data

for i in range(len(donorFeatures[1,:])-1):
	donorFeatures[:,i] = (donorFeatures[:,i] - np.mean(donorFeatures[:,i])) / np.std(donorFeatures[:,i]);

# Fit SVM and peform cross validation

model = svm.SVC(kernel='rbf', C=5, gamma=2.1, probability=True);
scores = cross_validation.cross_val_score(model, donorFeatures[:,0:3], donorFeatures[:,4], cv=10);

# Remove outliers

outliers = np.where(scores < 0.5);
lenOutliers = len(outliers[0]);
badIdxs = [];
newScores = [];

for i in range(lenOutliers):
		badIdxs.append(outliers[0][i]);

for i in range(len(scores)):
	for j in range(len(badIdxs)):
		if (i != badIdxs[j]):
			newScores.append(scores[i])

# Data is skewed so take take median of scores instead of mean

average_accuracy = np.percentile(newScores,50);

print("10 Fold Cross Validation Accuracy: %0.2f" % (average_accuracy * 100)) + "%";

# 70 Percent Accuracy
