from typing import Callable

def find_next_symbol(eq: str, symbol_to_find: str, offset: int) -> int:
    """
    Returns the index of next symbol_to_find starting after the offset index

        Params:
            - eq: equation to look through
            - symbol_to_find: symbol we're looking for (+,-,*,/)
            - offset: offset into equation

        Returns:
            - None if symbol not found
            - index of symbol
    """

    raise NotImplementedError("find_next_symbol not yet implemented")

def find_previous_symbol(eq: str, offset: int) -> int:
    """
    Returns the index of the first symbol that occurs before the offset index

        Params:
            - eq: equation to look through
            - offset: offset into the equation

        Returns:
            - None if no symbol found before the offset
            - index of the symbol
    """

    raise NotImplementedError("find_previous_symbol not yet implemented")

def process_operation(eq: str, symbol: str, op_func: Callable[[str, str],float]) -> str:
    """
    Processes all the operations of the specified symbol and updates the equation according

        Params:
            - eq: equation
            - symbol: symbol we want to process (+,-,*,/)
            - op_func: function that will do the operation specified
        Notes:
            - op_func will do the operation corresponding to the symbol passed in.
            If the symbol is +, calling op_func(num1, num2) will return num1+num2.

        Returns:
            - equation that has processed all of the operations involving the symbol
            specified. If I call process_operation("1*3+2+3*5", "*", ...), it should return
            "3+2+15".
    """

    raise NotImplementedError("process_operation not yet implemented")
