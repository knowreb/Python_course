print("3.4")
visitors = ['Mary', 'Jane', 'Roma', 'Adrian']
print(f'I would like to cordially invite to lunch {visitors[0]}')
print(f'I would like to cordially invite to lunch {visitors[1]}')
print(f'I would like to cordially invite to lunch {visitors[2]}')
print(f'I would like to cordially invite to lunch {visitors[3]}')

print("3.5")

visitors = ['Mary', 'Jane', 'Roma', 'Adrian']

print(f'I would like to cordially invite to lunch {visitors[0]}')
print(f'I would like to cordially invite to lunch {visitors[1]}')
print(f'I would like to cordially invite to lunch {visitors[2]}')
print(f'I would like to cordially invite to lunch {visitors[3]}')

print(f'\nUnfortunately, Roma cannot come to lunch')
unable_come = 'Roma'
visitors.remove(unable_come)
print(visitors)
visitors.append('Bruno')
print(visitors)
print(f'I would like to cordially invite to lunch {visitors[0]}')
print(f'I would like to cordially invite to lunch {visitors[1]}')
print(f'I would like to cordially invite to lunch {visitors[2]}')
print(f'I would like to cordially invite to lunch {visitors[3]}')

print("3.6")
print('\nFinding a bigger table!')

visitors = ['Mary', 'Jane', 'Roma', 'Adrian']
visitors.insert(0, 'Bruno')
print(visitors)
visitors.insert(3,'Sophia')
print(visitors)
visitors.append('Layla')
print(visitors)
print(f'I would like to cordially invite to lunch {visitors[0]}')
print(f'I would like to cordially invite to lunch {visitors[1]}')
print(f'I would like to cordially invite to lunch {visitors[2]}')
print(f'I would like to cordially invite to lunch {visitors[3]}')
print(f'I would like to cordially invite to lunch {visitors[4]}')
print(f'I would like to cordially invite to lunch {visitors[5]}')
print(f'I would like to cordially invite to lunch {visitors[6]}')

print("3.7")
print("\nI'm sorry, unfortunately I can invite only two friend😭")
print(visitors)

popped_visitors = visitors.pop(0)
print(visitors)
print(f'\nSee you soon {popped_visitors}!')

popped_visitors = visitors.pop(1)
print(visitors)
print(f'\nSee you soon {popped_visitors}!')

popped_visitors = visitors.pop(2)
print(visitors)
print(f'\nSee you soon {popped_visitors}!')

popped_visitors = visitors.pop(3)
print(visitors)
print(f'\nSee you soon {popped_visitors}!')

popped_visitors = visitors.pop(2)
print(visitors)
print(f'\nSee you soon {popped_visitors}!')

print(f'\nCordially invite you {visitors [0]} to lunch!')
print(f'\nCordially invite you {visitors [1]} to lunch!')

del visitors [0]
del visitors [0]
print(visitors)




