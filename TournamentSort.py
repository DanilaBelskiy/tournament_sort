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

