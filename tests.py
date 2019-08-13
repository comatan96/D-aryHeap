from dheap import DHeap

# TESTS


def main():

    def trinary():
        pass

    ''' LIST CREATION '''

    # All test cases are trinary heap (3 ary heap)
    # Each case is a tuple with input and expected output
    # None
    none = (None, None)
    # Empty
    empty = ([], [])
    # Full
    full = ([1, 2, 3, 4, 5, 6], [6, 5, 3, 4, 1, 2])
    # Full with negative and equal numbers
    negatives_and_equals = ([-4, 2, -3, -10, 20, 32, -4],
                            [32, 20, -3, -10, -4, 2, -4])
    # Full with wrong types
    full_with_wrong_types = ([1, 3, 22, 'a', 'WRONG', []], None)
    # List of those cases
    test_cases = [none, empty, full,
                  full_with_wrong_types, negatives_and_equals]

    output = []  # Output list for heaps and next tests
    # Iterate over the list and check each case
    for i in range(len(test_cases)):
        print(f'------------- Creation test number: {i+1} -------------')
        # `test_cases[i][0]` is the input
        print(f'Testing heap construction as {test_cases[i][0]}')
        try:
            # Call __init__ with d=3
            heap = DHeap(test_cases[i][0], 3)
            print('Heap created succesffuly')
            # `test_cases[i][0]` is the expected output
            print(f'Excpected:\t {test_cases[i][1]}')
            # Printing heap as an array (python's list)
            print(f'Resault:\t {heap}')
            output.append(heap)
        # check for TypeError (Creation)
        except TypeError:
            print('Given arguemtns are wrong!')

    # Extract max test for each heap
    print('\nCheck heap extract max for each heap\n')
    expect = [None, 6, 32]
    for i in range(len(output)):
        output[i] = (output[i], expect[i])
    i = 1
    for h, m in output:
        print(f'------------- Extract max test number {i} -------------')
        try:
            print(f'Expected max:\t {m}')
            print(f'Real max:\t {h.dheap_extract_max()}')
        except AttributeError:
            print('Empty list:\t None')
        i += 1

    # Check if heap is fine
    print('\nCheck if heap is fine after extraction of max\n')
    expect = [[], [5, 2, 3, 4, 1], [20, 2, -3, -10, -4, -4]]
    for i in range(3):
        output[i] = (output[i][0], expect[i])
    for counter, h in enumerate(output):
        print(f'------------- Test heap number {counter+1} -------------')
        print(f'Expected heap:\t {h[1]}')
        print(f'Current heap:\t {h[0]}')

    # Reset output to lists only
    for i in range(len(output)):
        output[i] = output[i][0]

    print('\nInsert test\n')
    # Insert negative
    print('------------- Inserting negative number -------------')
    for h in output:
        h.dheap_insert(-8)

    expect = [[-8], [5, 2, 3, 4, 1, -8], [20, 2, -3, -10, -4, -4, -8]]
    for i in range(len(output)):
        print(f'Insertion test number {i+1}')
        print(f'Expected:\t {expect[i]}')
        print(f'Current:\t {output[i]}')

    # Insert Big
    print('------------- Inserting big number -------------')
    for h in output:
        h.dheap_insert(1000)

    expect = [[1000, -8], [1000, 5, 3, 4, 1, -8, 2],
              [1000, 2, 20, -10, -4, -4, -8, -3]]
    for i in range(len(output)):
        print(f'Insertion test number {i+1}')
        print(f'Expected:\t {expect[i]}')
        print(f'Current:\t {output[i]}')
    
    # Insert equals
    print('------------- Inserting equal number -------------')
    for h in output:
        h.dheap_insert(1000)
    # Insert non-int


if __name__ == '__main__':
    main()
