import numpy as np


def take_input(): 
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    user_input = input("Enter all elements: ")
    split_values = user_input.split()
    values = []
    for x in split_values:
        values.append(int(x))

    if len(values) != rows * columns:
         raise ValueError("Incorrect number of elements")


     
    matrix = np.array(values).reshape(rows, columns)
    return matrix
  

    

def matrix_addition(): 

    while True:
        try: 
            matrix1 = take_input()
            break
        except ValueError: 
            print("Enter values correctly")
    

    while True:
            try: 
                matrix2 = take_input()
                break
            except ValueError: 
                print("Enter values correctly")


    if matrix1.shape != matrix2.shape:
        print("Matrix must be of same dimensions")
        return

    print("First matrix: \n", matrix1)
    print("Second matrix \n", matrix2)
    print("Result = \n", matrix1+matrix2)
    
    
def matrix_subtraction():
    while True:
            try: 
                matrix1 = take_input()
                break
            except ValueError: 
                print("Enter values correctly")
        
    while True:
            try: 
                matrix2 = take_input()
                break
            except ValueError: 
                print("Enter values correctly")

    if matrix1.shape != matrix2.shape:
        print("Matrix must be of same dimensions")
        return

    print("First matrix: \n", matrix1)
    print("Second matrix \n", matrix2)
    print("Result = \n", matrix1-matrix2)

def matrix_multiply():
    while True:
            try: 
                matrix1 = take_input()
                break
            except ValueError: 
                print("Enter values correctly")
        
    while True:
            try: 
                matrix2 = take_input()
                break
            except ValueError: 
                print("Enter values correctly")

    if matrix1.shape[1] != matrix2.shape[0]:
        print("Matrix must be of same dimensions")
        return                

    print("First matrix: \n", matrix1)
    print("Second matrix \n", matrix2)
    print("Result = \n", np.dot(matrix1,matrix2))

option = None
while option!= 4:
    print("\nOperations available: \n" \
          "1. Addition \n" 
          "2. Subtraction \n" 
          "3. Multiplication \n"
          "4. Exit \n"
    )

    option = int(input("Select matrix operation: "))
    
    match option:
        case 1:
            result = matrix_addition()
        case 2:
            result = matrix_subtraction()
        case 3:
            result = matrix_multiply()
        case 4:
            break




