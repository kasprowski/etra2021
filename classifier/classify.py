'''
Module using sklearn package to classify samples
@author: pawel@kasprowski.pl
'''

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

import numpy as np

# classifies all points from (0,0) to (rangex,rangey) 
# using samples with labels as training data 
def classification(model_name,samples,labels,rangex,rangey):
    samples = np.array(samples)
    labels = np.array(labels)

    # build the model
    models = {
        "KNN": KNeighborsClassifier(),
        "LDA": LinearDiscriminantAnalysis(),
        "NB": GaussianNB(),
        "TREE":DecisionTreeClassifier(),
        "RF":RandomForestClassifier(n_estimators=20),
        "SVM":SVC(gamma='scale'), 
        "PERC":Perceptron(max_iter=2000), 
        "GB":GradientBoostingClassifier()
    }
    model = models.get(model_name)
    
    # train the model
    model.fit(samples, labels)    
    print("classifier",model," - created")    
    
    # build the matrix of results using the model   
    result = np.zeros([rangex,rangey])
    for x in range(rangex):
        for y in range(rangey):
            sample = np.array([x,y])
            result[x][y] = model.predict(sample.reshape(1, -1))
            #sample = np.array([[x,y]])
            #result[x][y] = model.predict(sample)
            
                
    return result            



