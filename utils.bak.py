from preprocessing import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

def plot_histogram(X, y, Xname, yname) :
    """
    Plots histogram of values in X grouped by y.

    Parameters
    --------------------
        X     -- numpy array of shape (n,), feature values
        y     -- numpy array of shape (n,), target classes
        Xname -- string, name of feature
        yname -- string, name of target
    """

    # set up data for plotting
    targets = sorted(set(y))
    data = []; labels = []
    for target in targets :
        features = [X[i] for i in xrange(len(y)) if y[i] == target]
        data.append(features)
        labels.append('%s = %s' % (yname, target))

    # set up histogram bins
    features = set(X)
    nfeatures = len(features)
    test_range = range(int(math.floor(min(features))), int(math.ceil(max(features)))+1)
    if nfeatures < 25 and sorted(features) == test_range:
        bins = test_range + [test_range[-1] + 1] # add last bin
        align = 'left'
    else :
        bins = 25
        align = 'mid'

    # plot
    plt.figure()
    n, bins, patches = plt.hist(data, bins=bins, align=align, alpha=0.5, label=labels, density = True)
    # n, bins, patches = plt.hist(data, density=True)
    plt.xlabel(Xname)
    plt.ylabel('Frequency')
    plt.legend()
    plt.legend(loc='upper left')
    plt.show()

X, y, Xnames = main()
n,d = X.shape

for i in xrange(0,26):
    plot_histogram(X[:,i], y, Xname=Xnames[i], yname='still_together')
