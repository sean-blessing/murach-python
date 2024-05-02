print("Registration Form\n")

first_name = input("First name:    ")
last_name = input("Last name:     ")
birth_year = input("Birth year:    ")

full_name = f'{first_name} {last_name}'
temp_pwd = f'{first_name}*{birth_year}'

print(f'Welcome {full_name}!')
print('Your registration is complete.')
print(f'Your temporary password is: {temp_pwd}')

print("Bye")
