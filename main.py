import timeit

# Importing all algorithms here
from bubble_sort import bubbleSort
from heap_sort import heapSort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from quick_sort import quickSort

# Importing the input and output file directory
input_dir = "input_data/"
output_dir = "output/"


def time_it(func_name, data):
    total_time = 0
    for i in range(50):
        start = timeit.default_timer()
        if func_name.__name__ == "quickSort":
            result = func_name(data, 0, len(data))
        else:
            result = func_name(data)
        end = timeit.default_timer()
        total_time += end - start
    return (total_time / 50) * 1000000, result


def run_algorithms(options, nature, data):
    time_taken_bubble, result_b = time_it(bubbleSort, data)
    time_taken_insert, result_i = time_it(insertionSort, data)
    time_taken_merge, result_m = time_it(mergeSort, data)
    time_taken_quick, result_q = time_it(quickSort, data)
    time_taken_heap, result_h = time_it(heapSort, data)
    if options == 'functionality':
        output_file = ""
        output_file += f'Input string: {str(data)}\n\n'
        output_file += f'Output of Bubble Sort is: \n{str(result_b)}\n'
        output_file += f'Output of Insertion Sort: \n{str(result_i)}\n'
        output_file += f'Output of Merge Sort: \n{str(result_m)}\n'
        output_file += f'Output of Quick Sort: \n{str(result_q)}\n'
        output_file += f'Output of Heap Sort: \n{str(result_h)}\n'
        open(f'{output_dir}func_correctness.txt', "w+").write(output_file)
        print(f'Output for the functional correctness of the sorting algorithms '
              f'can be found in {output_dir}func_correctness.txt')
    output_time = ""
    output_time += f'Algorithm Runtime\n\n'
    output_time += f'Length of the Input: {len(data)}\n'
    output_time += f'Nature of the data is: {nature}\n\n'
    output_time += f'Runtime (in microsecond) for Bubble sort is: {time_taken_bubble}\n'
    output_time += f'Runtime (in microsecond) for Insertion sort is: {time_taken_insert}\n'
    output_time += f'Runtime (in microsecond) for Merge sort is: {time_taken_merge}\n'
    output_time += f'Runtime (in microsecond) for Quick sort is: {time_taken_quick}\n'
    output_time += f'Runtime (in microsecond) for Heap sort is: {time_taken_heap}\n'
    open(f'{output_dir}{options}_runtime.txt', "w+").write(output_time)
    print(f'Runtime analysis of the sorting algorithms can be found in {output_dir}{options}_runtime.txt')


if __name__ == '__main__' :
    while True:
        option = int(input("Choose from one of the following options:"
                           "\n1.Functional correctness of the sorting algorithms.\n"
                           "2.Analysis of runtime of the sorting algorithm w.r.t varying input sizes\n3.Exit.\n"
                           "Enter your choice : "))
        if option == 1:
            input_str = open(f"{input_dir}random_50.txt", "r").read().replace(' ', '').split(",")
            input_data = [int(num) for num in input_str]
            run_algorithms('functionality', 'random', input_data)
        elif option == 2:
            data_size = int(input("Enter data set size [1000, 10000, 50000, 75000] :"))
            data_nature = str.lower(input("Please select the nature of the data [Random (r), Sorted (s)] :"))
            if data_nature != 'r' and data_nature != 's':
                print("Choose either 'r' or 's'")
                break
            if data_nature == 'r':
                data_nature = 'random'
            else:
                data_nature = 'sorted'
            input_str = open(f'{input_dir}{data_nature}_{data_size}.txt', "r").read().split(",")
            input_data = [int(num) for num in input_str]
            run_algorithms('analysis', data_nature, input_data)
        elif option == 3:
            print("Exiting")
            break
        else:
            print("Please choose from option #1, #2 or #3\n")