Current state:

- Added script that does classification (3 donation amount classes) using an SVM.
- The script splits data into training and testing randomely using 10 fold cross validation
- Average cross validation accuracy is 60 percent (+- 25 percent)
  - E.g. on average, 6/10 samples are classified correcly
  - Model is shaky right now
- Need more data to train on and more features
  - User age
  - User historical donation data
  
Build a model to predict how much an individual is willing to donate to a given organization.
Features to look at:
- age of individual
- net worth of individual
- number of times donated to organization
- number of non profits involved in
- city that the individual lives in
