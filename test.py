import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import streamlit as st

# Load dataset
df = pd.read_csv("creditcard_2023.csv")  # Ensure you have the dataset in the working directory
df.head()
normal = df[df.Class==0.0]
Fraud = df[df.Class==1.0]

normal_sample = normal.sample(n=len(Fraud),random_state=2)
df=pd.concat([normal_sample,Fraud],axis=0)

x=df.drop("Class",axis=1)
y= df["Class"]
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2, stratify=y)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
train_accuracy = accuracy_score(model.predict(X_train),y_train)
test_accuracy =accuracy_score(model.predict(X_test),y_test)

#web app
st.title("Cradit card Fraud Detection Model")
input_df = st.text_input("Enter all Required Features values")
input_df_splited = input_df.split(",")
submit = st.button("submit")

if submit:
   features =np.asarray(input_df_splited,dtype=np.float64)
   prediction = model.predict(features.reshape(1,-1))

   if prediction[0] == 0:
      st.write("Normal Transaction")
   else:
      st.write("Fraud Transaction")