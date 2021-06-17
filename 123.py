nterms = int(input("How many terms? "))
a,b = 0,1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(a)
        c = a + b
        # update values
        a = b
        b = c
        count += 1
           
           
