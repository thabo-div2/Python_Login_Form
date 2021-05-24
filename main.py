numbers = [42, 12, 13, 89, 63, 11]
z = [22, 93, 64, 55, 22, 2]

# Selection Sort


def selection_sort(num):
    # sort nums into ascending order

    n = len(num)

    # For each position in the list (except the very last)

    for a in range(n-1):
        # find the smallest item in the list

        x = a
        for i in range(a+1, n):
            if num[i] < num[x]:
                x = i
        num[a], num[x] = num[x], num[a]

    return num


print(selection_sort(numbers))
print(selection_sort(z))
