def unique_sorting(list_unsorted) -> list:
    '''
    finds the unique elements in a list and sorts them
    : param list_unsorted: a list of unsorted elements
    '''
    list_sorted = list_unsorted.unique()
    return list_sorted

list_unsorted = [1,4,5,7,2,4,90,7,8,4,5,3]
print(unique_sorting(list_unsorted))