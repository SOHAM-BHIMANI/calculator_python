print("Welcome to My Calculator")
num_1 =int(input("Enter Your First Number :- "))
num_2 =int(input("Enter Your Second Number :- "))
add = num_1+num_2
mul = num_1*num_2
div = num_1/num_2
sub = num_1-num_2
print("select operation ")
print("1 . Add")
print("2 . Multiply")
print("3 . Divide")
print("4 . Subtract")
b = input("Enter Your Choice(1/2/3/4) :- ")
if b == "1" :
    print(num_1,"+",num_2,"=", add)
elif b == "2" :
    print(num_1,"*",num_2,"=", mul)
elif b == "3" :
    print(num_1,"/",num_2,"=", div)
elif b == "4" :
    print(num_1,"-",num_2,"=", sub)
else:
    print("invalid operation")

