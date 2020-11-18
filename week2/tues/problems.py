ex = []
[ex.append([]) for y in range(0,10)]
[[ex[y].append(x) for x in range(y, 15)] for y in range(0, 10)]

[print(ex[x]) for x in range(0, len(ex))]


# ex is a 2d array containing numbers. Do the following:

# 1. print out the first element of each list in ex

# 2. print out the last element of ex in 2 different ways

# 3. remove the last item from each element in ex

# 4. print out the length of each element in ex

# 5. print only the second to last element in each list in ex

# 6. Use a list comprehension to generate a list of the first 10 cubes

# 7. Calculate the sum of the element in each list in ex
