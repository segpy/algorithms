def bubble_sort(user_list):
    """_summary_

    :param num_list: _description_
    :return: _description_
    """
    print(len(user_list))
    for i in range(len(user_list)):
        print(f'Iteracion {i} - {user_list}')
        swap = False
        for j in range(len(user_list)-i-1):
            print(f'J {j} - {user_list}')
            if user_list[j] > user_list[j+1]:
                user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
                swap = True
        if not swap:
            break
    return user_list


def selection_sort(user_list):
    for i in range(len(user_list)):
        min_index = i
        for j in range(i+1, len(user_list)):
            print(f'{i} - {j}')
            if user_list[j] < user_list[min_index]:
                min_index = j
        user_list[i], user_list[min_index] = user_list[min_index], user_list[i]
    return user_list


def insertion_sort(user_list):
    for i in range(1, len(user_list)):
        key = user_list[i]
        j = i - 1
        while j >= 0 and key < user_list[j]:
            user_list[j+1] = user_list[j]
            j -= 1
        user_list[j+1] = key
    return user_list


def merge_sort(user_list):
    print(f'List {user_list}')
    if len(user_list) <= 1:
        print(f'Base condition reached with {user_list}')
        return user_list
    mid = len(user_list) // 2
    left = merge_sort(user_list[:mid])
    right = merge_sort(user_list[mid:])
    # return f'L:{left} - R:{right}'
    print(f'Merging {left} and {right} - {merge(left, right)}')
    return merge(left, right)


def merge(left, right):
    i = j = 0
    output = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            output.append(right[j])
            j += 1
        else:
            output.append(left[i])
            i += 1
    output += left[i:] + right[j:]
    return output


def main():
    # print(selection_sort([1, 5, 16, 6]))
    # print(merge([1, 5, 6, 8], [2, 3, 4, 7]))
    print(merge_sort([1, 5, 16, 6, 2, 3, 4, 7]))


if __name__ == "__main__":
    main()
