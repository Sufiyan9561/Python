#Function to create an acronym from an input string
def generate_acronym(phrase):
    words = phrase.split()  # Split the input string into words
    acronym = ""
    for word in words:
        acronym += word[0].upper()  # Take the first letter of each word and convert it to uppercase
    return acronym
#Main program
def main():
    print("Welcome to the Acronym Generator!")
    input_string = input("Enter a phrase or sentence to generate an acronym: ")
    # Generate the acronym
    acronym = generate_acronym(input_string)
    # Output the result
    print(f"The acronym for '{input_string}' is: {acronym}")
#Run the main program
if __name__ == "__main__":
    main()
