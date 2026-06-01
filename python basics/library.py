# Library importing and implementation

import numpy as np                       # numerical python(array)
from numpy import random                 # random code generator
import matplotlib.pyplot as plt          # For graphs plotting
import pandas as pd                      # Panel data -> data manipulation (series , data frames)
from mpl_toolkits.mplot3d import Axes3D  # 3D graphs plotting
import tensorflow as tf                  # Tensorflow -> Deeplearning framework for AI learning (Complex computation)

# Scikit learn features
'''
from sklearn.datasets import load_breast_cancer, fetch_california_housing         # Loading a dataset , fetch -> used to get dataset from internet
from sklearn.datasets import load_iris                  # dataset related to flowers info.
from sklearn.model_selection import train_test_split    # Splitting data for training and testing
from sklearn.preprocessing import StandardScaler        # Scaling the data
from sklearn.datasets import make_blobs,make_moons      # Clustering data, making other structures also
from sklearn.datasets import fetch_openml               # to get any other dataset
from sklearn.preprocessing import OrdinalEncoder             # encoding of the data in machines 

from sklearn.neighbors import KNeighborsClassifier as knn     # Algorithm for prediction
from sklearn.linear_model import LogisticRegression           # classifiers with different mathematical classification logic
from sklearn.tree import DecisionTreeClassifier         
from sklearn.ensemble import RandomForestClassifier           # Strongest classifier model

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet         # Regression models used
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.cluster import KMeans             # Clustering algorithm

from sklearn.decomposition import PCA          # Principle component analysis (PCA)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score     # Score metrics
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, root_mean_squared_error

from sklearn.model_selection import cross_val_score,GridSearchCV  # Cross valid

from sklearn.pipeline import Pipeline                             # Pipelining
'''

# tensorflow keras API used
'''
from tensorflow import keras              # importing keras API
from keras import layers,models,losses    # importing all other modules
from keras.models import Sequential       # importing features from modules
from keras.layers import Dense, Flatten, Input, Dropout
from keras.losses import SparseCategoricalCrossentropy      # loss calculation
from keras.optimizers import Adam           # for compiling the model
'''

#_____________________________________________________
# Numpy operations:
#_____________________________________________________

'''
lst1 =[1,2,3,4,'d',6.5,'l','b',9]   #heterogenous 
print(lst1,type(lst1))

arr1=np.array([1,2.5,'d',4,'l',6,'u',8,9])  #homogenous
print(arr1,type(arr1))

lst2=[1,2,3,4,5]
arr2=np.array([1,2,3,4,5])
print(lst2*6)       #iterative 
print(arr2*6)       #operation on each element

lst3=[1,2,3,4] +[5]
                            #lst4=[1,2,3,4] + 5 (error)
for i in lst3:
    lst3.append(i*5)
print(lst3)

arr3=np.array([5,4,3,2,1])    #vectorised operation
print(arr3+5)
print(arr3*5)

arr4=np.array([5,4,3,2,1])
print(arr4.ndim)
print(arr4.shape)

arr5=np.array([1,2,3],[4,5,6],[7,8,9])
print(arr5)

arr1=np.array([1,2,3])
print('1 d array: \n',arr1)
print('dimension of the array: ',arr1.ndim)
print('shape: ',arr1.shape,'\n')

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('2 d array: \n',arr2)
print('dimension of the array: ',arr2.ndim)
print('shape: ',arr2.shape,'\n')

arr3=np.array([[[1,2,3]]])
print(arr3)
print('dimension of the array: ',arr3.ndim)
print('shape: ',arr3.shape)

arr4=np.array([[[2,4,5,8],[1,2,3,0],[2,2,0,9]],[[2,4,5,8],[1,2,3,0],[2,2,0,9]]])
print(arr4)
print('shape: ',arr4.shape)

arr5=np.array([[[4,6,3,4],[5,6,6,8]],[[3,4,5,3],[10,43,45,46]]])
print(arr5)
print('shape: ',arr5.shape)

arr6=np.array([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[1,2,3]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
print('maximum dimension: ',arr6.ndim)                                        # maximum dimensions for an array (32)

anyar1=np.zeros([5],dtype=int)
print(anyar1,'\n')

anyar2=np.zeros([2,2,2],dtype=int)
print(anyar2,'\n')

anyar3=np.ones([3,3,3],dtype=int)
print(anyar3,'\n')

arrw=np.full([2,3,4],10,dtype=int)                # variable=np.full(shape,value,dtype=)
print(arrw,'\n')

arr=np.eye(4)   #for identity matrix
print(arr,'\n')

print(np.arange(2,20,3),'\n')    #last bound not included || (start,end,step)

arre= random.randint(1,7,1)   # (start,end,shape)
print(arre,'\n')

arro=random.randint(1,7,[3,3])
print(arro,'\n')

arrh=random.choice(a=[1,2,3,4,5,6,7,8,9,10],size=10)
print(arrh)

arrh=random.choice(a=['a','b','c','d'],size=3)
print(arrh)

arr1=[1,2,3,4]
arr2=[5,6,7,8]
print('sum of array=',arr1+arr2)
'''

#_____________________________________________________
#matplot lib operations:
#_____________________________________________________

'''
#simulate the motion of a projectile under influence of gravity(by using matplotlib)

# Parameters
v0 = 50          # initial velocity (m/s)
angle = 45       # launch angle (degrees)
g = 9.81         # gravity (m/s^2)

# Convert angle to radians
theta = np.radians(angle)

# Time of flight
t_flight = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, t_flight, num=500)

# Trajectory equations
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.axis("equal")
plt.show()

# extra graphs
plt.plot([1,2,3],[1,4,9])
plt.show()

plt.plot(x,x**2)
plt.show()

x=[1,2,3,4]
y=[4,3,2,1]

plt.plot(x,y)
plt.grid(True)
plt.show()

#bar graph plot
x=[1,2,3,4,5]
y1=[20,40,50,10,90]
y2=[40,60,48,60,20]
y3=[100,150,200,0,0]
plt.figure(figsize=(10,5))

plt.plot(x,y1,color='b',marker='o',lw=2,label='line 1')
plt.plot(x,y2,color='r',marker='o',lw=2,label='line 2')
plt.plot(x,y3,color='g',marker='o',lw=2,label='line 3')

plt.xticks(np.arange(1,6,step=1))
plt.yticks(np.arange(0,210,step=20))
plt.legend()
plt.grid()
plt.show()

x=[1,2,3,4,5]
y1=[20,40,50,10,90]
y2=[40,60,48,60,20]
y3=[100,150,200,0,0]
plt.figure(figsize=(10,5))
bar_width=0.8
plt.bar(x,y1,color='b',lw=2,label='bar 1')
plt.bar(x,y2,color='r',lw=2,label='bar 2')
plt.bar(x,y3,color='g',lw=2,label='bar 3')

plt.xticks(np.arange(1,6,step=1))
plt.yticks(np.arange(0,210,step=20))
plt.legend()
plt.show()

#for prediction analysis
x=[1,2,3,4,5]
y1=[20,40,50,10,90]
y2=[40,60,48,60,20]
y3=[100,150,200,0,0]
plt.figure(figsize=(10,5))
bar_width=0.8
plt.scatter(x,y1,color='b',lw=2,label='shape 1')
plt.scatter(x,y2,color='r',lw=2,label='shape 2')
plt.scatter(x,y3,color='g',lw=2,label='shape 3')

plt.xticks(np.arange(1,6,step=1))
plt.yticks(np.arange(0,210,step=20))
plt.legend()
plt.show()

slices=[3,5,7,11]
label=['iphone','android','airpods','laptop']
cols=['b','c','r','pink']

plt.pie(slices,labels=label,colors=cols,autopct='%1.0f%%',shadow=True)
plt.title('Pie chart')
plt.show()

slices=[3,5,7,11]
label=['iphone','android','airpods','laptop']
cols=['b','c','r','pink']

plt.pie(slices,labels=label,colors=cols,explode=(0.3,0,0.3,0),autopct='%1.0f%%',shadow=True)
plt.title('Pie chart')
plt.show()

# 3-D graphs ploting
Any=plt.figure(figsize=(10,2))
Any.add_subplot(projection='3d')

x=[1,2,3,4,5]

y1=[20,40,30,10,60]
y2=[10,200,40,50,20]
y3=[30,60,20,40,10]
y4=[40,50,10,60,70]

plt.plot(x,y1,color='b',marker='o',lw=2,label='1st')
plt.plot(x,y2,color='g',marker='o',lw=2,label='2nd')
plt.plot(x,y3,color='r',marker='o',lw=2,label='3rd')
plt.plot(x,y4,color='k',marker='o',lw=2,label='4th')

plt.title('3d graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xticks(np.arange(1,6,step=1))
plt.yticks(np.arange(0,210,step=50))

plt.legend()
plt.grid()
plt.show()

# unique styled 3d plotted graph
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()

# PIE chart -> plt.pie(x,labels=y,explode=z)
x=[0.1,0.2,0.3,0.4]
y=['label1','label2','label3','label4']
z=[1,0,0,0]

plt.pie(x,labels=y,explode=z)

plt.show()
'''

#_____________________________________________________
# pandas library operations:
#_____________________________________________________

'''
lst=[2,3,4,5,5,67,7]

print(lst)

ser=pd.Series(lst,name='marks')
ser1=pd.Series(lst,index=['a','b','c','d','e','f','g'])

print(ser)
print(ser1)
print(type(lst))
print(type(ser))

list_any=[['[name]','[5]','[My]'],['[a]','[l]','[p]'],[[1],[2],[3]]]
ser2=pd.Series(list_any,name='series',index=['(a)|','(b)|','(c)|'])
print(ser2)
print(type(list_any),list_any[1][2])

df=pd.DataFrame(list_any,columns=['|column1|','|column2|','|column3|'],index=['(a)|','(b)|','(c)|'])
print('\n',df,type(df))

d={'A':1,'B':2,'C':3}

df=pd.DataFrame(d,index=['(a)|','(b)|','(c)|'])
print(df,type(df))

d={'Fruit':['M','D','B','G'],
   'indexvalue':[0,1,2,3],
   'like/dislike':['L','D','D','l']}

df=pd.DataFrame(d)
print(df,type(df))

data = pd.DataFrame({'A':[1,2,3,4,5],'B':[1,3,5,7,9]})
print(data)

data['C']=data['A']+data['B']
data['D']=data['B']-data['A']
data.insert(1,'Alphabets',['a','b','c','d','e'])
print(data)
del data['Alphabets']
print(data)

df = pd.read_csv('C:/Users/vkape/OneDrive/Desktop/coding basics/python basics/dataset.csv')   #loading data 

print(df)                                      # can use to_string for large dataset

# selection in dataset
print(df["name"])                         # selecting by column
print(df.loc[1])                               # selecting by rows
print(df.iloc[1:3])                            # selecting rows [initial:final:step,initial:final:step] , [rows,columns]

df = pd.read_csv("C:/Users/vkape/OneDrive/Desktop/coding basics/python basics/dataset.csv",index_col="Name")    

#selecting specific element by entering details of a column
Name= input("Enter name:")

try:
    print(df.loc[Name])
except KeyError:
    print(f"{Name} not found")

# filtering in dataset

filtered= df[df["id"]>=500]       # df["column"] conditions
print(filtered)

# aggregate functions (summarize and analyse data)

print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

#single column selection
print(f'Average age of employee = {df["Age"].mean()}')

grp = df.groupby("id")
print(grp["Age"].mean())

# Data cleaning

df = df.drop(columns=["Age","id"])             #to remove columns
df = df.dropna(subset=["Description"])         # to clean those elements which do not have a specific subset(to clean NAN values from the dataset)
df = df.fillna({"Description":"None"})         # places where NAN data was coming filled with None keyword(remove empty spaces)
df["Active"] = df["Active"].replace({"True":"T","False":"F"})   # Raplacing some words {"Initial":"Final"}
print(df.to_string)
print(df["Name"].str.lower())                  # .str.upper()  -> extras

# Fix datatypes (datatypes conversion for better representation)
df["Active"] = df["Active"].astype(int)

df = df.drop_duplicates()
'''

#_____________________________________________________
# Scikit learn:
#_____________________________________________________

'''
# illustration of a basic example

data = load_breast_cancer(as_frame=True).frame
print(data)

X,y= load_breast_cancer(return_X_y=True)  # having multiple variables
print(X)                             # values
print(y)                             # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()              # scaler variable for scaling the data

X_train_scaled = scaler.fit_transform(X_train)  # scaler function used
X_test_scaled = scaler.fit_transform(X_test)

knn  = KNeighborsClassifier()            # algorithm applied by function of algorithm
knn.fit(X_train_scaled, y_train)         # fitted data as per k spaces
print(knn.score(X_test_scaled, y_test))  # mean accuracy of the algorithm 

df = load_breast_cancer(as_frame = True).frame
df.hist()
plt.tight_layout()
plt.show()         # for histogram plotting

df.info()          # to know datatype of the data in any column

# Blobs making (Clustering data)
X, y = make_blobs(n_samples = 5000, centers=5)    # making 5000 entries as 5 blobs(clusters)

plt.scatter(X[:,0],X[:,1],c=y)
plt.xticks(np.arange(-15,10,5))
plt.yticks(np.arange(-15,15,5))
plt.legend()
plt.grid()
plt.show()

# Moons structure
X,y = make_moons(noise=0)   # random_state = 0 -> means same sataset plot is obtained every time (pass it as an argument)

plt.scatter(X[:,0],X[:,1],c=y)
plt.show()

# Splitting datasets

X, y = load_iris(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)   # 20% testing , 80% training

counts = np.bincount(y_train)
positions = np.arange(3)

plt.bar(positions, counts)          # produces variable graphs after running code
plt.show()

# For same splitted data everytime
from sklearn.model_selection import StratifiedShuffleSplit as sts

split = sts(n_splits = 1, test_size = 0.2)

for train_idx, test_idx in split.split(X,y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

plt.bar(positions, counts)
plt.show()                      # remains same for every running 

X, y = load_iris(return_X_y=True)  # -> raw data processed
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

scaler = StandardScaler()          # -> Scaler variable declared (Min max scaler also exists)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# Encoding datasets (one hot encoder also exists -> various different types)
 
data = fetch_openml('car', as_frame=True ).frame  # Internet must be connected to use

columns_to_encode = ['lug_boot','safety']

encoder = OrdinalEncoder(
    categories = [
        ['small','med','big'],
        ['low','med','high'],
    ]
)

data[columns_to_encode] = encoder.fit_transform(data[columns_to_encode])     # -> converts low to 0, med 1, high to 2

data[columns_to_encode] = encoder.inverse_transform(data[columns_to_encode])  # -> reverse the current operation

# Classification of data by various algorithms

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)  
X_test_scaled = scaler.fit_transform(X_test)

clf = knn()
clf.fit(X_train_scaled, y_train)
clf.score(X_test_scaled, y_test)

single_instance= X_test_scaled[0]      # variable used to see model performance

prd1 = clf.predict([single_instance])
prd2 = clf.predict_proba([single_instance])
print(prd1, y_test[0])                  # gives 1 output for correct data
print(prd2)                             # 2-dimensional answers

# Regression models used : 

reg = LinearRegression()

reg.fit(X_train_scaled, y_train)         
sc = reg.score(X_test_scaled, y_test)    # Returns R**2 score
print(sc)

single_instance = X_test_scaled[0]

pr3 = reg.predict([single_instance])
print(pr3)

# Multidimensional Clustering

x, _ = make_blobs(n_samples=5000, centers = 5, random_state=10)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

km = KMeans(n_clusters=5)
km.fit(x_scaled)

plt.scatter(x_scaled[:,0], x_scaled[:,1],c=km.labels_)
plt.show()

x, _ = make_moons(n_samples=5000, random_state=10, noise=0.08)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

km = KMeans(n_clusters=5)
km.fit(x_scaled)

plt.scatter(x_scaled[:,0], x_scaled[:,1],c=km.labels_)
plt.show()

# PCA logic

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pca = PCA(n_components=2)          # Reduces data components into smaller n parts

X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

clf = LogisticRegression(max_iter=100)
clf.fit(X_train_reduced, y_train)

print(clf.score(X_test_reduced, y_test))      # Accuracy

num = np.sum(pca.explained_variance_ratio_)   # Variance ratio sums
print(num)                  

# Matrics

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  
X_test_scaled = scaler.fit_transform(X_test)

clf = LogisticRegression(max_iter=100)
clf.fit(X_train_scaled, y_train)
clf.score(X_test_scaled, y_test)

y_pred = clf.predict(X_test_scaled)
print(accuracy_score(y_test, y_pred))   # any_score(y_test, y_pred) -> to know any type of score of the model on the data

reg = LinearRegression()
y_pred = reg.predict(X_test_scaled)
print(r2_score(y_test, y_pred))         # other types of error scores

# Cross Validation 

X,y = load_breast_cancer(return_X_y=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

clf = knn()
scores = cross_val_score(clf, X_scaled, y, cv=5 ,scoring='precision')
print(np.mean(scores))

# Hyper parameter tuning with grid search

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
param_grid = {
    'n_estimators': [50,100,200],
    'max_depth': [None, 5, 10],
    'min_samples_split':[2,5],
}

clf = RandomForestClassifier(n_jobs=-1)

grid = GridSearchCV(clf, param_grid, cv=3)
grid.fit(X_train, y_train)
grid.best_params_
{'max_depth':None, 'min_samples_split':2, 'n_estimators':100}
best_clf = grid.best_estimator_
print(best_clf.score(X_test, y_test))

# Pipelining

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

pipe = Pipeline([                                                   # Using scaling, component breaking and classifier at once
    ('scale', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('forest', RandomForestClassifier())
])

pipe.fit(X_train, y_train)                                          # Dataset is fitted inside this pipeline variable

print(pipe.score(X_test, y_test))       
'''

#_____________________________________________________
# Tensorflow :
#_____________________________________________________

'''
mnist = tf.keras.datasets.mnist         # loading dataset

(x_train, y_train), (x_test, y_test) = mnist.load_data()            # data already scaled and splitted

model = Sequential()            # linear stack of layer
model.add(Input((28,28)))
model.add(Flatten())            # Layer mechanism 
model.add(Dense(128, activation='relu'))          # hyper parameter required
model.add(Dropout(0.2))         # chances of not a connection
model.add(Dense(10))            # outut layer -> final

pred = model(x_train[:1]).numpy()       # random prediction
print(pred)

s = tf.nn.softmax(pred).numpy().sum()         # function for only +ve number 
# print(s)

loss_fn = SparseCategoricalCrossentropy(from_logits=True)           # losses function created

# -tf.math.log(1/10)     other method
loss_fn (y_train[:1] , pred)        # major method for loss calculation

optimizer = Adam(learning_rate = 0.01)
model.compile(optimizer=optimizer, loss=loss_fn, metrics=['accuracy'])                  # improving accuracy of the model
model.fit(x_train, y_train, epochs=10)

model.evaluate(x_test, y_test)              # final evaluation
'''
