import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import convolve
from sklearn import linear_model, datasets, metrics
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

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

logistic = linear_model.LogisticRegression();
rbm = BernoulliRBM(random_state=0, verbose=True);
classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)]);

###### Training

# Hyper-parameters using a grid search

rbm.learning_rate = 0.01
rbm.n_iter = 200
rbm.n_components = 100
rbm.batch_size=20;
logistic.C = 0.0001;
logistic.intercept_scaling=0.5;

# Training RBM-Logistic Pipeline

X_train, X_test, Y_train, Y_test = train_test_split(donorFeatures[:,0:3], donorFeatures[:,4], test_size=0.15, random_state=0)
rbmModel = classifier.fit(X_train,Y_train);

# Evaluation

print("Logistic regression using RBM synthesized features:\n%s\n" % (metrics.accuracy_score(Y_test, rbmModel.predict(X_test))))

# 68.75 percent accuracy
