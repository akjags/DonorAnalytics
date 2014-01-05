Current state:

- Added SVM, LR, RBM LR, and RBM SVM scripts that do classification (3 donation amount classes)
  - 1. RBM SVM - 76.45 percent accuracy
  - 2. RBM Logistic Regression - 70.59 percent accuracy
  - 3. Simple SVM - 70 percent accuracy
  - 4. Simple Logistic Regression - 62 percent accuracy
- RBM (Restricted Boltzmann Machine) is a model that is used to synthesize hidden features using a neural network
  - Combination with classifers greatly improves accuracy
- The scripts split data into training and testing randomely

Build a model to predict how much an individual is willing to donate to a given organization.
Features to look at:
- age of individual
- net worth of individual
- number of times donated to organization
- number of non profits involved in
- city that the individual lives in
