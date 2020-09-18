# Analysis_of_different_sorting_algorithm

Implementing and comparing the running time changes with respect to data size of different sorting algorithms

To run the sorting algorithm, simply run `python main.py` from the root directory.

This project implements two way of running the setup -- <b>to check for functional correctness of the sorting algorithms </b>
and <b>do analysis of the runtime of the sorting algorithms, which can be inputted from the command-line</b>.

For functional correctness, an input file of 50 random integers is inputed to the sorting algorithms
the output is writtn to a functional_correctness.txt file containing the result of the sorting algorithms
and runtime is stored in another file called functional_analysis.txt.
  
For analysis of runtime, different kinds of data options are given to check for the runtime of the sorting algorithms.
The idea is to check for various edge-cases for the algorithms implemented in this project
User is given with options to choose from data size ranging from 1000 to 75,000 with two input characteristic like random or sorted.
Once the user selects the option from the list,the output of this operation is a 
analysis_runtime.txt file which contains the runtime of each algorithm for the consumed input file.


Refer <b>`Project_Report.pdf`</b> file attached with this for evaluation of results.
