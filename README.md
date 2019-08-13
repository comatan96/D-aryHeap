# D-aryHeap
D-ary heap for 20407 course

Clone to your machine, import `DHeap` from dheap.

Create instances by calling init:

  ```python
  dheap = DHeap(list, d)
  ```

*Create instances by using .txt file:*

Use the static method `build_with_file()`.

Usage:
  ```python
  DHeap.build_with_file(str)  # str is path to file
  ```

format the file:

`list saperated with commas _ d`

E.g.
`1,2,3,4,5,6,7,8,9 3`
 **Multi line is available**
  
Use `extract max`, `increase key`, `insert`:

  ```python
  dheap.dheap_extract_max()
  ```
  
  ```python
  dheap.dheap_increase_key(x)  # x is integer
  ```
  
  ```python
  dheap.dheap_insert(x)  # x is integer
  ```
  
  **PDF sent by mail.**
