# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(f"first: \n {x}")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(f"second: \n {x}")

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(f"third: \n {x}")

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(f"fourth: \n {x}")

# Print the length of list x
# YOUR CODE HERE

print(f"fourth: \n {len(x)}")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("five:")
for elem in x:
    print(f" {elem*1000}")