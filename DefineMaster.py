import json
from difflib import get_close_matches

# Load the dictionary data from a JSON file
data = json.load(open("data.json", 'r'))

# Function to find the definition of a word
def find_definition(word):
    word = word.lower()  # Convert the input word to lowercase for consistent comparison
    
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        # Finding close matches to suggest possible correct words
        matches = get_close_matches(word, data.keys(), cutoff=0.8)
        
        if matches:
            correction = input(f"Did you mean {matches[0]} instead? Enter Y if yes, or N if no: ").upper()
            
            if correction == "Y":
                return data[matches[0]]
            elif correction == "N":
                return "Word does not exist. Please double check the word."
            else:
                return "We did not understand your entry."
        else:
            return "Word not found. Please double check the word."

# Function to interact with the user and display word definitions
def main():
    while True:
        word = input("Enter a word (or type 'exit' to quit): ")
        
        if word.lower() == 'exit':
            break
        
        definition = find_definition(word)
        
        if isinstance(definition, list):
            for item in definition:
                print(item)
        else:
            print(definition)
        print()  # Add a line break for better readability

main()
