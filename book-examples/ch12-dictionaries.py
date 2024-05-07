#p.329 creating dictionaries
seven_dwarfs_dict = {
    1: "Sleepy",
    2: "Sneezy",
    3: "Dopey",
    4: "Bashful",
    5: "Doc",
    6: "Grumpy",
    7: "Happy",
    8: "Test"
}
print(f"The 7 Dwarfs: {seven_dwarfs_dict}")

sw_movie = {
    "title": "Star Wars Episode IV: A New Hope",
    "year": 1976,
    "rating": "PG"
}
print(f"sw_movie: {sw_movie}")

jp_movie = {
    "title": "Jurassic Park",
    "year": 1993,
    "rating": "PG-13"
}

snwh_movie = {
    "title": "Spiderman: Homecoming",
    "year": 2017,
    "rating": "PG-13"
}

movies = {
    1: sw_movie,
    2: jp_movie,
    3: snwh_movie
}

print(f"Movies: {movies}")

#p.331 get/set values
print(f"dwarf w/ key 2: {seven_dwarfs_dict[2]}")

#p.333 del an item
dwarf_nbr = 8

if dwarf_nbr in seven_dwarfs_dict:
    dwarf = seven_dwarfs_dict[dwarf_nbr]
    del seven_dwarfs_dict[dwarf_nbr]
    print(f"{dwarf} deleted")
print(f"dwarfs after delete: {seven_dwarfs_dict}")

# pop method works too:
dwarf = seven_dwarfs_dict.pop(5)
print(f"{dwarf} deleted")
print(f"dwarfs after delete: {seven_dwarfs_dict}")

# re-add 5 - Doc
seven_dwarfs_dict[5] = "Doc"
print(f"dwarfs after re-add doc: {seven_dwarfs_dict}")

#p.335 looping through dictionary
print("looping through all keys and values - seven dwarfs")
for nbr in seven_dwarfs_dict.keys():
    print(f"{nbr}: {seven_dwarfs_dict[nbr]}")

print("looping through all tuple - seven dwarfs")
for nbr, dwarf in seven_dwarfs_dict.items():
    print(f"{nbr}: {seven_dwarfs_dict[nbr]}")

print("looping through all values - seven dwarfs")
for name in seven_dwarfs_dict.values():
    print(f"{name}")

#p. 337 - converting between list and dict (why would we do this?)

#p. 345 - merge and update dictionaries
# once again, why would we do this? I think it has to do with data cleaning,
# or in web scraping. Would be good to mention here, for perspective.

#p.347 - dictionaries w/ complex objects
