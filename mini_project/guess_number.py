'''dict={"karnataka":"Bangalore","Maharastr":"mumbai","tamilnadu":"chennai","telangan":"hydrabad"}
print("---------------------------------")
print("Welcome to our website")

word=input("Please enter state to know its capital: ")

print("the capital of the "+ word+" is the "+dict.get(word))

# faulty dictionery
first_nos=input('enter the first values:')
second_nos=input('enter the second value:')
operator=input('which operation do you want to perform :')
dict={"45*3":"555", "56+9":"77","56/6":"4"}
expr=first_nos+operator+second_nos
reverse=second_nos+operator+first_nos

if expr in dict.keys():
    print(dict[expr])
elif reverse in dict.keys():
    print(dict[reverse])
else:
    print(eval(first_nos+operator+second_nos))

print("THANKS")
'''


#Guess the numbers
x=1212
count=0
attempt=10
while(True):
    n = int(input("enter the number : "))
    count=count+1
    if n == x:
        print('wow your guess is correct,Thanks  ')
        print("you attempted in ",count ,"count")
        break
    elif n > x and count < 10:
        print("your entered large number its not a number")
        attempt = attempt-1
        print("your attempt remaining is ",attempt)
    elif n < x and count < 10:
        print("the entered small no ,try again")
        attempt = attempt- 1
        print("your attempt remaining is ",attempt)
    elif (n < x) and count == 10 or (n>x) and count == 10:
        print('game over,please try again next time')
    else:
        pass

