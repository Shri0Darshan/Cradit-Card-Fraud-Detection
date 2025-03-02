# Chapter 2: Literature Review

# 2.1 Introduction  
It is essential for credit card companies to establish credit card transactions that 
fraudulent from transactions that are non-fraudulent, so that their customers’ accounts 
won’t get affected and charged for products that the customers didn’t buy (Maniraj et al., 
2019). There are many financial Companies and institutions that lose massive amounts 
of money because of fraud and fraudsters that are seeking different approaches 
continuously to violate the rules and commit illegal actions; therefore, systems of fraud 
detection are essential for all banks that issue credit cards to decrease their losses 
(Zareapoor et al., 2012). There are multiple methods used to detect fraudulent behaviors 
such as Neural Network (NN), Decision Trees, K-Nearest Neighbor algorithms, and 
Support Vector Machines (SVM). Those ML methods can either be applied independently 
or can be used collectively with the addition of ensemble or meta-learning techniques to 
develop classifiers (Zareapoor et al., 2012).

# 2.2 Literature Review  
Zareapoor and his research team used multiple techniques to determine the best 
performing model in detecting fraudulent transactions, which was established using the 
accuracy of the model, the speed in detecting and the cost. The models used were Neural 
Network, Bayesian Network, SVM, KNN and more. The comparison table provided in the 
research paper showed that Bayesian Network was very fast in finding the transactions 
that are fraudulent, with high accuracy. The NN performed well as well as the detection 
was fast, with a medium accuracy. KNN’s speed was good with a medium accuracy, and 
finally SVM scored one of the lower scores, as the speed was low, and the accuracy was 
medium. As for the cost All models built were expansive (Zareapoor et al., 2012). 
The model used by Alenzi and Aljehane to detect fraud in credit cards was Logistic 
Regression, their model scored 97.2% in accuracy, 97% sensitivity and 2.8% Error Rate. 
A comparison was performed between their model and two other classifier which are 

Voting Classifier and KNN. VC scored 90% in accuracy, 88% sensitivity and 10% error 
rate, as for KNN where k = 1:10, the accuracy of the model was 93%, the sensitivity 94% 
and 7% for the error rate (Alenzi & Aljehane, 2020). 
Manirajs team built a model that can recognize if any new transaction is fraud or non
fraud, their goal was to get 100% in the detection of fraudulent transactions in addition to 
trying to minimize the incorrectly classified fraud instances. Their model has performed 
well as they were able to get 99.7% of the fraudulent transactions (Maniraj et al., 2019). 
The classification approach used by Dheepa and Dhanapal was the behavior-based 
classification approach, by using Support Vector Machine, where the behavioral patterns 
of the customers were analyzed to distinguish credit card fraud, such as the amount, date, 
time, place, and frequency of card usage. The accuracy achieved by their approach was 
more than 80% (Dheepa & Dhanapal, 2012).  
Mailini and Pushpa proposed using KNN and Outlier detection in identifying credit card 
fraud, the authors found after performing their model over sampled data, that the most 
suited method in detecting and determining target instance anomaly is KNN which 
showed that its most suited in the detection of fraud with the memory limitation. As for 
Outlier detection the computation and memory required for the credit card fraud detection 
is much less in addition to its working faster and better in online large datasets. But their 
work and results showed that KNN was more accurate and efficient (Malini & Pushpa, 
2017). 
Maes and his team proposed using Bayesian and Neural Network in the credit card fraud 
detection. Their results showed that Bayesian performance is 8% more effective in 
detecting fraud than ANN, which means that in some cases BBN detects 8% more of the 
fraudulent transactions. In addition to the Learning times, ANN can go up to several hours 
whereas BBN takes only 20 minutes (Maes et al., 2002). 
The team of Awoyemi compared the usage of three ML techniques in the detection of  
credit card fraud, the first is KNN, the second is Naïve Bayes and the third is Logistic 
Regression. They sampled different distributions to view the various outcomes. The top 
Accuracy of the 10:90 distribution is Naïve Bayes with 97.5%, then KNN with 97.1%, 
 
Logistic regression performed poorly as the accuracy is 36.4%. Another distribution that 
was viewed is 34:66, KNN topped the chart with a slight increase in the accuracy 97.9%, 
then Naïve Bayes with 97.6%,  Logistic Regression performed better in this distribution 
as the accuracy raised to 54.8% (Awoyemi et al., 2017). 
Jain’s team used several ML techniques to distinguish credit card fraud, three of them are 
SVM, ANN and KNN. Then to compare the outcome of each model, they calculated the 
true positive (TP), false negative (FN), false positive (FP), and true negative (TN) 
generated. ANN scored 99.71% accuracy, 99.68% precision, and 0.12% false alarm rate. 
SVM accuracy is 94.65%, 85.45% for the precision, and 5.2% false alarm rate. and finally, 
the accuracy of KNN is 97.15%, precision is 96.84% and the false alarm rate is 2.88% 
  
Gupta’s team worked on implementing an automated model that uses various ML 
techniques to detect fraudulent instances that are related economically to users but is 
specializing more in credit card transactions, according to Gupta and his team Out of all 
the techniques that they used Naïve Bayes had an outstanding performance in 
distinguishing fraudulent transactions as the accuracy of it was 80.4% and the area under 
the curve is 96.3% (Gupta et al., 2021). 
Adepoju and his team used all of the ML methods that are used in this paper, Logistic 
Regression , (SVM) Support Vector Machine, Naive Bayes, and (KNN) K-Nearest 
Neighbor, those methods were used on distorted credit card fraud data. The accuracies 
scored by all the models were 99.07% for Logistic Regression, Naïve Bayes scored 
95.98%, 96.91% for K-nearest neighbor, and the last model (SVM) Support Vector 
Machine scored 97.53% (Adepoju et al., 2019). 
 

The team of Varmedja used multiple machine learning algorithms in their paper such as 
Logistic Regression, Multilayer Perception, Random Forest, and Naïve Bayes. As the 
dataset was quite very unbalanced Varmedja and his team SMOTE technique to 
oversample, feature selection, in addition to sectioning the data into a training section and 
a testing data section. The best scoring model during the experiment is Random Forest 
with 99.96%, with not many difference the model in second place is Multilayer Perceptron 
with 99.93%, in third place is Naïve bayes with 99.23% and in last place is Logistic 
regression with 97.46% (Varmedja et al., 2019). 
The system to detect credit card fraud that was introduced by Sailusha and his team to 
detect fraudulent activities. The algorithms used in their model is adaboost and Random 
Forest, which scored the accuracy 93.99% and the accuracy of adaboost is 99.90% which 
shows that it did better than Random Forest in term of accuracy (Sailusha et al.). 
The paper of Kiran and his team presents Naïve Bayes (NB) improved (KNN) K-Nearest 
Neighbor method for Fraud Detection of Credit Card which is (NBKNN) in short format. 
The outcome of the experiment illustrates the difference in the process of each classifier 
on the same dataset. Naïve bayes performed better than K-nearest neighbor as it scored 
an accuracy of 95% while KNN scored 90% (Kiran et al., 2018). 
Najdat and his team’s approach in detecting fraudulent transactions is (BiLSTM) BiLSTM- 
MaxPooling-BiGRU- MaxPooling, this approach is established upon bidirectional Long 
short-term memory in addition to (BiGRU) bidirectional Gated recurrent unit. In addition, 
the group decided to go for six ML classifiers, which are Voting, Adaboost, Random 
Forest, Decision Tree, Naïve bayes, and Logistic Regression.  K-nearest neighbor scored 
an accuracy of 99.13%, and logistic regression scored 96.27%, Decision tree scored 
96.40% and Naïve bayes scored 96.98% (Najadat et al., 2020). 
The paper of Saheed and his group focuses on detection of Credit Card Fraud with the 
use of (GA) Genetic Algorithm as a feature selection technique. In feature selection the 
data is splitted in two parts first priority features and second priority features, and the ML 
techniques that the group used are The Naïve Bayes (NB), Random Forest (RF) and 
(SVM) Support Vector Machine. Naïve bayes scored 94.3%, SVM scored 96.3%, and 
Random Forest scored 96.40% which is the highest accuracy (Saheed et al., 2020). 

The work of Itoo and his group uses three different ML methods the first is logistic 
regression, the second is Naïve bayes and the last one is K-nearest neighbors. Itoo and 
his group recorded the work and comparative analysis, their work is implemented on 
python. Logistic regression accuracy is 91.2%, Naïve bayes accuracy is 85.4% and K
nearest neighbor is last with an accuracy of 66.9% (Itoo et al., 2020). 
The team of Tanouz proposed working on various ML based classification algorithms, like 
Naïve Bayes, Logistic Regression, Random Forest, and Decision Tree in handling 
datasets that are strongly imbalanced, in addition their research will have the calculations 
of five measures the first is accuracy, the second is precision, the third is recall, the fourth 
is confusion matrix, and the last one is Roc-auc score. 95.16% is the score of both Logistic 
Regression and Naïve Bayes, 96.77% is the score for random forest, for the last model 
Decision Tree scored 91.12%  (Tanouz et al., 2021). 
Dighe and his team used KNN, Naïve Bayes, Logistic Regression and Neural Network, 
Multi-Layers Perceptron and Decision Tree in their work, then evaluated the results in 
terms of numerous accuracy metrics. Out of all the models created the best performing 
one is KNN which scored 99.13%, then in second place Naïve Bayes which scored 
96.98%, the third best performing model 96.40% and in last place is logistic regression 
with 96.27% (Dighe et al., 2018). 
The paper of Bhanusri and his team implemented multiple ML techniques on an 
unbalanced dataset. The ML methods used are logistic regression, naïve bayes, and 
random forest to explain the relation of fraud and credit card. Their conclusion of the 
project presents the best classifier by training and testing supervised techniques in term 
of their work. The logistic regression model scored 99.8% accuracy, random forest scored 
100% and 90.8% is scored by naïve bayes. 
Sahin and Duman used four Support Vector Machine methods in detecting credit card 
fraud. SVM) Support Vector Machine with RBF, Polynomial, Sigmoid, and Linear Kernel, 
all models scored 99.87% in the training model and 83.02% in the testing part of the 
model (Sahin & Duman, 2011). 
  
# 2.3 Literature Review Conclusion  
Throughout the search I found that there were many models created by other researchers 
which have proven that people have been trying to solve the credit card fraud problem. I 
found that Najdat Team used an approach that is established upon bidirectional 
long/short-term memory in building their model, other researchers have tried different 
data splitting ratios to generate different accuracies. The team of Sahin and Duman used 
different Support Vector Machine methods which are (SVM) Support Vector Machine with 
RBF, Polynomial, Sigmoid, and Linear Kernel.  
The lowest accuracy of the four models that will be studied in this research, is 54.86% for 
KNN and 36.40% for logistic Regression which were scored by Awoyemi and his team, 
as for Naïve Bayes the lowest accuracy was scored by Gupta and his team which is 
80.4% and finally, SVM the lowest score was 94.65% and it was scored by Jain’s team. 
To determine the best model out of the four models that will be studied through the 
research, the average of the best three accuracies of each model will be calculated, the 
average of the accuracy of KNN is 98.72%, the average of logistic regression is 98.11%, 
98.85% for Naïve bayes and 96.16% for Support Vector Machine. So, for the best 
performing credit card fraud detecting model within the Literature review is the Logistic 
Regression model
