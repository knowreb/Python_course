print('4.3')
for number in range(1,21):
    print(number)

print('\n4.4')
# for number in range(1,1000000):
#     print(number)

print('\n4.5')
# numbers = list(range(1,1000001))
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

print('\n4.6')
for number in range(1,21,2):
    print(number)

print('\n4.7')
threes = []
for value in range(3,31):
    three = value**3
    threes.append(three)

print(threes)

print('\n4.8')
cubes = []
for number in range(1,11):
    cubes.append(number**3)
for cube in cubes:
    print(cube)

print('\n4.9')
cube = [number**3 for number in range(1,11)]
print(cube)