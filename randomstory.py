import random
# Function to get user-defined inputs for story elements
def get_user_inputs(prompt):
    items = []
    print(prompt)
    while True:
        item = input("Enter (or type 'done' to finish): ")
        if item.lower() == 'done':  # Stop input when user types 'done'
            break
        items.append(item)
    return items
# Function to generate the random story
def generate_story(characters, places, actions, objects):
    character = random.choice(characters)  # Randomly select a character
    place = random.choice(places)          # Randomly select a place
    action = random.choice(actions)        # Randomly select an action
    obj = random.choice(objects)           # Randomly select an object
    # Forming the story with the randomly chosen elements
    story = f"Once upon a time, {character} {place} {action} with the help of {obj}."
    return story
# Main Program: Getting user inputs and generating the story
def main():
    print("Welcome to the Random Story Generator!\n")
    # Prompting the user to enter characters, places, actions, and objects
    characters = get_user_inputs("Please enter characters:")
    places = get_user_inputs("Please enter places:")
    actions = get_user_inputs("Please enter actions:")
    objects = get_user_inputs("Please enter objects:")

    # Ensuring that the user has entered at least one item in each category
    if characters and places and actions and objects:
        # Generate and display the random story
        print("\nYour randomly generated story is:")
        print(generate_story(characters, places, actions, objects))
    else:
        print("You need to provide at least one item in each category!")
# Running the main function to execute the program
if __name__ == "__main__":
    main()
