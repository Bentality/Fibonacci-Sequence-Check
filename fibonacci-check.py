print("Enter a nuber to see if it is in the fibbonacci sequence!!!")

while 1:
    x = int(input("Enter a number, 0 to quit: "))
    
    if x == 0:
        break

    A = [0, 1]

    for i in range(2,720):

        A.append(A[i-1]+A[i-2])

    bool=False

    for i in range(2,720):

        if x==A[i]: 

            bool=True
            break

    if bool==True:

        print ("Is Fibonacci")
    else: 

        print("Not Fibonacci")
