# Chapter 1
# 1.1 Introdution
With the increase of people using credit cards in their daily lives, credit card companies 
should take special care in the security and safety of the customers. According to (Credit 
card statistics 2021) the number of people using credit cards around the world was 2.8 
billion in 2019, in addition 70% of those users own a single card at least.  
Reports of Credit card fraud in the US rose by 44.7% from 271,927 in 2019 to 393,207 
reports in 2020. There are two kinds of credit card fraud, the first one is by having a credit 
card account opened under your name by an identity thief, reports of this fraudulent 
behavior increased 48% from 2019 to 2020. The second type is by an identity thief uses 
an existing account that you created, and it’s usually done by stealing the information of 
the credit card, reports on this type of fraud increased 9% from 2019 to 2020 (Daly, 2021). 
Those statistics caught my attention as the numbers are increasing drastically and rapidly 
throughout the years, which gave me the motive to try to resolve the issue analytically by 
using different machine learning methods to detect the credit card fraudulent transactions 
within numerous transactions. 
# 1.2 Project goals
The main aim of this project is the detection of credit card fraudulent transactions, as it’s 
important to figure out the fraudulent transactions so that customers don’t get charged for 
the purchase of products that they didn’t buy. The detection of the credit card fraudulent 
transactions will be performed with multiple ML techniques then a comparison will be 
made between the outcomes and results of each technique to find the best and most 
suited model in the detection of the credit card transaction that are fraudulent, graphs and 
numbers will be provided as well. In addition, exploring previous literatures and different 
techniques used to distinguish the fraud within a dataset.
# 1.3 Research Methodology
A)Phase 1:- Business Understanding
As stated before credit card fraud is increasing drastically every year, many people are 
facing the problem of having their credits breached by those fraudulent people, which is 
impacting their daily lives, as payments using a credit card is similar to taking a loan. If 
the problem is not solved many people will have large amounts of loans that they cannot 
pay back which will make them face a hard life, and they won’t be able to afford necessary 
products, in the long run not being able to pay back the amount might lead to them going 
to jail. Basically, the problem proposed is the detection of the credit card fraudulent 
transactions made by fraudsters to stop those breaches and to ensure customers 
security.
B) phase 2:- Data Understanding
In the Data understanding phase, it was  critical to obtain a high-quality dataset as the 
model is based on it, the dataset was explored by taking a closer look into it which gave 
the knowledge needed to confirm the quality of the dataset, additionally to reading the 
description of the whole dataset and each attribute. It’s also important to have a dataset 
that contains several mixed transaction types “Fraudulent and real” and a class to clarify 
the type of transaction, finally, identifiers to clarify the reason behind the classification of 
the transaction type. I made sure to follow all of those points during the search for the 
most suited dataset.
C) phase 3:-Data Preparation
After choosing the most suited dataset the preparation phase begins, the preparation of 
the dataset includes selecting the wanted attributes or variables, cleaning it by excluding 
Null rows, deleting duplicated variables, treating outlier if necessary, in addition to 
transforming data types to the wanted type, data merging can be performed as well where 
two or more attributes get merged. All those alterations lead to the wanted result which is 
to make the data ready to be modeled.  
The dataset chosen for this project didn’t need to go through all of the alterations 
mentioned earlier, as there were no missing nor duplicated variables, there was no 
merging needed as well. But there was some changing in the types of the data to be able 
to create graphs, in addition to using the application Sublime Text to be able to insert the 
data into Weka and perform analysis, as it needed to be altered

D) phase 4:-  Modeling
Four machine learning models were created in the modeling phase, KNN, SVM, Logistic 
Regression and Naïve Bayes. A comparison of the results will be presented later in the 
paper to know which technique is most suited in the credit card fraudulent transactions 
detection. The dataset is sectioned into a ratio of 70:30, the training set will be the 70% 
and remaining set will be the testing set which is the 30%. The four models were created 
using Weka and only two in R, KNN and Naïve Bayes. Visualizations will be provided 
from both tools.
