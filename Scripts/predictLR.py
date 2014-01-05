import numpy as np
import scipy
from sklearn.linear_model import LogisticRegression
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

# Fit Logistic Regression Model and peform cross validation

model = LogisticRegression(C=0.0001);
scores = cross_validation.cross_val_score(model, donorFeatures[:,0:3], donorFeatures[:,4], cv=10);

average_accuracy = np.percentile(scores,50);

print("10 Fold Cross Validation Accuracy: %0.2f" % (average_accuracy * 100)) + "%";

# 62 Percent Accuracy
