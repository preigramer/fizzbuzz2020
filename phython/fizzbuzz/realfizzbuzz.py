"""A FIzzBuzz Program"""

from numbers import Number

def fizz(x):
    """ 
    Takes an input 'x' and checks to see if x is a number, 
    and if so, also a multiple of 3.
    If it is both, return 'fizz', Otherwise, return the input.
    """
    return 'fizz' if isinstance(x,Number) and x % 3 == 0 else x
    # # determine if x is a number or not
    # if isinstance(x, Number) and x % 3 == 0:
    #     # yes, it is a number
    #         return 'fizz'
    #     else:
    #         # no it is not a number 
    #         return x