Current state:

- Added SVM, LR, and RBM LR script that does classification (3 donation amount classes).
  - RBM LR uses a Restricted Boltzmann Machine to synthesize hidden features using a neural network
- The script splits data into training and testing randomely using 10 fold cross validation
- Average cross validation accuracy is 70 percent for SVM, 60 percent for LR, and 68.75 percent for RBM LR right now

  
Build a model to predict how much an individual is willing to donate to a given organization.
Features to look at:
- age of individual
- net worth of individual
- number of times donated to organization
- number of non profits involved in
- city that the individual lives in
