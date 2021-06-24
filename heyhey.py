# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def pass_50(item):
    return item > 50


print(list(filter(pass_50, scores)))
print(scores)
# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_list = [5, 4, 3]
new_list = list(map(lambda num: num ** 2, my_list))
print(new_list)
# list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
# dict comprehensions
my_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)


def my_decorator(func):
    def warp_func(*args, **kwargs):
        print('**************')
        func(*args, **kwargs)
        print('**************')

    return warp_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hi')

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    pass


while True:
    try:
        age = int(input('What is your age?'))
        10 / age
        #raise Exception('cut it out')

    except ValueError:
        print('Placse enter a number.')
    except ZeroDivisionError:
        print('Placse enter a age higher than 0.')
    else:
        print('Thank you!')
        break
    finally:
        print('oh finally I am done')


def sum(num1, num2):
    try:
        return num1/num2
    except TypeError as err:
        print(f'please type numbers.{err}')
    except(TypeError,ZeroDivisionError):
        print('oops')


print(sum(1, 0))
