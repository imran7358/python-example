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

# Q.11 Sum of First N Numbers

n = 10
print(sum(range(1, n+1)))

# Q. 12 Count Vowels
text = "hello world"
count = sum(1 for ch in text if ch in "aeiou")

print(count)

# Q. 13 List Remove Duplicates

list = [1,2,3,3,4,4]
unique = (set(list))
print("Unique", unique)

# Q. 14 Find Max in List

nums = [14,15,50,90]
print("Maximum Num", max(nums))

# Q.15 Second Largest
nums = [14,15,50,90]
nums.sort()
print(nums[-2])

#Q.16 Merge Two Lists
a = [1,2]
b = [3,4]
print((a + b))

#Q.17 Merge Two Lists unsorted
a = [4,3]
b = [2,1]
print(sorted(a + b))

# Q.18 Dictionary Example

person = {"name": "Imran", "age": 30}
print(person["name"])

# Q.19 Dictionary Example
text = "apple"

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# Q.20 Function Example
def add(a, b):
    return a + b

print(add(2, 3))

