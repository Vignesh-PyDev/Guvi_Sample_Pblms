# 1
# Share
# Write a code to get the input in the given format and print the output in the given format

# Input Description:
# To take an integer value

# Output Description:
# Print the integer value

# Sample Input :
# 2
# Sample Output :
# 2

print(input())

# 2
# Share
# Write a code to get the input in the given format and print the output in the given format

# Input Description:
# A single line contains integers separated by space

# Output Description:
# Print the integer list of integers separated by space

# Sample Input :
# 2 3 4 5 6 7 8
# Sample Output :
# 2 3 4 5 6 7 8

print(input())

# 3
# Share
# Write a code to get the input in the given format and print the output in the given format

# Input Description:
# First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.

# Output Description:
# Print the input in the same format.

# Sample Input :
# 2 4
# 2 4
# 2 4
# Sample Output :
# 2 4
# 2 4
# 2 4

#A Simple Hello World

userInput = input()

userInput_1 = input()

userInput_3 = input()


print(userInput)

print(userInput_1)

print(userInput_3)



# 4
# Share
# Write a code to get the input in the given format and print the output in the given format

# Input Description:
# Three integers are given in line by line.

# Output Description:
# Print the integers in a single line separate by space.

# Sample Input :
# 2
# 4
# 5
# Sample Output :
# 2 4 5

userInput_1,userInput_2,userInput_3 = input(),input(),input()


print(userInput_1,userInput_2,userInput_3)

# 8
# Share
# Write a code to get the input in the given format and print the output in the given format.

# Input Description:
# A single line contains three float values separated by space.

# Output Description:
# Print the float value separated by line.

# Sample Input :
# 2.3 4.5 7.8
# Sample Output :
# 2.3
# 4.5
# 7.8

userInput = list(input().split(' '))

for Iter in userInput:print(Iter)

# 9
# Share
# Write a code to get the input in the given format and print the output in the given format.

# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by line.

# Sample Input :
# guvigeek
# Sample Output :
# g
# u
# v
# i
# g
# e
# e
# k

userInput = input()
for Iter in userInput:print(Iter)


# 10
# Share
# Write a code to get the input in the given format and print the output in the given format.

# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by comma.

# Sample Input :
# guvi
# Sample Output :
# g,u,v,i


#A Simple Hello World
# print("Hello World")

#Getting input via STDIN
userInput = list(input())

print(','.join(userInput))