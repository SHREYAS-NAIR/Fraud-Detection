from dataSpliting import data_Spliting
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')
# Mentioning the models for Classification
dtc = tree.DecisionTreeClassifier()
rfc = RandomForestClassifier()
gbc = GradientBoostingClassifier()
lr = LogisticRegression()
knc = KNeighborsClassifier()
svc = LinearSVC()

def modelSelection():
    x_train, x_test, y_train, y_test = data_Spliting()
    
    #Name of algorithms used.
    algo_names = ["Decision Tree","Logistic Regression","Random Forest Classification","Gradient Boosting Classification","Linear Support Vector Classification","K Neighbours Classification"]
    algo = [dtc, lr, rfc, gbc, svc, knc] 
    
    print("Selecting the best model")
    #Finding AI Scores for each classifier.
    Al_Scores = []
    j=0
    for i in algo:
        train = i.fit(x_train,y_train)
        score = train.score(x_test,y_test)
        Al_Scores.append(score)
        # print(score)
        print(algo_names[j],":",score*100)
        j+=1
    
    #Deciding final model
    max_value= max(Al_Scores)
    for i in range(len(Al_Scores)):
        if Al_Scores[i] == max_value:
            best_model = algo[i]
            best_model_name = algo_names[i]
    print("The best model is", best_model_name)

    #Finding metrics for the best model and printing them
    y_predict = best_model.predict(x_test)
    precision = precision_score(y_test, y_predict, pos_label='positive', average='micro')
    recall = recall_score(y_test, y_predict, pos_label='positive', average='micro')
    accuracy = accuracy_score(y_test, y_predict)
    f1score = f1_score(y_test, y_predict, pos_label='positive', average='micro')

    print("Precision = ", precision)
    print("f1score = ", f1score)
    print("recall = ", recall)
    print("accuracy = ", accuracy)

    #Creating pickle file for best model
    print("Creating pickel file.")
    pickle.dump(best_model, open('model.pkl', 'wb'))
    
modelSelection()