def mergeKLists(list_of_lists):
    #rtype : single list of all elements nk
    final_sorted = []
    lowest_val = 0
    low_val_index = 0
    for index, list in enumerate(list_of_lists):
        while list: #while not empty
            for ind in range(len(list_of_lists[index])):
                if list_of_lists[0][0] <= list_of_lists[ind][0]:
                    lowest_val = list_of_lists[0][0]
                    low_val_index = 0
                else:
                    lowest_val = list_of_lists[ind][0]
                    low_val_index = ind
        list_of_lists[low_val_index].remove(lowest_val)
        final_sorted.append(lowest_val)
    return final_sorted
		
