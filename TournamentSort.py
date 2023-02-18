def tournament(arr):
    def isAllNone():
        return (root is None) and (left is None) and (right is None)

    def isOnlyRootNone():
        return (root is None) and not(left is None) and not(right is None)

    def isOnlyLeftNone():
        return not(root is None) and (left is None) and not(right is None)

    def isOnlyRightNone():
        return not(root is None) and not(left is None) and (right is None)

    def isAllNotNone():
        return not(root is None) and not(left is None) and not(right is None)

    if len(arr) == 0:
        return[[], []]

    if len(arr) == 1:
        return[[arr[0]], []]

    if len(arr) == 2:
        return[[min(arr[0], arr[1]), max(arr[0], arr[1])], []]

    winners = []
    losers = []
    root = None
    left = arr[0]
    right = arr[1]
    arr_flag = 2

    while not isAllNone():

        if arr_flag > len(arr) - 1:

            minimum = min(left, right)
            maximum = max(left, right)

            left = None
            right = None

            if winners[-1] <= minimum:
                winners.append(minimum)
                winners.append(maximum)
            else:
                losers.append(minimum)
                if winners[-1] <= maximum:
                    winners.append(maximum)
                else:
                    losers.append(maximum)

        if isOnlyRootNone():
            if left >= right:
                root, right = right, root
            else:
                root, left = left, root

        if isOnlyLeftNone():
            left = arr[arr_flag]
            arr_flag += 1

            if left < root:
                left, root = root, left

        if isOnlyRightNone():
            right = arr[arr_flag]
            arr_flag += 1

            if right < root:
                right, root = root, right

        if isAllNotNone():
            # Первое вхождение, нужно, чтобы условие после следующего else ничего не сломало
            if arr_flag == 3:
                winners.append(root)
                root = None
            else:
                if len(winners) > 0 and root >= winners[-1]:
                    winners.append(root)
                    root = None
                else:
                    losers.append(root)
                    root = None

    print(winners)
    print(losers)

    return [winners, losers]


def array_merge(arr1, arr2):

    flag1 = 0
    flag2 = 0
    buffer = []

    while True:
        if flag1 > len(arr1)-1:
            buffer += arr2[flag2:]
            break
        elif flag2 > len(arr2)-1:
            buffer += arr1[flag1:]
            break
        else:
            if arr1[flag1] <= arr2[flag2]:
                buffer.append(arr1[flag1])
                flag1 += 1
            else:
                buffer.append(arr2[flag2])
                flag2 += 1

    return buffer


def tournament_sort(arr):

    losers = arr
    winners_big = []

    while len(losers) > 0:
        result = tournament(losers)
        winners_buffered = result[0]
        losers = result[1]

        winners_big.append(winners_buffered)

    print(winners_big)
    print()

    for i in range(1, len(winners_big)):
        winners_big[0] = array_merge(winners_big[0], winners_big[i])
        winners_big[i] = []
        print(winners_big)

    return winners_big[0]

