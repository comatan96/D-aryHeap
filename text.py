from dheap import DHeap

l = DHeap.build_with_file(path='example.txt')
for dh in l:
    print(dh)
    dh.dheap_insert(5)
    print(dh)
    dh.dheap_extract_max()
    print(dh)
    dh.dheap_increase_key(0, 500)
    print(dh)
