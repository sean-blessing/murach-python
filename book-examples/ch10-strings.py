#p.277 using index value to access char of string
message = "There goes my hero. Watch him as he goes. He's ordinary!"
print(message)
print(f"message[:5]: {message[:5]}.")
print(f"message[6:10]: {message[6:10]}.")
print(f"message[42:]: {message[42:]}.")
print(f"message[:-1]: {message[:-1]}")

# repetition operator
print("=" * 20)

# triple quotes - multi line string
message_1 = '''This is an example of a multi line string. This is line 1.
This is line 2.
This is line 3.
'''
print(message_1)

#p. 279 Searching Strings
print('--- Searching Strings ---')
print(f"Gonna search this string: {message}")
print(f"'hero' in message?: {'hero' in message}")

print("If statement check from user input...")
#search_for = input("Word to search for: ")
search_for = "hero"
if search_for in message:
    print(f"Yes, '{search_for}' was found.")
else:
    print(f"No, '{search_for}' was not found.")
print(f"For loop through each char in {search_for}:")
for char in search_for:
    print(char)

# p.281 basic string methods
print("Basic String methods".center(25))
lower_string = "this is a string in all lower case letters"
print(lower_string)
print(f"Title version: {lower_string.title()}")
mixed_string = "abcd 1234 xyz"
print(mixed_string)
print(f"isalpha?: {mixed_string.isalpha()}")
print(f"isdigit?: {mixed_string.isdigit()}")
print(f"islower?: {mixed_string.islower()}")
print("there's a bunch of others!")

#p.283 find, replace, remove
phone_num = "513-645-7782"
print(f"Validate this phone #: {phone_num}")
# rules - must be 12 chars long, must be all digits except for 2 dashes
#       - dash in positions 3 and 7
length_check = len(phone_num)==12
def count_dashes(check_str):
    count = 0
    for char in check_str:
        if char=="-":
            count+=1
    return count
num_dashes = count_dashes(phone_num)
print(f"num_dashes = {num_dashes}")
num_dashes_ok = num_dashes == 2
print(f"num_dashes_ok: {num_dashes_ok}")
phone_remove_dashes = phone_num.replace("-","")
all_num = phone_remove_dashes.isdigit()
dash_positions = phone_num[3]=="-" and phone_num[7]=="-"
print(f"12 chars long?: {length_check}")
print(f"Dashes removed: {phone_remove_dashes}")
print(f"All nums?: {all_num}")
print(f"Dashes in right spots?: {dash_positions}")
valid_phone = length_check and all_num and dash_positions and num_dashes_ok
print(f"Valid phone #?: {valid_phone}")

#p.287 split strings
print("--- splitting strings ---")
print(f"String to split: {message}")
words = message.split()
print(f"num words: {len(words)}")
print(f"first word: words[0]: {words[0]}")
print(f"seventh word: words[6]: {words[6]}")
print(f"last word: words[-1]: {words[-1]}")
#print(f"12th word: words[12]: {words[12]}")

movie_csv_string = "Star Wars Episode IV: A New Hope,1976,PG"
movie_split = movie_csv_string.split(",")
print(f"Movie CSV String: {movie_csv_string}")
print(f"title = {movie_split[0]}")
print(f"year = {movie_split[1]}")
print(f"rating = {movie_split[2]}")

#p.289 joining strings
first_name = "Robert"
middle_name = "Nesta"
last_name = "Marley"

print(f"first_name: {first_name}")
print(f"middle_name: {middle_name}")
print(f"last_name: {last_name}")
print(f"full name: {last_name}, {first_name} {middle_name}")

print("-- joining list of names with | character --")
names_list = ["Bob","Jane","Gena","Tommy","Amy"]
print(names_list)
print(f"join: {'|'.join(names_list)}")

