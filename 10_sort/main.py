# TODO здесь писать код

def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn + 1, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]

nums = [1, 4, -3, 0, 10]

selection_sort(nums)

print(nums)
