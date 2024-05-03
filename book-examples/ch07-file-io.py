# p.205 basic file operations
outfile_1 = open("test-1.txt", "w")
outfile_1.write("Test1")
outfile_1.close

with open("test-2.txt", "w") as outfile_2:
    outfile_2.write("Test2")

with open("test-2.txt", "r") as infile_2:
    print(infile_2.readline())

# p. 207 write vs append
with open("members.txt", "w") as members_file:
    members_file.write("John Cleese\n")

with open("members.txt", "a") as members_file:
    members_file.write("Eric Idle\n")

print('=====================================')
# p.209 reading from a file
# for statement to read each line of a file
with open("members.txt") as members_file:
    for line in members_file:
        print(line, end="")
    print()

# read whole file as a string
with open("members.txt") as members_file:
    contents = members_file.read()
    print(contents)

# p. 211 lists and files
foo_fighters = ["Dave Grohl", "Pat Smear", "Chris Shiflet", "Nate Mendel", "Josh Freese", "Rami Jaffee"]
with open("foo-fighters.txt", "w") as foo_fighters_file:
    for ff in foo_fighters:
        foo_fighters_file.write(f'{ff}\n')

ff_list = []
with open("foo-fighters.txt") as ff_file:
    for line in ff_file:
        ff_list.append(line.replace("\n", ""))
print(f'Foo Fighters List: {ff_list}')

# p.217 - csvs
print("=== csv processing of movies ===")
movies = [["Star Wars Episode IV: A New Hope", 1976],
          ["Sixteen Candles", 1984],
          ["Rogue One", 2016],
          ["Happy Gilmore", 1996],
          ["Wedding Crashers", 2005]
        ]
import csv

# write list to a csv
with open("movies.csv", "w", newline="") as movie_file:
    writer = csv.writer(movie_file)
    writer.writerows(movies)

#p.219 csv.reader()
with open("movies.csv", newline="") as movie_file:
    reader = csv.reader(movie_file)
    for row in reader:
        print(f"{row[0]} ({row[1]})")