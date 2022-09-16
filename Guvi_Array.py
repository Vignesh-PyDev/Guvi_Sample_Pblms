# 1
# you are given with array of numbers.you have to find whether array is beautiful or not. A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5

# Input Description:
# You are given a number ‘n’ denoting the size of array.Next line contains n space separated numbers.

# Output Description:
# Print 1 if array is beautiful and 0 if it is not

# Sample Input :
# 5
# 5 25 35 -5 30
# Sample Output :
# 1

ip_1 = input()

ip = ["1" if int(x) % 2 == 0 and  int(x) % 3 == 0 and  int(x) % 5 == 0 else "0" for x in input().split(' ')]

if "1" in ip:
    
    # print(ip)
    
    print(1)
    
else:
    
    print(0)

# 2

# You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids.

# Input Description:
# First line contains a number ‘n’ representing no of prisoners. Next line contains n space separated numbers.

# Output Description:
# Print the ids which are not unique. Print -1 if all ids are unique

# Sample Input :
# 7
# 1 1 11 121 131 141 98
# Sample Output :
# 1

ip1 = input()

ip = [int(e) for e in input().split(' ')]

# print(ip,"ip")

op = {Iter:ip.count(Iter) for Iter in ip if ip.count(Iter) > 1}

print(''.join(str(e) for e in list(op.keys())))

# 3

# You are given with an array. For each element present in the array your task is to print the next smallest than that number. If it is not smallest print -1

# Input Description:
# You are given a number ‘n’ representing size of array. And n space separated numbers.

# Output Description:
# Print the next smallest number present in array and -1 if no smallest is present

# Sample Input :
# 7
# 10 7 9 3 2 1 15
# Sample Output :
# 7 3 3 2 1 -1 -1


ip = input()

ip1 = [int(e) for e in  input().split() if int(e) <= int(ip)]

op = []

# print(ip1)

if sorted(set(ip1)) == ip1:
    
    for x in range(max(ip1)):
        
        op.append(-1)
    
    print(*(op))

else:
    

    for x in range(len(ip1)):

        if x == 0:

            op.append(ip1[x])

        else:

            for y in range(ip1[x] - 1):

                op.append(ip1[x])

    if min(ip1) == op[-1]:

        pass

    else:

        op.append(min(ip1))

        if len(op) == int(ip):

            pass

        else:

            for y in range(abs(len(op) - int(ip))):

                op.append(-1)

    
    
# else:
    
#     if ip1 == sorted(ip1):
        
        
    
#         op1 = []

#         for x in range(int(ip)):

#             op1.append(-1)

#         print(*(op1),"op1")

    print(*(op))        

# 4

# You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

# Input Description:
# First line contains a number ‘n’. Then next line contains n space separated numbers.

# Output Description:
# Print the difference of indices of largest and smallest array

# Sample Input :
# 5
# 1 6 4 0 3
# Sample Output :
# -2

ip_1 = int(input())

ip = [int(e) for e in input().split(' ')]


# print(ip.index(min(ip)))
print(int(ip.index(max(ip))) - int(ip.index(min(ip))))

# 5

# You are given an array of numbers. Print the least occurring element. If there is more than 1 element print all of them in decreasing order of their value.

# Input Description:
# You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

# Output Description:
# Print the number as mentioned

# Sample Input :
# 9
# 1 6 4 56 56 56 6 4 2
# Sample Output :
# 2 1

ip1 = input()

ip = input().split()

ip = {e:ip.count(e) for e in ip}

# sorted(ip.values())[0]

# ip[sorted(ip)[0]

print(' '.join(reversed(sorted(str(e) for e in [int(k) for k,v in ip.items() if int(v) == 1][::-1]))))

# 6

# You are a passport issuer, but due to some problems in the system, there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers. You are given a list of passport numbers.

# Input Description:
# You are given length of list.Second line,You are given with a list.

# Output Description:
# Print the list of passport numbers without duplicates.

# Sample Input :
# 5
# A23 B56 B56 C79 D16
# Sample Output :
# A23 B56 C79 D16

ip = input()

userInput_1 = input().split()

Temp = []

op = [Temp.append(e) for e in userInput_1 if e not in Temp]

print(' '.join(Temp))

# 7


# You are given with two arrays. Your task is to merge the array such that first array is in ascending order and second one in descending order.

# Input Description:
# First line contains two integer ‘n’ and ‘m’. ‘n’ denotes length of array 1 and ‘m’ of array 2.Next line contains n space separated numbers and third line contains ‘m’ space separated numbers

# Output Description:
# Print a single array in desired order

# Sample Input :
# 3 3
# 23 15 16
# 357 65 10
# Sample Output :
# 15 16 23 357 65 10

userInput = input()
userInput_1 = sorted([int(e) for e in input().split()],reverse=False)
userInput_2 = sorted([int(e) for e in input().split()],reverse=True)

# sorted(userInput_1,reverse= True)

print(' '.join(str(e) for e in userInput_1 + userInput_2))

# 8

# A person saves his monthly saving according to given schema. He saves same amount of money which is equal to the money saved in immediate previous two months. Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell how much he had totally saved at the end of ‘n’ months

# Input Description:
# You will be given a number ‘n’->No. of months

# Output Description:
# Print the total savings at the end of ‘n’ months

# Sample Input :
# 1
# Sample Output :
# 2000

ip = int(input())

s = 1

op = []

for x in range(1,1+ip):
    
    op.append(((s + x) * 1000))
    
    if x == ip:
        break
        
    s += x
    
print(op[-1])   

# 9

# Given a string S, print it without using semicolon in your program.
# Sample Testcase :
# INPUT
# hello world
# OUTPUT
# hello world

userInput = input()
print(userInput)

# 10

# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
# Sample Testcase :
# INPUT
# 4 2
# 1 2 3 3
# OUTPUT
# yes


userInput = input().split()[1]

print("yes" if userInput in input().split() else "no")

# 11


# Pk finds it difficult to judge the minimum element in the list of elements given to him. Your task is to develop the algorithm in order to find the minimum element.

 

# Note:Don’t use sorting
 

# Input Description:
# You are given ‘n’ number of elements. Next line contains n space separated numbers.

# Output Description:
# Print the minimum element

# Sample Input :
# 5
# 3 4 9 1 6
# Sample Output :
# 1

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

ip = input()
userInput_1 = input().split()

for i in range( len( userInput_1 ) ):
    least = i
    for k in range( i + 1 , len( userInput_1 ) ):
      if userInput_1[k] < userInput_1[least]:
        least = k

    swap( userInput_1, least, i )

print(userInput_1[0])

# 12


# Loki wants to steal the tesseract but in order to do so, he has to rearrange the elements in an array in a specific manner which is mentioned in a clue. The clue says ‘cursed are the odd and sorted are the even’. Loki manages to decode the clue which translates to “sort the even positioned elements of an array, starting from the element at index 0, in ascending order”. Manipulate the array so as to help Loki steal the tesseract.
 

# Input Description:
# Size of the array followed by the elements of the array

# Output Description:
# Even index array elements sorted in ascending order

# Sample Input :
# 5
# 3 9 1 44 6
# Sample Output :
# 1 9 3 44 6



userInput = input()

ip = [e for e in input().split()]



al = sorted(ip[0::2]) + ip[1::2] 

n = round(len(al)/2)

# print(n)

if len(al) % 2 == 1:
    
    al.append(' ')
    
    n = round(len(al)/2)
    
# print(n)

ev,od = al[:n],al[n:]

# print(ev,"even",od,"odd")

        
ev_ls = (x for x in ev)

od_ls = (x for x in od)

        
def od_list():
    
    for x in range(len(od)):
        
        yield(od[x])        
        
tmp = []


for x in range(1,len(ev) + len(od) + 1):
    
    if x % 2 == 0:
        
        tmp.append(next(od_ls))
        
#         tmp.append(next(od_list()))
        
    elif x % 2 == 1:
        
        tmp.append(next(ev_ls))
#         print((next(ev_list())))
#         tmp.append(next(ev_list()))

print(' '.join(str(e) for e in tmp).strip())

# 13

# Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
# Input Size : N <= 100000
# Sample Testcase :
# INPUT
# 2143
# OUTPUT
# 1 3

ip = ' '.join([str(e) for e in input() if int(e) % 2 == 1 ])

# ip = input()


print(ip if len(ip) >= 1 else "-1")

# 14

# Ramesh is a student and wants to find out if there is any other student in his class who has got the same marks as his, in maths. Help him to find out.
 

# Input Description:
# First line contains the number of students in the class followed by Ramesh’s mark. Second line contains the marks of all students in the class.

# Output Description:
# Index of student who got mark same as Ramesh’s mark. If no such mark exists, return -1.

# Sample Input :
# 2 10
# 1 2
# Sample Output :
# -1

userInput = input().split()

ip = input().split()

if userInput[1] in ip:
    
    print(ip.index(userInput[1]))
    
else:print(-1)

#15


# You are an intern at GUVI and the company wants to organise its data and delete unnecessary extra storage elements used. You are given k arrays of unequal dimensions. Sort the k arrays individually and concatenate them.
 

# Input Description:
# First line contains the number of arrays. Subsequent lines contain the size of the array followed by the elements of the array.

# Output Description:
# An array containing the sorted elements of k sorted arrays

# Sample Input :
# 3
# 2
# 98 12
# 6
# 1 2 3 8 5 9
# 1
# 11
# Sample Output :
# 12 98 1 2 3 5 8 9 11

userInput = input()

tmp = []

for x in range(int(userInput)):
    
    ip = int(input())
    
    tmp += sorted(int(x) for x in input().split())
    
# print("The Input Provided is: " + userInput)

print(' '.join(str(e) for e in tmp))

#16


# Ria is a 5 year old girl. Her mother wants to teach her how to sort words in the same order that they appear in a dictionary. She decides to write a program to sort a given set of strings based on their alphabetical order. Help Ria’s mother to complete the program.

 

# Input Description:
# A set of N strings

# Output Description:
# Alphabetically sorted set of strings

# Sample Input :
# 3
# InfinityWar EndGame Avengers
# Sample Output :
# Avengers EndGame InfinityWar

op = input() 

ip = sorted(input().split())

print(' '.join(ip))

#17


# Ria is a 5 year old girl. Her mother wants to teach her how to sort words in the same order that they appear in a dictionary. She decides to write a program to sort a given set of strings based on their alphabetical order. Help Ria’s mother to complete the program.

 

# Input Description:
# A set of N strings

# Output Description:
# Alphabetically sorted set of strings

# Sample Input :
# 3
# InfinityWar EndGame Avengers
# Sample Output :
# Avengers EndGame InfinityWar

op = input() 

ip = sorted(input().split())

print(' '.join(ip))

#18

# Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
# Sample Testcase :
# INPUT
# hello
# OUTPUT
# he*lo

ip = [str(e) for e in input()]

if len(ip) % 2 == 0:
    
    ip[round(len(ip) / 2) - 1:round(len(ip) / 2) + 1] = ["*","*"]
    
    print(''.join(ip))
    
else:
    
    ip[round(len(ip) / 2)] = "*"
    
    print(''.join(ip))
#19

# You are given an array of numbers. Print the least occurring element. If there is more than 1 element print all of them in decreasing order of their value.

# Input Description:
# You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

# Output Description:
# Print the number as mentioned

# Sample Input :
# 9
# 1 6 4 56 56 56 6 4 2
# Sample Output :
# 2 1

sp = int(input())

ip = [int(e) for e in input().split(' ')]

# print(ip,"ip")

op = {Iter:ip.count(Iter) for Iter in ip}

indi = sorted(op.values())[0]

keyy = []


# print(op)

for k,v in op.items():
    
    if v == indi:
        
#         print(k,"loop")
        
        keyy.append(k)


print(' '.join([str(e) for e in sorted(keyy,reverse=True)]))

# 20


# In a world cup tournament,no of goals scored by each team is given to you. Your task is to calculate net goal rate of each team.

# Net goal rate of team is calculated

 

# No of goals(team)- sum of(no of goals by last 3 teams)

# Input Description:
# You are given a number ‘n’.Next line contains n space separated numbers.

# Output Description:
# Print the net goal rate of each team

# Sample Input :
# 5
# 95 85 75 12 11
# Sample Output :
# -3 -13 -23 -86 -87

from functools import reduce

ip = input()

ip1 = [int(e) for e in input().split()]

print(' '.join([str(e - reduce(lambda x,y:x+y,ip1[-3:])) for e in ip1]))

#21


# Rajesh and Ram are having a conflict on the maximum marks that they have scored in all the exams conducted in the past year. The one having scored the maximum gets a treat from the other. They decide to go through their test papers and record their highest marks. You are Rajesh’s best friend and as he has tutions to attend, he gives you all his test papers and asks you to find out the maximum marks that he has scored among all the marks in all exams. He promises you a treat if he wins the bet with Ram. Help Rajesh find out his highest marks.

# Constraints:

# 1 <= N <= 10

# 0 <= A[] <= 100

# Input Description:
# First line contains count of marks. Next line is the list of marks obtained by Rajesh.

# Output Description:
# Highest marks obtained by Rajesh.

# Sample Input :
# 3
# 82 96 72
# Sample Output :
# 96

#A Simple Hello World
# print("Hello World")

#Getting input via STDIN
userInput = int(input())

ip = [int(x) for x in input().split()]


print(max(ip))

#22


# You are given two arrays of equal length. Your task is to merge the two arrays then sort them too and then find the sum of two middlemost elements.

# Input Description:
# You are given a number ‘n’. Then Next line contains first list of 'n' separated numbers.Third line contains second list of 'n' space separated numbers.

# Output Description:
# Print the sum of two middle elements

# Sample Input :
# 5
# 1 9 16 25 46
# 2 3 4 5 6
# Sample Output :
# 11

userInput = input()

ip = sorted([int(x) for x in input().split()]  + [int(y) for y in input().split()])


# print(ip)

print(ip[round(len(ip) / 2)] + ip[round(len(ip) / 2) - 1])

#23

# Given numbers A,B find A^B.
# Input Size : 1 <= A <= 5 <= B <= 50
# Sample Testcase :
# INPUT
# 3 4
# OUTPUT
# 81

userInput = [int(x) for x in input().split()]

print(userInput[0] ** userInput[1])

#24

# You are a software engineer at an MNC. You are given the task of sorting the employees in your company based on their salary. Perform the task so that the employees, including yourself, will get a bonus from the management.

# CONSTRAINT:

# 0<=salary<=1000000

 

# Input Description:
# Number of employees followed by their name and salary

# Output Description:
# Sorted list of employee names

# Sample Input :
# 3
# Karthik 23000 rohan 81734 varshini 12343
# Sample Output :
# varshini
# Karthik
# Rohan

ip1 = input()

ip = input().split()

srt = sorted(ip[1::2])

for x in srt:
    
    print(ip[ip.index(x) - 1])
# 24

# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
# Sample Testcase :
# INPUT
# 6 2
# 1 2 3 5 7 8
# OUTPUT
# 0

ip = input().split()
ip1 = [int(e) for e in input().split()].count(int(ip[1]))

print(ip1-1 if ip1 else -1)

# 25

# Given a number N and 2 arrays A and B of sorted order of size N, print the common elements.If it is not found print -1.
# Input Size : 1 <= N <= 100000
# Sample Testcase :
# INPUT
# 5
# 1 1 1 1 1
# 1 2 3 4 5
# OUTPUT
# 1

ip  = input()

ip1  = input().split()

ip2  = input().split()

lst = []

for i in ip1:
    
    if i in ip2:
        
        lst.append(i)
        
        ip2.remove(i)
        
            
print(' '.join(str(e) for e in lst) if len(lst) >= 1 else "-1")  

# 26


# Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her. As an examiner develop an algorithm to test her memory.

 

# CONSTRAINTS

# 1<=Y,N,T<=1000

# Input Description:
# First line contains no. of test cases(Y). Next line contains a number N. Next line contains n space separated numbers Next line contains a number T denoting the number of questions asked from you regarding the given array. Next line contains T space separated numbers.

# Output Description:
# Print the occurrence of each number if present else “NOT PRESENT”

# Sample Input :
# 10
# 1 1 1 2 2 2 3 8 9 7
# 5
# 1 2 3 0 5
# Sample Output :
# 3 3 1 Not Present Not Present


# 1 1 1 2 2 2 3 8 9 7

# 1 2 3 0 5

ip  = input()

ip1  = input().split()

ip_1  = input()

ip2  = input().split()

print(' '.join(str(x) for x in [ip1.count(e) if ip1.count(e) >= 1 else "Not Present"  for e in ip2]))


# 25


# Prakash is bored and wants to spends his time. He starts rolling a die (having the face values as 1, 2, 3, 4, 8, 15, 7, 9) and observes that some of the values keep repeating. Also while rolling n times, some face appear once only. Find the number on its face.

# Constraints

# 0 <   N  <= 100

# 0 <= A[i] <= 100

 

# Input Description:
# The first line contains a positive integer N, denoting the size of the array. The second line contains N positive integers, denoting the face values that appeared when the die was rolled.

# Output Description:
# Print out the singly occurring number. print 0 if no numbers are repeating.

# Sample Input :
# 5
# 1 1 2 5 5
# Sample Output :
# 2

ip  = input()

ip1  = input().split()


# print(len([e  for e in ip1 if ip1.count(e) > 1]))

print(' '.join([e  for e in ip1 if ip1.count(e) == 1]) if len([e  for e in ip1 if ip1.count(e) > 1]) >=1 else "0")

#26

# Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -1
# Input Size : |sentence| <= 1000000(complexity O(n)).
# Sample Testcase :
# INPUT
# I enjoy doing codekata
# codekata
# OUTPUT
# 1

# I enjoy doing codekata
# codekata

ip = input().split()

ip1 = input()

print(ip.count(ip1) if ip.count(ip1) >= 1 else "-1")

#27

# You are given given task is to print whether array is ‘majestic’ or not.A ‘majsetic’ array is an array whose sum of first three number is equal to last three number.

# Input Description:
# You are given a number ‘n’,Next line contains ‘n’ space separated

# Output Description:
# Print 1 if array is majestic and 0 if it is not

# Sample Input :
# 7
# 1 2 3 4 6 0 0
# Sample Output :
# 1

from functools import reduce

ip1 = input()

ip = [int(e) for e in input().split()]



# ip = [int(e) for e in "1 2 3 4 6 0 0".split()]

print("1" if reduce(lambda x,y:x+y,ip[:3]) == reduce(lambda a,b:a+b,ip[-3:]) else "0")