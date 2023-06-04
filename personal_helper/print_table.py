"""
The TablePrinter module provides a utility class for printing tabular data to the console.
"""

class TablePrinter:
    """
    A utility class for printing tabular data to the console.

    Usage:
    - Initialize an instance of TablePrinter with a list of data.
    - Call the print_table() method to print the table.
    """
    def __init__(self, data: list) -> None:
        self.data = data

    def calculate_column_widths(self) -> list[int]:
        """
        The calculate_column_widths function takes the data and returns a list of integers.
        The length of the list is equal to the number of columns in self.data, and each element
        in that list represents how wide that column should be when printed.
        """
        num_columns = len(self.data[0])
        column_widths = [0] * num_columns
        for row in self.data:
            for i in range(num_columns):
                column_widths[i] = max(column_widths[i], len(str(row[i])))
        return column_widths

    def format_columns(self, columns: list, column_widths: list[int]) -> str:
        """
        The format_columns function takes a list of columns and a list of column widths,
        and returns the formatted string. The zip function is used to iterate over both lists at once.
        The f-string formatting syntax is used to format each column with its corresponding width.
        """
        formatted_columns = [f"{column:<{width}}" for column, width in zip(columns, column_widths)]
        return "| " + " | ".join(formatted_columns) + "|"

    def format_data_row(self, row: list | str, column_widths: list[int]) -> str:
        """
        The format_data_row function takes a row of data and formats it to fit the column widths.
        """
        formatted_row = [f"{str(column):<{width}}" for column, width in zip(row, column_widths)]
        return "| " + " | ".join(formatted_row) + "|"

    def print_table(self) -> None:
        """
        The print_table function prints a table of data to the console.
        """
        column_widths = self.calculate_column_widths()

        horizontal_line = "-".join("-" * (width + 2) for width in column_widths)
        print(horizontal_line)

        formatted_header = self.format_columns(self.data[0], column_widths)
        print(formatted_header)

        print(horizontal_line)

        for row in self.data[1:]:
            formatted_row = self.format_data_row(row, column_widths)
            print(formatted_row)

        print(horizontal_line)
