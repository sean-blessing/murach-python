from dataclasses import dataclass

@dataclass
class Movie:
    title:str = ""
    year:int = 0
    rating:str = ""
    
    def details(self):
        return f"Movie: {self.title}({self.year}), Rated: {self.rating}"

def main():
    print("Welcome to the movie app")
    sw_movie = Movie("Star Wars Episode IV: A New Hope", 1976, "PG")
    print(sw_movie.details())
    
    
    print("bye")

if __name__ == "__main__":
    main()
