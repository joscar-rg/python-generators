def square(stop):
    for num in range(1, stop):
        yield (num ** 2)


result = square(10)
print(list(result))