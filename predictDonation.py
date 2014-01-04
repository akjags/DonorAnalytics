import numpy as np
import scipy
import csv
from sklearn import svm

donorFeatures = np.loadtxt("donorAnalyticsFeatures.txt");

for i in range(len(donorFeatures[:,3])):

	# Group donation amounts into categories
	if ( donorFeatures[i,3] < 90):
		donorFeatures[i,3] = 1;
	elif ( donorFeatures[i,3] >= 90 and donorFeatures[i,3] < 250):
		donorFeatures[i,3] = 2;
	elif ( donorFeatures[i,3] >= 250):
		donorFeatures[i,3] = 3;

svmModel = svm.SVC(C=10, gamma=1);

model = svmModel.fit(donorFeatures[:,0:2], donorFeatures[:,3]);
predLabels = model.predict(donorFeatures[:,0:2]);
labelMatch = np.zeros((len(predLabels), 1));

for i in range(len(predLabels)):
	if (predLabels[i] == donorFeatures[i,3]):
		labelMatch[i] = 1;
	else:
		labelMatch[i] = 0;

sumLabelMatch = sum(labelMatch);
predictionAccuracy = sumLabelMatch/len(labelMatch);

print "Training Set Prediction Accuracy (SVM): " + str(predictionAccuracy * 100) + "%";















