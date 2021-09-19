# Text Classification
Spam Classification
language identifation: which language?

# Problem
Input: document x = [x1, x2, ...]
output y in {1,2,3,...,k}

identify priori that makes words informative

# Learning-based classification
inputs, labels, and predictions
where do datasets come from?
human institutions, noisy labels, expert annoation, crowd workers

# log-linear models
p(y|x) linear to exp(w_y^T x)
log p(y|x) = w_y^T * x - log sum exp (wy^T x)
log p(*|x) = logsoftmax(W^T x)


