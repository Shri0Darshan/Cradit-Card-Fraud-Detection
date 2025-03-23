
##Chapter 3: Project Description
#3.1 Introduction
In order to accomplish the objective and goal of the project which is to find the most
suited model to detect credit card fraud several steps need to be taken. Finding the most
suited data and preparing/preprocessing are the first and second steps, after making sure
that the data is ready the modeling phase starts, where 4 models are created, K-Nearest
Neighbor (KNN) , Naïve Bayes, SVM and the last one is Logistic Regression. In the KNN
model two Ks were chosen K=3 and K=7. All models were created in both R and Weka
programs expect SVM which was created in Weka only, in addition all visualizations are
taken from both applications.
#3.2 Data Source
The dataset was retrieved from an open-source website, Kaggle.com. it contains data of
transactions that were made in 2013 by credit card users in Europe, in two days only. The
dataset consists of 31 attributes, 284,808 rows. 28 attributes are numeric variables that
due to confidentiality and privacy of the customers have been transformed using PCA
transformation, the three remaining attributes are “Time” which contains the elapsed
seconds between the first and other transactions of each attribute, “Amount” is the
amount of each transaction, and the final attribute “Class” which contains binary variables
where “1” is a case of fraudulent transaction, and “0” is not as case of fraudulent
transaction.
Dataset Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
