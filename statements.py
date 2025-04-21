my_lists=['apple','cherry','lemon']
my_dict={"drinks":"coffee","milk":"whole"}

for item in my_lists:
    print(f'My favorite food to eat is {item}')

for _,value in my_dict.items():
    print(f'My favorite food to drink is {value}')

print(my_dict)