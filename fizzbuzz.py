N=101

def my_fizz_buzz_tarun(N):
    for i in range(1, N):
        if (i%3==0 and i%5!=0):
            print ("Fizz\n", end = "")
            # This occurs when it is divisible by 3
        elif(i%5==0 and i%3!=0):
            print ("Buzz\n", end = "")
            # This occurs  when it is divisible by 5
        elif(i%15==0):
            print ("FizzBuzz\n", end = "")
            # This occurs when it is divisible by 3 and 5
        else:
            print (i, end = "")
            print("\n", end = "")

my_fizz_buzz_tarun(N)