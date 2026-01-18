import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import  train_test_split

X,y =load_iris(return_X_y=True)
X_train , X_test , y_train , y_test = train_test_split ( X ,y , test_size =0.2 , random_state =42 ) 

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", SVC())
])

param_grid = {
    "model__C": [0.1, 1, 10],
    "model__kernel": ["linear", "rbf"]
}

from sklearn.model_selection import GridSearchCV
 
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)