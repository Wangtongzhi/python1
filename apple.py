def func(a, b):
    def line(x):
        return a * x - b
    return line
line = func(2,3)
print(line(5))
print(id(line))