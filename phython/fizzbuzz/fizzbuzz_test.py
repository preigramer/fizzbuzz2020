

from fizzbuzz import Fizz, Buzz, Fibu

def describes_a_buzz_function(): ""

    def throws_an_error_if_no_input():
        with raises(Exception) as err_info:
        buzz()
    assert err_info == TypeError
    assert 'missing 1 requiried positional argument' in s


    def can_determine_if_a_number_is_a_multiple_of_5():
        """Checks to see if a given number is a multiple of 5."""
        assert Buzz(5)== 'Buzz'         #multiple of 5
        assert Buzz(2)== 2              #non-multiple of 5
        assert Buzz(5.5)== 3.5          #non - integer
        assert Buzz(0)== 0              #zero
        assert Buzz(-5)== 'Buzz'        #negative multiple of 5
        assert Buzz(-4)== -4            #negative non-multiple of 5
        assert Buzz("Buzz")== 'Buzz'    #non-numeric input
        assert Buzz() == 'error'        #no input