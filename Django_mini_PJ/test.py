from random import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import random
# 接收POST请求数据

x=np.linspace(1,50,2)
f=np.poly1d([1,5,10])
y=f(x)
for i in range(len(y)):
    y[i]=y[i]+random.random()*100
    print(y[i])

x=np.reshape(x,(-1,1))

#SKLEARN

poly_reg=PolynomialFeatures(degree=2)
X_ploy=poly_reg.fit_transform(x)
lin_reg=LinearRegression()

lin_reg.fit(X_ploy,y)

X_new=poly_reg.fit_transform([[51]])
y_pred=lin_reg.predict(X_new)

plt.plot(x,y,c="red")
# plt.plot(x,y_pred,c='blue')
plt.scatter(51,y_pred)
plt.show()