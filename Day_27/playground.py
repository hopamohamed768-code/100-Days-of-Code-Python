def add(*args):
    sum = 0
    for n in args:
       sum += n
    return sum
        
print(add(1, 7, 8, 3, 5))