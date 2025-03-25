## Chapter 4: Data Analysis 
## 4.1 Data Preparation  
The first figure bellow shows the structure of the dataset where all attributes are shown, 
with their type, in addition to glimpse of the variables within each attribute, as shown at 
the end of the figure the Class type is integer which I needed to change to factor and 
identify the 0 as Not Fraud and the 1 as Fraud to ease the process of creating the model 
and obtain visualizations  
 1 - Dataset Structure   
The second figure shows the distribution of the class, the red bar which contains 284,315 
variables represents the non-fraudulent transactions, and the blue bar with 492 variables 
represents the fraudulent transactions. 
 2 - Class Distribution 
 Correlation between attributes “Image from R” 
The correlations between all the of the attributes within the dataset are presented in the 
3 - Correlations   
4.1.2 Attribute with the most fraud  
  below shows attribute 18 the attribute with the most credit card fraudulent 
transactions, the blue line represents the variable 1 which is the fraudulent transactions. 
 4 – Variable 18 
4.1.3 Attribute with the less fraud  
The figure below shows the variable that have the lowest number of fraudulent transactions, 
as mentioned earlier the blue line represents the fraudulent instances within the dataset.  
## 4.2 Data Preprocessing  
As there are no NAs nor duplicated variables, the preparation of the dataset was simple 
the first alteration that was made to be able to open the dataset on Weka program is 
changing the type of the class attribute from Numeric to Class and identify the class as 
{1,0} using the program Sublime Text. Another alteration was made on the type as well 
on the R program to be able to create the model and the visualization. 
## 4.3 Data Modeling 
After making sure that the data is ready to get modeled the four models were created 
using both Weka and R. the model SVM was created using Weka only, as for KNN, 
Logistic Regression and NaïveBayes they were created using R and Weka. 
## 4.3.1 KNN 
The K-Nearest Neighbor algorithm (KNN) is a supervised ML technique that can be 
applied in both scenario instances, classification instances along with regression 
instances (Mahesh, 2020).
## 4.3.2 Naïve Bayes  
Naïve Bayes is a classification algorithm that consider the being of a certain trait within a 
class is unrelated to the being of any different feature, the main use of it is for clustering 
and classifications, depending on the conditional probability of happening (Mahesh, 
2020). 
The second model created by R is Naïve Bayes, figure 9 shows the performance of the 
model, it scored an accuracy of 97.77% and misclassified a total of 2,051 transactions, 
33 fraudulent as nonfraudulent and 2018 nonfraudulent as fraudulent. There is a slight 
difference in the accuracy of the Naïve bayes model created within Weka as its 97.73% 
## 4.3.3 Logistic Regression 
Logistic Regression model is statical model where evaluations are formed of the 
connection among dependent qualitative variable (binary or binomial logistic regression) 
or variable with three values or higher (multinomial logistic regression) and one 
independent explanatory variable or higher whether qualitative or quantitative 
(Domínguez-Almendros et al., 2011). 
The last model created using both R and Weka is Logistic Regression, the model 
managed to score and accuracy of 99.92% in R (figure 11) with 70 misclassified 
instances, while it scored 99.91% in Weka with 77 misclassified instances as presented 
  
## 4.3.4 Support Vector Machine  
Support Vector machine is a supervised ML technique with connected learning algorithms 
which inspect data used for both classification and regression analyses, it also performs 
linear classification, additionally to non-linear classification by creating margins between 
the classes, which are created in such a fashion that the space between the margin and 
the classes is maximum which minimizes the error of the classification (Mahesh, 2020). 
Finally, the model Support Vector Machine as show in figure 12 managed to score 
99.94% for the accuracy and misclassified 51 instances.
 
## 4.4 Evaluation and Deployment 
The last stage of the CRISP-DM model is the evaluation and deployment stage, as 
presented in table 2 below all models are being compared to each other to figure the best 
model in identifying fraudulent credit card transactions.  
Accuracy is the overall number of instances that are predicted correctly, accuracies are 
represented by confusion matrix where it showed the True Positive (TP), True Negative 
(TN), False Positive (FP) and False Negative (FN). True Positive represents the 
transactions that are fraudulent and was correctly classified by the model as fraudulent. 
True Negative represents the not fraudulent transactions that were correctly predicted by 
the model as Not fraudulent. The third rating is False positive which represents the 
transaction that are fraudulent but was misclassified as not  fraudulent. And finally False 
Negative  which are the not fraudulent transactions that were identified as fraudulent
 the confusion matrix. 

 
