import sqlite3

# Function to create the SQLite database and table
def create_database_and_table():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
        movieID TEXT PRIMARY KEY,
        movieName TEXT,
        movieYear INTEGER,
        imdbRating REAL
    )
    ''')
    
    conn.commit()
    conn.close()

# Function to read data from file and insert into the database
def read_file_and_insert_data():
    stephen_king_adaptations_list = []
    with open('stephen_king_adaptations.txt', 'r') as file:
        for line in file:
            movie_data = line.strip().split(',')
            stephen_king_adaptations_list.append(tuple(movie_data))
    
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()
    
    cursor.executemany('INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)', stephen_king_adaptations_list)
    
    conn.commit()
    conn.close()

# Function to search for movies based on user's choice
def search_movies():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()
    
    while True:
        print("\nSearch Options:")
        print("1. Movie name")
        print("2. Movie year")
        print("3. Movie rating")
        print("4. STOP")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            movie_name = input("Enter the name of the movie: ")
            cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?', (movie_name,))
            result = cursor.fetchone()
            if result:
                print("Movie Found:")
                print("Movie ID:", result[0])
                print("Movie Name:", result[1])
                print("Movie Year:", result[2])
                print("IMDB Rating:", result[3])
            else:
                print("No such movie exists in our database.")
        
        elif choice == '2':
            movie_year = int(input("Enter the year: "))
            cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?', (movie_year,))
            results = cursor.fetchall()
            if results:
                print("Movies Found for Year", movie_year, ":")
                for row in results:
                    print("Movie ID:", row[0])
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No movies were found for that year in our database.")
        
        elif choice == '3':
            rating_limit = float(input("Enter the minimum rating: "))
            cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?', (rating_limit,))
            results = cursor.fetchall()
            if results:
                print("Movies with Rating at or above", rating_limit, ":")
                for row in results:
                    print("Movie ID:", row[0])
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No movies at or above that rating were found in the database.")
        
        elif choice == '4':
            break
    
    conn.close()

# Main function
if __name__ == "__main__":
    create_database_and_table()
    read_file_and_insert_data()
    search_movies()
