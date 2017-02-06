# allcombinations

##Motivation
- You have lists A, B, C, D... and would like to calculate all combinations [a, b, c, d...] such that a is in A, b is in B etc.

- allcombinations takes as input a csv/txt file, where each line represents an input list and returns a generator object which produces each combinations. 

##General comments

- No limits on number of lists or size of the lists

- Storing the combinations as a generator results in lower storage requirements than if all combinations are stored (same as xrange vs range in Python 2.x)

##Example

Input file 'example.csv':
```
3,4,6
7,8
9,10,1
```

Code:
```python
from allcombinations import allcombinations as ac

for i in ac.allcombinations('example.csv'):
    print(i)
```

Returns:
```python
[3, 7, 9]
[4, 7, 9]
[6, 7, 9]
[3, 8, 9]
[4, 8, 9]
[6, 8, 9]
[3, 7, 10]
[4, 7, 10]
[6, 7, 10]
[3, 8, 10]
[4, 8, 10]
[6, 8, 10]
[3, 7, 1]
[4, 7, 1]
[6, 7, 1]
[3, 8, 1]
[4, 8, 1]
[6, 8, 1]
```