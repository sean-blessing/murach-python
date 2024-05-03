try:
    whole_nbr = int(input("Enter a whole #: "))
    print(f"You entered {whole_nbr}")
except ValueError:
    print("You entered an invalid entry.")