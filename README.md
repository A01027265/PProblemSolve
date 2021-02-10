# P Problem Solver
A CLI program where the user inputs a `.txt` file with a K-SAT problem and a solution to verify. The program then responds with a 1 if the user's solution was accepted or with a 0 if the user's solution was rejected for the K-SAT problem in question.

## What I Learned
- Text conversion to correct format (string parsing)
- Efficient verification for P-Problem solutions

## Authors
- Emilio Popovits Blake (A01027265)
- Patricio Tena (A01027293)
- Ana Paola Minchaca (A01026744)
- Rodrigo Benavente (A01026973)

## Input
Each *P* problem must be saved as a .txt file individually inside '/Input' directory for the program to run properly in the following format:

```sh
c A SAT instance generated from a 3-CNF formula that had 91 clauses and 20 variables
p cnf 20 91
10000111101010101010
9 -3 16 0
4 -16 20 0
-4 6 5 0
-6 -5 4 0
-6 -12 -13 0
-19 -16 13 0
1 -20 -9 0
6 -2 5 0
-4 -11 15 0
-16 8 10 0
-5 2 18 0
-5 8 3 0
-4 -20 -6 0
7 -6 20 0
-17 2 -3 0
-8 -9 -11 0
...
8 10 -19 0
```

Where the first line describes the problem in question, the second line provides a shorthand summary of the problem, and the third line provides an input binary string to be tested against the clauses starting from the fourth line untill the last line.

### Sample Input
Two sample inputs (one that accepts and one that rejects respectively) are provided in the '/Input' directory as `demoaccept.txt` and `Instance_3SAT_example.txt`.

## Output

This program will output a 0 if the binary string provided in line 3 is rejected or a 1 if the binary string provided in the line 3 is accepted.
