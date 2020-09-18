def merge(leftSubArray , rightSubArray ):
    result = []
    while len(leftSubArray ) != 0 and len(rightSubArray ) != 0:
        if leftSubArray [0] < rightSubArray [0]:
            result.append(leftSubArray [0])
            leftSubArray .remove(leftSubArray [0])
        else:
            result.append(rightSubArray [0])
            rightSubArray .remove(rightSubArray [0])

    if len(leftSubArray ) == 0:
        result += rightSubArray
    else:
        result += leftSubArray

    return result


def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        leftSubArray  = mergeSort(arr[:middle])
        rightSubArray  = mergeSort(arr[middle:])
        return merge(leftSubArray , rightSubArray )
