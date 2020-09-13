import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()

sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()

sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()

sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()

sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

