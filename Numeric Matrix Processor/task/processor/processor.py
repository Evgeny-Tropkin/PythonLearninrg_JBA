# region Classes
class CustomMatrix:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__value = [[0 for _ in range(self.__columns)] for _ in range(self.__rows)]

    def get_rows_count(self):
        return self.__rows

    def get_columns_count(self):
        return self.__columns

    def get_value(self):
        return self.__value

    def set_value(self):
        pass

    def __add__(self, other):
        """Addition of matrices"""
        if other.get_rows_count() == self.__rows and other.get_columns_count() == self.__columns:
            res = CustomMatrix(self.__rows, self.__columns)
            return res
        else:
            return ValueError

# end region


# region Methods
def main():
    matrix1 = input_matrix()
    matrix2 = input_matrix()
    try:
        result = matrix1 + matrix2
    except ValueError:
        print("ERROR")
    else:
        print(result.get_value())


def input_matrix():
    """ The function is intended for entering a matrix of a given dimension. \n
        Returns a List with elements of the List type. \n
        The number of nesting levels depends on the specified dimension of the matrix"""
    return []
# endregion


# region Script
if __name__ == "__main__":
    main()
# end region
