#def square(num):
#    my_list = []
#    for n in range(1, num):
#        my_list.append(n ** 2)
#    return my_list

my_list = (num ** 2 for num in range(1,10))


print(my_list)

# convert type
# print(list(my_list))
print(set((num ** 2 for num in range(1,10))))
print(tuple((num ** 2 for num in range(1,10))))

# loop
for num in (num ** 2 for num in range(1,10)):
    print(num)

# next
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
