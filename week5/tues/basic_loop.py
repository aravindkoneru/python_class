numbers = [1,2,3,4,5,6,7,8,9]
ex = [numbers, numbers, numbers, numbers]

#total = 0
#for x in numbers:
#    print(f"total at start of iteration: {total}")
#    print(f"value of x: {x}")
#    total = total + x
#    print(f"total at end of iteration: {total}\n")
#
#print(total)

# ex is a 2d list
for x in ex:
    # x is a list
    print(x)
    total = 0
    for e in x:
        print(f"total at start of iteration: {total}")
        print(f"value of e: {e}")
        total = total + e
        print(f"total at end of iteration: {total}\n")
    print(total)
    print("\n")




