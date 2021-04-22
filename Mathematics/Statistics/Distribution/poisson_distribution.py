# import matpotlib
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image



# https://data-flair.training/blogs/python-probability-distributions/
# 여기서 따라해봄

# Normal Distribution
import numpy as np
import scipy.stats

np.random.seed(1234)
samples = np.random.lognormal(mean=1., sigma=.4, size=10000)
shape, loc, scale = scipy.stats.lognorm.fit(samples, floc=0)
num_bins = 50
clr = "#EFEFEF"

counts, edges, patches = plt.hist(samples, bins=num_bins, color=clr)
centers = 0.5*(edges[:-1] + edges[1:])
cdf = scipy.stats.lognorm.cdf(edges, shape, loc=loc, scale=scale)
prob = np.diff(cdf)
plt.plot(centers, samples.size*prob, 'k-', linewidth=2)
# plt.show()
#
# s=np.random.poisson(5, 10000)
# plt.hist(s,16,normed=True, color='Green')

# Binomial
import seaborn as sns
from scipy.stats import binom
data = binom.rvs(n=17, p=0.7, loc=0, size=1010)
ax = sns.distplot(data,
                 kde=True,
                 color='pink',
                 hist_kws={"linewidth": 22, 'alpha':0.77})
ax.set(xlabel="Binomial", ylabel="Frequency")
# plt.show()


# Poisson Distribution
s = np.random.poisson(5, 10000)
# plt.hist(s, 16, normed=True, color="Green")
plt.hist(s,16, color='Green')
plt.show()