# prob
unfair coin to make fair game, followup 如果p=0.99怎么优化
一个电梯里有十个人，一共有十层，每个人随机按一层（对于一个人，按到某一层的概率是0.1），问期望有多少层被按到过。
问n个人占n个座位，每个人进去了以后随机选座，但是不能选已经被占的座位的相邻座位，what's the expected number of occupied seats in the end。 DP, 再多记录sum
fair coin, 投n次, 求P(H个数为odd).  用归纳法得1‍‌‍‌‌‌‍‌‍‌‌‌‍‍‍‌‍‌‌‍/2
100扇门,每扇门后$1. 每次随机开一扇门, 第一次有钱拿. 再次打开就没钱了. 问随机开100次,期望收益


# Regression
stats 就是 linear regression assumption, F-test.
假设，如何处理高度共线性: Stepwise regression; PCA; Ridge regression
无偏性和t统计量
y对x1回归得系数beta, y对(x1,x2)回归得beta1, beta2. 如果beta2=0, 问beta1是否=beta?
- beta1,beta2 = argmin( y- beta1 x1 - beta2 x2)^2

# Linear Algebra & Math
eigenvalues property
asset x, 年化sharpe ratio为1, 问4年后 P(return<0)?  
Ans: y = x1+x2+x3+x4. 换算E(y) / std(y) = 2. 然后说chebshev不等式估p(y<0), 面试官说很impressive. 只要假设y是正态分布就够了.  

# Coding
LC, how to find stationary distribution given a matrix
LC 877 Stone Game, DP
max subarray 绿书P180
编程，给你几种硬币的面值，给定一个金额，求组成这个金额的最少硬币数。比如有2，3，5元硬币，组成10元至少要2枚 DP
LC121 Buy and Sell Stock
给一个全是正整数array 和k, 求其和严格小于k的subarray数目. 虽然知道要sliding-window, 但挣扎了半小时没能做出来. 最后在面试官提示下，连蒙带猜写了sliding window的移动方式，但没能写出代码.

编程，给一个string，找所有出现两次及以上的长度为8的子串 后缀/前缀数组？