new_list = [4, 6, 8, 2, 9, 1]

def sort(this_list):
    for i in range(len(this_list)-1):
        for j in range(len(this_list)-1):
            small = this_list[j]
            if small > this_list[j+1]:
                small = this_list[j + 1]
                this_list[j+1] = this_list[i]
                this_list[i] = small
    print(this_list)

sort(new_list)