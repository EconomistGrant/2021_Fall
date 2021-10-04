# Bubble sort
function bubble_sort (array, length) {
    var i, j;
    for(i from 0 to length-1){
        for(j from 0 to length-1-i){
            if (array[j] > array[j+1])
                swap(array[j], array[j+1])
        }
    }
}

every iteration fix the position of one element
# Merge sort
O(nlogn)
sort left and right seperately, and then merge
merge sorted arrays: O(n),single pass
# Counting / Radix Sort
n numbers, base k, d digits => O((n+k)d)

# Insertion sort
O(n^2)
when new comes, swap until it is in the right place (in-place)

# Quick sort
1. randomly pick pivot
2. put smaller elements left to pivot, and greater elements right to pivot
3. sort left and right subarray
```c++
 void quicksort(vector<int> &v, int start, int end){
     if (end - start <= 1){
         return;
     }
     int picked = rand()%(end-start+1)+start;
     int pivot = v[picked];
     swap(v[picked],v[start]);

     int index = start;
     for (int i = start+1;i <= end; i++){
         if (v[i] <= pivot){
             swap(v[index+1],v[i]); //smaller element "stack' from start to index
             index++;
         }
     }
     swap(v[start],v[index]);
     quicksort(v,start, index - 1);
     quicksort(v,index+1, end);
     }
```
# Heap sort
Build heap in O(n), and then pop element one by one
level k: O(k), sum k up