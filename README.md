# Gauss-Jordan Elimination Solver

This Python script implements the Gauss-Jordan elimination method to solve systems of linear equations.

## Usage

1.  **Save the script:** Save the Python code as a `.py` file (e.g., `gauss_jordan.py`).
2.  **Run the script:** Execute the Python script from your terminal or command prompt.
3.  **Input matrix dimensions:** The script will prompt you to enter the number of rows (`n`) and columns (`v`) of the augmented matrix.
4.  **Input matrix elements:** The script will then prompt you to enter each element of the matrix row by row.
5.  **View the solution:** The script will perform Gauss-Jordan elimination and display the resulting reduced row-echelon form of the matrix, along with the solutions for each variable.

## Class `gauss_jordan`

* **`__init__(self, n, v)`:**
    * Initializes the `gauss_jordan` object with the number of rows (`n`) and columns (`v`) of the matrix.
* **`receive_elements(self)`:**
    * Prompts the user to input the elements of the augmented matrix.
    * Creates a NumPy array (`mat`) to store the matrix.
    * Stores the matrix as a global variable.
* **`row_reduction(self)`:**
    * Performs Gauss-Jordan elimination on the input matrix.
    * Prints the matrix at various stages of the reduction process to show the steps involved.
    * Prints the solutions for each variable (`X1`, `X2`, etc.).
    * Returns the reduced row-echelon form of the matrix.

## Example Usage

```python
from gauss_jordan import gauss_jordan

n = int(input("Enter number of rows: "))
v = int(input("Enter number of columns: "))

solver = gauss_jordan(n, v)
solver.receive_elements()
reduced_matrix = solver.row_reduction()

print("\nReduced Row-Echelon Form:\n", reduced_matrix) 
