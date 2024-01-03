def two_sum(num_list, target_value):
    num_dict = {}
    for i in range(len(num_list)):
        num_dict[num_list[i]] = i
    for i in range(len(num_list)):
        if target_value - num_list[i] in num_dict:
            return [i, num_dict[target_value - num_list[i]]]


def binary_search(num_list, target_value):
    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == target_value:
            return mid
        elif num_list[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
    return -1
