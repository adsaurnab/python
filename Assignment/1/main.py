# 1
# create a list -- please input first name in andrew, last name in mathew's place
# and you can put anything in the rest of the elements.
list1 = ["Andrew", "and", "Mathew", 18, "male", "Love food"]


# ----------------------------
# 2
# printing your list

# normal printing
print("Number 2: ",list1)
print()

# # or
# # forloop printing
# print("2")
# for data in list1:
#     print (data)


# ----------------------------
# 3
# print thirt element of your list
# third element is 2 because list counts as [ 0 ,1, 2 ,3 ,4, 5 ]
# so number 2 is mathew in this place

print("Number 3: ", list1[2])
print()

# ----------------------------
# 4
# print last element of your list
# as length gives the total length as 6
# but for lists last element we have to call by 5 so we subtract list1 length by 1 to get the element

print("Number 4: ", list1[len(list1)-1])
print()

# ----------------------------
# 5
# change value of the third element to 7

list1[2] = 7
print("Number 5: ",list1)
print()

# ----------------------------
# 6
# change value of the second element to 13

list1[1] = 13
print("Number 6: ",list1)
print()

# ----------------------------
# 7
# replace the value of first elementto the sum of second and third element

sum = list1[1] + list1[2]
list1[0] = sum
print("Number 7: ",list1)
print()

# ----------------------------
# 8
# define a new list V

V = [1,2,3]
print("Number 8 Before: ",V)

# here v.copy() is copying v to x
#  otherwise there was a recursion of dataand you can see the eaxample
#  by just removing x=V.copy() with x=V and see the result

x=V.copy()

# x is stored to last element
V[len(V)-1]=x
print("Number 8 After: ",V)

# # print using forloop
# for i in V:
#     print(i)

print()


# ----------------------------
# 9
# test is list contains 2

if 2 in V:
    print("Number 9: ", "list V contains 2")
else:
    print("Number 9: ","list V doesn't contain 2")

print()



# ----------------------------
# 10
#test if list1 contains "Hello"

if "Hello" in V:
    print("Number 10: ", "list1 contains Hello")
else:
    print("Number 10: ", "list1 doesn't contain Hello")

print()



# ----------------------------
# 11
# using slicing method print values from 1 to 3 in list1
# as they are asking to get 1 2 and 3rd in the list you have to put 4 in list1[1:4]
# because list tend to slice till before the last index you have given
# you can change and try putting 3 in the 4 place "list1[1:3]" and see the output

print("Number 11: ", list1[1:4])
# list2= list1[1:4]
# print(list2)
print()

# ----------------------------
# 12
# using slicing method add element [5,6,7,8] insted of 2nd and 3rd element



# list2 = list1[1:4]
# list2[1:] = [5,6,7,8]
# print("Number 12: ", list2)

# or
print("Number 12 Before : ", list1)
list1[1:3] = [5,6,7,8]
print("Number 12 After : ", list1)
print()



# ----------------------------
# 13
# using slicing method delete element 2 to 4

del list1[2:5]
print("Number 13: ",list1)

print()


# ----------------------------
# 14
# append value 6000 in list1

list1.append(6000)
print("Number 14: ", list1)

print()


# ----------------------------
# 15
# pop last element in list1
list1.pop()
print("Number 15: ", list1)

print()

# ----------------------------
# 16
# pop third element in list1

list1.pop(2)
print("Number 16: ", list1)

print()

# ----------------------------
# 17
# pring length of list 1
print("Number 17: ", len(list1))

print()

# ----------------------------
# 18
# define a new list V3 amnd combine list1 and v3
V3 = [5,6,8,7,9,7]
list1= list1+V3
print("Number 18: ",list1)

print()

# ----------------------------
# 19
# check the imput number is even or odd

value = input("Number 19: Enter a number to check even or odd: ")
print("Number 19:"," You have entered the value to check even or odd: ",value)
value = int(value)

if value%2 == 0:
    print("Number 19: ",'Input Number is even')
else:
    print("Number 19: ",'Input number is odd')

print()

# ----------------------------
# 20
name = input("Number 20: Enter your name: ")
print("Number 20: ","You have entered your name as: ",name)
age = input("Number 20: Enter your age in integer: ")
print("Number 20: ","You have entered your age as: ",age)
age = int(age)

turn90 =90-age
currentyear = 2020
yeartoturn90 = currentyear+turn90

print("Number 20: ",name," you will turn 90 in the year : ",yeartoturn90)

print()

# ----------------------------
# 21
# print this
# 1
# 12
# 123
# 1234
# 12345

print("Number 21: ")
for i in range(1,6):
    for j in range(0,i):
        print(j+1,end = '')
    print()









