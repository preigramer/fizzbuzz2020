def can_determine_if_a_number_is_a_multiple_of_3():
    """Checks to see if a given number is a multiple of 3."""
    assert fizz(3)== True   #multiple of 3
    assert fizz(2)== False  #non-multiple of 3
    assert fizz(3.5)== False #non - integer
    assert fizz(0)== True
    assert fizz(-3)== True
    assert fizz(-4)== False
    assert fizz("buzz")== False