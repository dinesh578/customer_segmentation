from flask import Flask,render_template,request
import pickle
import jsonify
import requests
import sklearn
# import required libraries
import numpy as np
import pandas as pd

import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from preprocess import preprocess



app=Flask(__name__)
#model = pickle.load(open('C:\\Users\\Dinesh ram\\Downloads\\models\\clusrtering\\model.pkl', 'rb'))
model = pickle.load(open('C:\\Users\\Dinesh ram\\review.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':     
        Amount = float(request.form['Amount'])
        print(Amount)
        Frequency=float(request.form['Frequency'])
        print(Frequency)
        Recency=float(request.form['Recency'])
        print(Recency)
        input=[Amount,Frequency,Recency]
        print(input)
        l1=Amount
        l2=Frequency
        l3=Recency
        #df = pd.DataFrame(list(zip(l1, l2,l3)),columns =['Amount', 'Frequency','Recency'])
        #input1=df.head(1)
        data = pd.read_csv("C:\\Users\\Dinesh ram\\Downloads\\Cluster_AFR_data.csv")
        data = data.append({'Amount':Amount,'Frequency':Frequency, 'Recency':Recency,}, ignore_index=True)
        data=preprocess(data) 
        print(data)
        #print(data.head())
        #input1=StandardScaler(data)
        input1=data.tail(1)
        print(input1)
        input1=input1.iloc[0: ,0:]
        #input1=[Amount,Frequency,Recency]
        
        prediction=model.predict(input1)
        print(prediction)
        output=prediction
        print(output)
        if output<0:
            return render_template('index.html',prediction_text="Sorry something went wrong")
        else:
            return render_template('index.html',prediction_text="customer belongs to :"+str(output))
    else:
        return render_template('index.html')
        
        
    
if __name__=="__main__":
    app.debug = True
    app.run(debug=False)       
            
        
        
            