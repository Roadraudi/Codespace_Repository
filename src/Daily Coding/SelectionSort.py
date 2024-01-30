def selectionSort(this_list):
    a = 0
    minimum = 0
    for i in range(len(this_list)-1):
        minimum = this_list[0]
        j = 1
        for j in range(len(this_list)):
            if this_list[j] < minimum:
                a = minimum
                minimum = this_list[j]


num_list = [2, 5, 1,7,9,6,27,19]
selectionSort(num_list)