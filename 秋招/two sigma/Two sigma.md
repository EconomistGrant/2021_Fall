# Stat/Prob
multivariate normal
OLS y~x, x~y
multicolinearity (PCA???)
linear regression assumptions

第一题：问两个correlated Gaussian，当给定其中Gaussian的一个值的时候，另外一个Gaussian的prediction还有error。
第二题：给定Gaussian的covariance matrix，问怎么从这个Gaussian里面sample。

# Math
combine 10 strategy, collectve sharpe ratio
covariance matrix + estimation method 

# Code/algo

reverse list

interval merge
treemap vs hashmap

hash table load factor

thread vs process 
- 线程 进程 process = environment to execute a program, including lots of threads; thread = subset of process, share resources of a process that it belong 

python 里面 set可以存哪些object
- must be hashable (immutable during its lifetime)

__new__ 和 __init__ 的区别
-https://zhuanlan.zhihu.com/p/111728199

random number generator

## LC
### LC564 closest palindrome
### 1048 Longest String Chain
### 547 #provinces DFS 并查集
### 528 random integer with weights
presum; x = random.randint(1, self.total); return bisect_left(self.pre, x)
lower_bound(pre.begin(), pre.end(), x) - pre.begin(); #找到第一个》=target的元素的位置

实现bisect left:
l = 0, r = n-1
while (r - l >1):
    mid = (l+r)/2
    if arr[mid] >= target:
        r = mid
    else:
        l = mid

### 随机数生成 不可放回(without replacement)
srand((unsigned)(time(NULL)));random_shuffle(myints.begin(),myints.end());
random.shuffle(arr);


# 710 random integer with blacklist: 
N = B + W, for i < W that is blacked, map to [W, N]

# 146 LRU 
https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/ python和c++都看看
生成一个DLinkedNode的class

981 Time-based key-value storage hash 到一个 vector 然后二分法查找 最大的不超过查找值的  

43 multiply strings

415 add string 

4 median of two sorted array hard

289 board of life

443 string compression

689 Maximum Sum of 3 Non-Overlapping Subarray   an array to store subarray sum, prefix, postfix

207 Course schedule, topo

123 dp

850 太难了 有空再看 一定看

835 image overlap

1779 
606
886

三角形里随机产生点： 直角三角形，xy方向随机点，映射保证在三角形内。投射回原三角形。

# Case
NYC taxi driver
Bike case
twittwer news predicting stock returns

