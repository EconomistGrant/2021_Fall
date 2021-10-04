# Embedding
Target: word embedding, V*N matrix (len of voc * dimension)
method: Continuous Bag of Words & Skip-Gram, a hidden layer in the middle
problem: embedding matrix too large -> 
1. hierachical softmax, tree instead of one-hot, O(logV)
2. Negative sampling: prediction from correct label + some random chosen noise
