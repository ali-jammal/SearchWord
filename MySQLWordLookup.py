import pymysql
from difflib import get_close_matches

# Establishing a connection to the MySQL database
connection = pymysql.connect(
    host="localhost",
    password="Picture12",
    user="root",
    database="dictionary"
)

# Function to convert query results into a dictionary
def convert_to_dict(results):
    dictionary = {}
    for word, definition in results:
        dictionary.setdefault(word, []).append(definition)
    return dictionary

# Function to fetch word definitions
def define(word):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    
    # Converting query results to a dictionary format
    dictionary = convert_to_dict(results)

    if word in dictionary:
        return dictionary[word]
    elif word.upper() in dictionary:
        return dictionary[word.upper()]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif len(get_close_matches(word, dictionary.keys(), cutoff=0.8)) > 0:
        correction = input(f"Did you mean {get_close_matches(word, dictionary.keys(), cutoff=0.8)[0]} instead? Enter Y if yes, or N if no: ").upper()
        if correction == "Y":
            return dictionary[get_close_matches(word, dictionary.keys(), cutoff=0.8)[0]]
        elif correction == "N":
            return "Word does not exist. Please double check the word."
        else:
            return "We did not understand your entry."

# Function to continuously prompt for words until the user chooses to exit
def main():
    while True:
        word = input("Enter a word (or type 'exit' to quit): ")
        
        if word.lower() == 'exit':
            break
        
        definition = define(word)
        print(definition)
        print()  # Add a line break for better readability

# Run the main function to start the program
main()
