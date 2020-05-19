# Longest sublist

The function *identifySublist* in list_analysis.py returns find the longest sublist, which contains the same amount of chars and digit.

The function expects to get a list, which only contains chars or numbers. 
For example: **[0, 'a', 'c', 4, 1, 2, 'b', 0, 2, 3]**
It returns with the first and last index of the found sublist: **(1,6)**

The given algorithm complexity is 

![equation](https://latex.codecogs.com/png.latex?O%5Cleft%20%28%5Cfrac%7B%5Cleft%20%28%20n%20-%20%5Cfrac%7Bk%7D%7B2%7D%20%5Cright%20%29%20*%20%5Cleft%20%28%5Cleft%20%28n%20-%20%5Cfrac%7Bk%7D%7B2%7D%29%20&plus;%201%5Cright%20%29%5Cright%20%29%7D%7B2%7D%5Cright%20%29)

which is the sum of first  ![equation](https://latex.codecogs.com/gif.latex?%5Cleft%20%28%20n%20-%20%5Cfrac%7Bk%7D%7B2%7D%20%5Cright%20%29) number, where ![equation](https://latex.codecogs.com/gif.latex?k) is the length of the found longest sublist, and ![equation](https://latex.codecogs.com/gif.latex?n) is the number of elements in the list.
The complexity is computed based on the number of times that two elements of the list are being "compared".

In exchange for using more memory and performing less execution on deciding whether an element of a given list is a number or string, the algorithms create a helper list which contains these data. This helper list is used during the search of the longest substring.
