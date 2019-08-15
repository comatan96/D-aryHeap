from dheap import DHeap


''' CONSTANTS '''
INSERTION_TEST      = {'BIG': 100, 'SMALL': -20, 'EQUAL': 12}
BUILD_PROMPT        = '----------- TESTING BUILD -----------'
INSERT_PROMPT       = '----------- TESTING INSERTION -----------'
EXTRACT_MAX_PROMPT  = '----------- TESTING EXTRACT MAX -----------'
INCREASE_KEY_PROMPT = '----------- TESTING INCREASE KEY -----------'

def prompt_generator():
    prompts = [BUILD_PROMPT, INSERT_PROMPT, EXTRACT_MAX_PROMPT, INCREASE_KEY_PROMPT]
    for p in prompts:
        yield print('\n' + p)

def test():
    # define prompt generator
    prompt = prompt_generator()

    # print prompt
    next(prompt)
    dheaps = []
    # test building
    for d in range(2, 11):
        dh = DHeap([-5, 20, 4, 12, 42, 20, -10, 76], d)
        print(f'd = {d}, heap is: \t{dh}')
        dheaps.append(dh)

    # print prompt
    next(prompt)
    # test insertion
    d_count = 2
    for dheap in dheaps:
        for value in INSERTION_TEST:
            dheap.dheap_insert(INSERTION_TEST.get(value))
        print(f'd = {d_count}, heap is: \t{dheap}')
        d_count += 1

    #print prompt
    next(prompt)
    # test extract max
    d_count = 2
    for dheap in dheaps:
        extracted_max = dheap.dheap_extract_max()
        print(f'Maximum is: {extracted_max}')
        print(f'd = {d_count}, Heap after extraction: \t{dheap}')
        d_count += 1

    # print prompt
    next(prompt)
    # test increase key
    d_count = 2
    print('Increasing key in the middle index to 77.')
    for dheap in dheaps:
        dheap.dheap_increase_key(len(dheap)-1, 77)
        print(f'd = {d_count}, Heap after increasing key: \t{dheap}')
        d_count += 1



if __name__ == '__main__':
    test()
