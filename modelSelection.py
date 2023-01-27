from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.linear_model import LogisticRegression
from dataPreprocessing import data_preprocessing
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
    data = data_preprocessing()
    print(type(data))
    # Assigning the featurs as X and trarget as y
    X= data.drop(["TX_FRAUD"],axis =1)
    y= data["TX_FRAUD"]
    x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=7)
    algo_names = ["Decision Tree","Logistic Regression","Random Forest Classification","Gradient Boosting Classification","Linear Support Vector Classification","K Neighbours Classification"]
    algo = [dtc, lr, rfc, gbc, svc, knc] 
    
    #Finding AI Scores for each classifier
    Al_Scores = []
    j=0
    for i in algo:
        train = i.fit(x_train,y_train)
        score = train.score(x_test,y_test)
        Al_Scores.append(score)
        # print(score)
        print(algo_names[j],":",score)
        j+=1
    
    #Deciding final model
    max_value= max(Al_Scores)
    for i in range(len(Al_Scores)):
        if Al_Scores[i] == max_value:
            best_model = algo[i]
            best_model_name = algo_names[i]
    print("Best model is", best_model_name)

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
    
modelSelection()
