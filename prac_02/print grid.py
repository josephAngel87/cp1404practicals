"""Print Grid"""


def print_grid(number_of_rows, number_of_coloumns):
    for i in range(0,number_of_rows):
      print("*" * number_of_coloumns)

print_grid(4,2)