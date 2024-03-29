""" Selection sort algorithm """
def selection_sort(lst):
    comp = 0
    swap = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            comp += 1
            if lst[j] < lst[min_index]:
                min_index = j
        # place smallest at the beginning (swap min index with i)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        swap += 1
    #return counts
    return comp, (swap * 3)