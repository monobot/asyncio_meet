def my_generator(num):
    while num > 0:
        yield num
        num -= 1


for pos in my_generator(9):
    print(pos)
