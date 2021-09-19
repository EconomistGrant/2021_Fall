min/max of subtree
              |build|insert|find max|
dynamic array | n   |  1   |  n     |
sorted D.A    |nlogn|  n   |  1     |
AVL Tree      |nlogn| logn | logn   |
Heap          |n    | logn | logn   |
# BST
binary search tree: left, right, parent, item
# AVL
balanced BST, rotation:
     D
   B   E
  A C 

     B
   A   D
      C E

# Augmentation
calculate "rank": size of subtree

# Heap
heapify: exchange with largest child, recurse
heap sort" call heapify from n/2 -> 1, O(n)

n/4 * (c) + n/8 * (2c) + n/16(3c) + ... 1(lgn - 1)c 
= cn (1/4 + 2/8 + 3/16 + 4/32 + ...) 
