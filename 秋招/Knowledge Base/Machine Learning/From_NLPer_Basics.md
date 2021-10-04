# 1. Logistic Regression
Binary Classfication 
$$h_\theta(x) = sigmoid(\theta^T X)  = \frac{1}{1 + e^{-\theta^T X}}$$

Gradient of sigmoid: f(1-f)
Target: cross entropy, gradient descent

## Discretization:
1. Non-linearity
2. Sparse matrix, quick multiplication
3. Cross-product of features
4. stability: for example, between age 20-30 (part of non-linearity?)
5. reduce overfitting 

# 2. Decision Tree
Feature Selection + Pruning
criterion: information gain, GINI index, cross entropy, CART
## Pruning: pre-prune and post prune
pre-prune: evaluate the regularized (penalized) gain when deciding branches
post-prune: bottom up evaluate every node (costly, but keeps more branches, and less likely to be underfit)

# 3. Perceptron
binary classification using linear boundary
loss function: distance of a mis-classified datapoint
gradient: x_i * y_i, w = w + \eta * gradient


# 4. Naive Bayes
all "features" are independent, i.e. P(X|y) = \pi P(x_i|y)

P(y|X) = P(X|y)*P(y) / P(X)
=> post = prior * \pi p(x_i|y) / p(x_i), both are accessible through training data

pros: performs well on low dimensional data
cons: strong independence assumption fails almost certainly; sensitive to data and extreme values?

# 5. Random Forest
## Bagging
select samples, build trees, aggregate
## Random Forest
select random features & random samples, aggregate (vote)
randomness: reduce overfit

# 6. Support Vector Machine
target: maxixum margin hyperplane
distance of a point to a plane:
$$\frac{|w^Tx + b|}{||w||} \\
||w|| = \sqrt{w_1^2 + ... + w_n^2}$$
support vector: closest point to the hyperplane

$$\begin{cases} \frac{w^Tx_i + b}{||w||} \geq d, & y_i = +1 \\ \frac{w^Tx_i + b}{||w||} \leq -d, & y_i = -1 \end{cases}$$

normalize: ||w||d = 1 => maximize d, minimize ||w||
$$min \quad \frac{1}{2} ||w||^2 \quad \\ st. y_i(w^Tx_i + b) \geq 1$$
lagrange dual, quadratic optimization with linear constraints
soft margin: hinge loss
multiple class: every class: yes or else, k classifiers, bias; C(k,2) calssifiers, vote
## Kernal Methods
not linear seperable: map to higher dimensions,$f(x) = w \phi (x) + b$
polinomial, sigmoid, Gaussian, Laplacian ...

# 7. K-means & KNN
## KNN
supervised learning, K nearest neighbors -> vote
small k: overfitting; large k: underfitting
## K means
unsupervised learning, clustering
initialize centoids -> find clusters -> new centroids -> iterate and stop criterion

sensitive to abnormal values / starting values /abnormal shapes
kmeans++: initialization, random first centroid, sampling weighted on the distance from the first centroid
## Spectual Clustering:
two circles having same centroid
https://zhuanlan.zhihu.com/p/84834952
https://en.wikipedia.org/wiki/Spectral_clustering


# Higher-level concepts
## Frequentist vs Bayesian
frequentist: theta is an unknown constant and X(data) is an RV, use MLE to estimate theta
Bayesian: theta is an RV, use MAP to estimate P(theta|X)

MLE  $L(\theta) = L(X_1, X_2, \cdots, X_n; \theta) = \prod_{i=1}^n p(X_i| \theta)$
MAP $P(\theta|X) = \frac{P(X | \theta) P(\theta)}{P(X)}= \frac{P(X | \theta) P(\theta)}{\int_{\theta} P(X|\theta)P(\theta)d{\theta}} \\$, maximize P(x|theta) P(theta)

MLE: pick the parameter to maximize the likelihood that your dataset occurs
MAP: pick the parameter that given prior and data, your posterior porb is maximized

do you believe the world has an ultimate constant or is changing?

## Generative vs Discriminative
generative: P(x,y)
discriminative: P(y|x)
#TODO
https://www.zhihu.com/question/20446337

## Hyperparameter
learning rate, kernal size, batch size (more accurate gradient every time vs. exploration & memory concern)
initialization: Xavier? avoid gradient vanish?
gradient descent: SGD(randomnized, avoid local maxima), standard (slow, memory? local maxima), mini-batch (art & science)
momentum, adam (considers 1st and 2nd gradients)
## Relu, tanh, sigmoid
relu pro: fast, sparse, dead cells cannot be updated
sigmoid / tanh: gradient vanish

# Case studies
evaluation criteria
bias vs variance
gradient explosion
curse of dimensionality
local minima
batch normalization
dropouts?
