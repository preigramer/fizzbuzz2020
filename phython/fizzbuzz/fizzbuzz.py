x = 0
while x <= 100:
    if x % 15 == 0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print ("buzz")
    elif x % 3 == 0:
        print ("fizz")
    else: 
        print (x)
    x += 1

