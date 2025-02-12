# Accept a list of 8 numbers from user. 
# Sort the list without using built-in function, without creating any extra list.

# number = int(input("Enter any number : "))
n = 8
list1 = []

for i in range(n):
    val = input(f"Enter any number {i + 1} : ")
    list1.append(val)
print(list1[::-1])
# rev_list = list1[::-1]
# print(rev_list)
