# Q:1 Print "Hello, World!"
print('Hello World!')

#Q:2 Take a name as input and print it
name = input('Please Enter name')
print('Hello',name)

# Q:3 Swap values of a and b
a =5
b = 10
a,b = b,a
print(a,b)

# Q:4 Check if number is even or odd

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q.5 Largest of 3 Numbers
a, b, c = 10, 20, 15
largest = max(a,b,c)
print(largest)

# Q.6 Factorial
n =5
fact =1 
for i in range(1, n +1):
    fact *= i
    print(fact)

# Q.7 Fibonacci Series

n = 6
a,b = 0,1
for _ in range(n):
    print(a, end=" ")
    a,b = b, a+b

# Q.8 Reverse a String
text = "python"
print(text[::-1])

# Q.9 Palindrome String
text = "madam"
if text == text[::-1]:
    print("Plindrome")

# Q.10 Prime Number

num = 7
for i in range(2,num):
 if num % 2 == 0:
    print("Not Number")
    break;
else:
   print("Prime Number")

   print("Hello Mohammad")