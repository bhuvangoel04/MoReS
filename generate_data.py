import numpy as np
import pandas as pd
import random

def generate_100k_dataset(output_csv="final_100k_movies_webseries.csv", number_of_records=100_000):
    """
    Creates a synthetic CSV file with <number_of_records> rows of data
    that includes the columns needed for your recommendation system:
      - title
      - Type (Movie or Webseries)
      - Year
      - genres
      - keywords
      - tagline
      - cast
      - director
      - Country
      - index (auto-assigned row number)

    With expanded lists to reduce repetition.
    """

    movie_titles = [
        "The Shawshank Redemption","The Godfather","Pulp Fiction","Fight Club","Inception","The Dark Knight",
        "Forrest Gump","Parasite","Interstellar","Schindler's List","The Matrix","Goodfellas","Se7en","Gladiator",
        "Titanic","Avatar","Braveheart","Saving Private Ryan","Avengers: Endgame","La La Land","Joker","Black Panther",
        "WALL-E","Up","Toy Story","Spirited Away","Amélie","City of God","Whiplash","The Prestige","Memento","Django Unchained",
        "The Lion King","The Silence of the Lambs","Jurassic Park","Terminator 2: Judgment Day","The Green Mile","Back to the Future",
        "Casablanca","Star Wars","The Pianist","12 Angry Men","Once Upon a Time in the West","Alien","Psycho","The Departed",
        "The Usual Suspects","Indiana Jones and the Last Crusade","Die Hard","Raiders of the Lost Ark","The Great Dictator",
        "Cinema Paradiso","Slumdog Millionaire","Inglourious Basterds","1917","Shutter Island","The Wolf of Wall Street","Gone Girl"
    ]

    webseries_titles = [
        "Breaking Bad","Game of Thrones","Stranger Things","The Crown","Friends","Sherlock","Money Heist","Dark",
        "The Mandalorian","The Witcher","House of Cards","Westworld","Narcos","The Handmaid's Tale","Peaky Blinders",
        "Better Call Saul","The Boys","Chernobyl","Ozark","The Office","Brooklyn Nine-Nine","Modern Family","Vikings",
        "Black Mirror","Succession","Lucifer","Fargo","Dexter","The Big Bang Theory","Homeland","Prison Break",
        "True Detective","Lost","Mr. Robot","Hannibal","Cobra Kai","Invincible","Band of Brothers","Ted Lasso","Arcane"
    ]

    genres_list = [
        "Drama","Crime","Thriller","Action","Romance","Comedy","Sci-Fi","Fantasy","Mystery","Horror",
        "Adventure","Animation","Biography","Family","Musical","War","Superhero"
    ]

    keywords_list = [
        "revenge","love","betrayal","hero","villain","friendship","war","magic","time-travel","epic",
        "survival","espionage","heist","dystopian","robots","zombies","murder","coming-of-age","conspiracy","courtroom",
        "gangster","space","multiverse","pirates","historical","martial-arts","alien","apocalypse","cyberpunk","disaster"
    ]

    tagline_list = [
        "An unexpected journey.","A battle of wills.","Destiny awaits.","Nothing is what it seems.","Love conquers all.",
        "The world will tremble.","A mind-bending adventure.","Truth lies within.","Beyond the horizon.","Two worlds collide.",
        "A race against time.","Unleash your imagination.","The legend begins.","Where heroes are born.",
        "One secret can change everything."
    ]

    cast_list = [
        "Leonardo DiCaprio","Morgan Freeman","Brad Pitt","Tom Hanks","Scarlett Johansson","Natalie Portman","Johnny Depp",
        "Kate Winslet","Al Pacino","Keanu Reeves","Marlon Brando","Christian Bale","Heath Ledger","Benedict Cumberbatch",
        "Emilia Clarke","Aaron Paul","Bryan Cranston","Pedro Pascal","Henry Cavill","Jennifer Aniston","Courteney Cox",
        "Matthew Perry","Matt Damon","Julia Roberts","Angelina Jolie","Samuel L. Jackson","Robert Downey Jr.","Chris Evans",
        "Chris Hemsworth","Gal Gadot","Ryan Reynolds","Denzel Washington","Will Smith","Anne Hathaway","Jessica Chastain",
        "Harrison Ford","Keira Knightley","Ian McKellen","Patrick Stewart","Emma Stone","Amy Adams","Bruce Willis",
        "Zoe Saldana","Tom Holland","Zac Efron","Joaquin Phoenix"
    ]

    director_list = [
        "Christopher Nolan","Steven Spielberg","Quentin Tarantino","Martin Scorsese","David Fincher","James Cameron",
        "Francis Ford Coppola","Tim Burton","Ridley Scott","Denis Villeneuve","Alfred Hitchcock","Bong Joon Ho",
        "Coen Brothers","Peter Jackson","Guy Ritchie","Michael Bay","Clint Eastwood","Alejandro G. Inarritu","Kathryn Bigelow",
        "Taika Waititi","Wes Anderson","Robert Zemeckis","Stanley Kubrick","Ron Howard","George Lucas","J.J. Abrams",
        "Gore Verbinski","Sam Mendes","Anthony & Joe Russo"
    ]

    countries = [
        "USA","India","China","Japan","France","UK","Germany","Italy","Spain","Korea","Russia","Brazil","Australia",
        "Canada","Mexico","New Zealand","Sweden","Denmark","South Africa","Argentina"
    ]
    data_rows = []
    for idx in range(number_of_records):
        content_type = random.choice(["Movie", "Webseries"])

        if content_type == "Movie":
            title = random.choice(movie_titles)
        else:
            title = random.choice(webseries_titles)

        if content_type == "Movie":
            year_val = str(random.randint(1960, 2023))
        else:
            start_year = random.randint(2000, 2023)
            if random.random() < 0.5:
                end_year = random.randint(start_year, 2023)
                year_val = f"{start_year}–{end_year}"
            else:
                year_val = f"{start_year}–Present"
        
        num_genres = random.randint(1,2)
        chosen_genres = random.sample(genres_list, num_genres)
        genres_str = ", ".join(chosen_genres)

        num_keywords = random.randint(1,3)
        chosen_keywords = random.sample(keywords_list, num_keywords)
        keywords_str = ", ".join(chosen_keywords)

        tagline_str = random.choice(tagline_list)

        chosen_cast = random.sample(cast_list, k=random.choice([2, 3]))
        cast_str = ", ".join(chosen_cast)
        
        director_str = random.choice(director_list)
        country_str = random.choice(countries)
        
        row_dict = {
            "title": title,
            "Type": content_type,
            "Year": year_val,
            "genres": genres_str,
            "keywords": keywords_str,
            "tagline": tagline_str,
            "cast": cast_str,
            "director": director_str,
            "Country": country_str,
            "index": idx 
        }
        
        data_rows.append(row_dict)

    df = pd.DataFrame(data_rows)
    df.to_csv(output_csv, index=False)
    print(f"Generated '{output_csv}' with {number_of_records:,} rows.")

if __name__ == "__main__":
    generate_100k_dataset()
