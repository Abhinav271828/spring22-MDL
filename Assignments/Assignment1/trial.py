import pickle
import random
import matplotlib.pyplot as plt
from numpy import array, array_split, var, subtract, mean, square
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model  import LinearRegression

trainset = pickle.load(open("data/train.pkl", "rb"))
random.shuffle(trainset)
trainsetSplit = array_split(trainset, 16)
xSplit = array([[ [point[0]] for point in data]
                    for data in trainsetSplit])
ySplit = array([[ [point[1]] for point in data]
                    for data in trainsetSplit])
testset = pickle.load(open("data/test.pkl", "rb"))
xTest = array([ [point[0]] for point in testset])
yTest = array([ [point[1]] for point in testset])

def bias(predicted, required):
  bias = mean(subtract(predicted, required))
  return bias

f = open("biasvar.csv", 'w')
f.write("Degree,Trainset,Bias,Variance,Irreducible\n")

biasList = []
biasOrd = []
variance = []
mse = []
irred = []

biasMod = []
varMod = []
mseMod = []
irredMod = []
# Linear Regression
for i in range(16):
  lreg = LinearRegression().fit(xSplit[i], ySplit[i])
  predicted = lreg.predict(xTest)
  b = bias(predicted, yTest)
  biasMod.append(b)
  v = var(predicted)
  varMod.append(v)
  err = mean(square(subtract(yTest, predicted)))
  mseMod.append(err)
  s = err - (b**2 + v)
  irredMod.append(s)
  f.write("1,{i},{b},{v},{s}\n".format(i=i,b=b,v=v,s=s))
biasList.append(mean(square(biasMod)))
biasOrd.append(mean(biasMod))
variance.append(mean(varMod))
mse.append(mean(mseMod))
irred.append(mean(irredMod))

# Polynomial Regression
lr = LinearRegression()
for d in range(2,16):
  biasMod = []
  varMod = []
  mseMod = []
  irredMod = []
  for i in range(16):
    poly = PolynomialFeatures(degree=d)
    poly_x = poly.fit_transform(xSplit[i])
    test_x = poly.fit_transform(xTest)

    lr.fit(poly_x, ySplit[i])
    predicted = lr.predict(test_x)

    b = bias(predicted, yTest)
    biasMod.append(b)
    v = var(predicted)
    varMod.append(v)
    err = mean(square(subtract(yTest, predicted)))
    mseMod.append(err)
    s = err - (b**2 + v)
    irredMod.append(s)
    f.write("{d},{i},{b},{v},{s}\n".format(d=d,i=i,b=b,v=v,s=s))
  
  biasList.append(mean(square(biasMod)))
  biasOrd.append(mean(biasMod))
  variance.append(mean(varMod))
  mse.append(mean(mseMod))
  irred.append(mean(irredMod))

f.close()

f = open("averages.csv", 'w')
f.write("Degree,AvgBias,AvgVar,AvgIrred,AvgMSE\n")
for d in range(15):
  f.write("{d},{b},{v},{s},{m}\n".format(d=d+1,
                                         b=biasOrd[d],
                                         v=variance[d],
                                         s=irred[d],
                                         m=mse[d]))
f.close()

def rescale(l):
  amin = min(l)
  amax = max(l)
  return list(map(lambda x: (x-amin)/(amax-amin),
                      l))

biasList = rescale(biasList)
variance = rescale(variance)
mse = rescale(mse)

plt.plot(range(1,16), biasList, color='g', label='bias^2')
plt.plot(range(1,16), variance, color='r', label='variance')
plt.plot(range(1,16), mse, color='b', label='total error')
plt.legend()
plt.show()
