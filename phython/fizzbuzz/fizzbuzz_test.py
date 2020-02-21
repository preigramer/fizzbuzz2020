
def throws_an_error_if_no_input():
    with raises(Exception) as err_info:
        fizz()
    assert err_info.type


def can_determine_if_a_number_is_a_multiple_of_3():
    """Checks to see if a given number is a multiple of 3."""
    assert fizz(3)== 'Fizz'   #multiple of 3
    assert fizz(2)== 2 #non-multiple of 3
    assert fizz(3.5)== 3.5 #non - integer
    assert fizz(0)== 0   #zero
    assert fizz(-3)== 'Fizz'  #negative multiple of 3
    assert fizz(-4)== -4 #negative non-multiple of 3
    assert fizz("buzz")== 'buzz' #non-numeric input
    assert fizz() == 'error' #no input