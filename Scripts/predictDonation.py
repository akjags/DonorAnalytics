import numpy as np
import scipy
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import cross_validation

donorFeatures = np.loadtxt("modelData1.txt");
class1 = 0;
class2 = 0;
class3 = 0;

for i in range(len(donorFeatures[:,3])):

	# Group donation amounts into categories

	if ( donorFeatures[i,3] < 60):
		donorFeatures[i,3] = 1;
		class1 = class1 + 1;
	elif ( donorFeatures[i,3] >= 60 and donorFeatures[i,3] < 200):
		donorFeatures[i,3] = 2;
		class2 = class2 + 1;
	elif ( donorFeatures[i,3] >= 200):
		donorFeatures[i,3] = 3;
		class3 = class3 + 1;

print "Number of Class 1 Samples: " + str(class1);
print "Number of Class 2 Samples: " + str(class2);
print "Number of Class 3 Samples: " + str(class3);

# Classes are imbalanced right now - most people are in class 1

meanData0 = np.mean(donorFeatures[:,0]);
stdData0 = np.std(donorFeatures[:,0]);

meanData1 = np.mean(donorFeatures[:,1]);
stdData1 = np.std(donorFeatures[:,1])

meanData2 = np.mean(donorFeatures[:,2]);
stdData2 = np.std(donorFeatures[:,2])

# Standardize Data

donorFeatures[:,0] = (donorFeatures[:,0] - meanData0) / stdData0;
donorFeatures[:,1] = (donorFeatures[:,1] - meanData1) / stdData1;
donorFeatures[:,2] = (donorFeatures[:,2] - meanData2) / stdData2;

# Fit SVM and peform cross validation

model = svm.SVC(kernel='rbf', C=100, gamma=2.1);
scores = cross_validation.cross_val_score(model, donorFeatures[:,0:2], donorFeatures[:,3], cv=10);

print("10 Fold Cross Validation Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2));
print scores
