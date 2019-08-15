import math
''' mmn 13 2020a Ds & Algo '''
''' Matan Cohen , ID: 205907371 '''
''' d-Heap implementation '''


class DHeap:
    ''' creates d-heap
        heap: A python's list
        inp: inpus source as str, will include path to .txt file
        txt file should contain a list and d '''

    def __init__(self, heap: list, d: int=None):
        if type(heap) is list:
            self.__heap = heap
        else:
            raise TypeError("Argument heap is not a list!")
        if not d:
            try:
                self.__d = int(input('Please insert d: '))
            except ValueError:
                print("Not a valid integer")
        else:
            if type(d) is int:
                self.__d = d
            else:
                raise TypeError("Given d is not an integer!")
        if self.__d < 2:
            raise ValueError("d must be greater than 2!")
        self.build_d_heap(self.d)

    ''' Build d-heaps using a file, a static method
        the building is iterating through every line in the file
        picks a list and an integer and append it as a tuple in the
        return list.
        .txt file should look like given example.txt
        and should be formated like:
        [list of integers in order to create a d heap from them] d
        space is required between list and d.
        commas only  between integers in list, NO SPACES! '''
    @staticmethod
    def build_with_file(path: str) -> list:
        def use_file(path: str) -> list:
            dheap_list = []
            with open(path) as f:
                for line in f:
                    try:
                        line = line.split(' ')
                        nums = line[0].split(',')
                        d = int(line[1])
                        h = [int(x) for x in nums]
                        dheap_list.append((h, d))
                    except ValueError:
                        print(f'Sorry, wrong input in: {line}, Please check input.')
            return dheap_list

        returnvalue = []
        for heap in use_file(path):
            returnvalue.append(DHeap(heap[0], heap[1]))
        return returnvalue

    @property
    def d(self):
        return self.__d

    def __len__(self):
        return len(self.__heap)

    def __str__(self):
        return str(self.__heap)

    ''' return the kth child of index i
        k >= 0 and k <= d-1
        child function as described on the paper (PDF)
        Constant time Complexity '''
    def _child(self, k: int, i: int) -> int:
        return self.d*i+1+k

    def _parent(self, i: int) -> int:
        return math.ceil(i/self.d)-1

    def build_d_heap(self, d):
        ''' i is exactly as the regular binary heap 
            this time instaed of using LENGTH/2 I used LENGHT/d 
            // is floor division in Python '''
        i = (len(self)-1)//d
        for i in range(i, -1, -1):  # O(n/d)
            self.dheap_max_heapify(i)

    ''' The implementation of dheap_max_heapify is pretty
        similar to the original heapify implementation.
        the main changes are the choosing of the largest number of each
        "subtree" in order to make changes!
        The Time Complexity of this heapify is: O(d log d (n)). '''
    def dheap_max_heapify(self, i: int):
        largest = i  # O(1)
        for k in range(0, self.d):  # O(d)
            # O(1)
            if self._child(k, i) < len(self) and self.__heap[self._child(k, i)] > self.__heap[i]:
                if self.__heap[self._child(k, i)] > self.__heap[largest]:  # O(1)
                    largest = self._child(k, i)  # O(1)

        if largest != i:  # O(1)
            # O(1) - swapping
            self.__heap[i], self.__heap[largest] = self.__heap[largest], self.__heap[i]
            ''' This recursive call is happening at most Tree-Height times '''
            ''' A proof for Tree-Heigh on the paper (PDF) '''
            self.dheap_max_heapify(largest)

    ''' The implementation of d-ary heap_extract max as shown,
        in order to make the implementation work I had to implement
        the d-ary max_heapify.
        My implementation for dheap_extract_max is using constant time
        operations alongside the dheap_max_heapify method which the time
        complexity of this method is described just before it's implementation.
        TOTAL TIME: O(d log d (n)). '''
    def dheap_extract_max(self):
        if len(self) < 1:
            raise AttributeError("Heap is Empty")
        returnvalue = self.__heap[0]
        self.__heap[0] = self.__heap.pop()
        self.dheap_max_heapify(0)
        return returnvalue

    def dheap_insert(self, key: int):
        ''' check if key is valid '''
        if type(key) is int:  # O(1)
            self.__heap.append(key)  # O(1) - adding key to the end of heap.
            i = len(self)-1  # O(1)
            self.dheap_upwords_heapify(i)  # fixing the heap.

    def dheap_increase_key(self, i: int, key: int):
        ''' check for error chances '''
        if i < 0 or i >= len(self):
            raise IndexError("Index out of range")
        if type(key) is not int or key < self.__heap[i]:
            raise ValueError("Error, Invalid key")
        self.__heap[i] = key  # set heap[i] as new key
        ''' call method to fix heap '''
        self.dheap_upwords_heapify(i)

    ''' dheap_upwords_heapify created in order to keep my code clean.
        While creating insert and increase-key I had to use the same
        methods in order to "fix" the d-ary heap and in order not to
        duplicate my code I made a new method.
        This method takes i (index) and fixing the d-ary heap
        from this i and upwords (unlike heapify who goes downwords).
        Time complexity: O(log d (n)) bounded by the tree-height. '''
    def dheap_upwords_heapify(self, i: int):
        # O(log d (n))
        while i > 0 and self.__heap[self._parent(i)] < self.__heap[i]:
            self.__heap[i], self.__heap[self._parent(i)] = self.__heap[self._parent(i)], self.__heap[i]
            i = self._parent(i)
