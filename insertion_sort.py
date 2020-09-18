def insertionSort(array):
    # for each element in the array
    for index in range(1, len(array)):
        present = array[index]
        position = index

        while position > 0 and array[position-1] > present:
            array[position] = array[position-1]
            position -= 1

        array[position] = present

    return array
