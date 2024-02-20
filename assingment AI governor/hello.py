# Q2) Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”#

person_name ="Eric"
print(f"Hello {person_name}, would you like to learn some Python today?")


#Q3) Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.#

person_name = "Syed Ali Azhar"

print("Lowercase:", person_name.lower())

print("Uppercase:", person_name.upper())

print("Titlecase:", person_name.title())

 #Q4) Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
 # Albert Einstein once said, “A person who never made a mistake never tried anything new.”#

author ="Amir khan once said,"
quote ="All is well"

print(f"{author}"f"'{quote}'")


# Q5) Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.


famous_person ="mudassir"


print(f"{famous_person} was a very nice man")


# Q6) Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name after striping the white spaces.



name ="\t\n john doe \n\t"
print("Name with whitespace around it:")
print(name)

stripped_name = name.strip()
print("\nName after stripping the whitespace:")
print(stripped_name)


# Q7)  Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results.

print("Addition operation:", 5 + 3 )

print("Subtraction operation:", 12 - 4)

print("Multiplication operation:", 4 * 2)

print("Division operation:", 64 / 8)


# Q9)  Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.


favourite_number ="4"
print(f"My favourite number is {favourite_number}")


# Q10)  Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.


# Program Name: Rectangle Area Calculator
# Author: OpenAI Assistant
# Date: February 16, 2024


# Define the dimensions of the rectangle
length = 5
width = 4

# Calculate the area of the rectangle
area =length * width

# Print the result
print(f"The area of rectangle is:" ,area)


# Q11) Store the names of a few of your friends in a array called names. Print each person’s name by accessing each element in the list, one at a time.

names =["Talib","safi","fahad","umer","ahmed"]

for name in names:

  print(name)


  # Q12) Start with the array you used in Exercise 11, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

  names =["bilal","yahya","abdulah"]

  for name in names:
    print(f"Hello {name}, I hope you're having a great day")


    # Q13) Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”


    transportation_modes =["car","motorcycle","bugatti","corolla"]

    for mode in transportation_modes:
     print(f"I would like to own a {mode}.")

     # Q14) If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

         # Define a function to create invitations
def create_invitation(guest):
    return f"Dear {guest},\n\nI would be honored if you could join me for dinner. Your presence would make the evening truly special.\n\nBest regards,\n[Syed ali azhar]"

# List of guests
guests = ["arham", "maya", "khalid"]

# Send invitations
for guest in guests:
    invitation = create_invitation(guest)
    print(invitation)
    print("\n---\n")



# Q15)  You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

#• Start with your program from Exercise 14. Add a print statement at the end of your program stating the name of the guest who can’t make it.

#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#• Print a second set of invitation messages, one for each person who is still in your list.


# Define a function to create invitations
def create_invitation(guest):
    return f"Dear {guest},\n\nI would be honored if you could join me for dinner. Your presence would make the evening truly special.\n\nBest regards,\n[Your Name]"

# List of guests
guests = ["Albert Einstein", "Maya Angelou", "Leonardo da Vinci"]

# Print the guest who can't make it
guest_cant_make_it = guests.pop(1)  # Removing the guest who can't make it
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
new_guest = "Marie Curie"
guests.append(new_guest)

# Send invitations to the updated guest list
print("Sending new invitations:\n")
for guest in guests:
    invitation = create_invitation(guest)
    print(invitation)
    print("\n---\n")



# Q16) You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 15. Add a print statement to the end of your program informing people that you found a bigger dinner table.

#• Add one new guest to the beginning of your array.

#• Add one new guest to the middle of your array. • Use append() to add one new guest to the end of your list. • Print a new set of invitation messages, one for each person in your list.


# Define a function to create invitations
def create_invitation(guest):
    return f"Dear {guest},\n\nI would be honored if you could join me for dinner. Your presence would make the evening truly special.\n\nBest regards,\n[Your Name]"

# List of guests
guests = ["Albert Einstein", "Maya Angelou", "Leonardo da Vinci"]

# Print the guest who can't make it
guest_cant_make_it = guests.pop(1)  # Removing the guest who can't make it
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
new_guest = "Marie Curie"
guests.append(new_guest)

# Inform about the bigger dinner table
print("Good news! We've found a bigger dinner table. More guests are invited!\n")

# Add one new guest to the beginning of the array
guests.insert(0, "Nelson Mandela")

# Add one new guest to the middle of the array
guests.insert(len(guests) // 2, "Ada Lovelace")

# Add one new guest to the end of the array using append()
guests.append("Stephen Hawking")

# Send invitations to the updated guest list
print("Sending new invitations:\n")
for guest in guests:
    invitation = create_invitation(guest)
    print(invitation)
    print("\n---\n")


# Q17) # Define a function to create invitations
def create_invitation(guest):
    return f"Dear {guest},\n\nI would be honored if you could join me for dinner. Your presence would make the evening truly special.\n\nBest regards,\n[Your Name]"

# List of guests
guests = ["Albert Einstein", "Maya Angelou", "Leonardo da Vinci", "Marie Curie", "Nelson Mandela", "Ada Lovelace", "Stephen Hawking"]

# Print a message saying only two people can be invited
print("Unfortunately, the new dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, we won't be able to invite you to dinner.")

# Print messages to the two remaining guests
print(f"\n{guests[0]}, you're still invited to dinner. Thank you for understanding.")
print(f"{guests[1]}, you're still invited to dinner. Thank you for understanding.\n")

# Remove the last two names from the list
guests.clear()

# Print the list to ensure it's empty
print("Remaining guest list:", guests)



# Q18) Think of at least five places in the world you’d like to visit.
#• Store the locations in a array. Make sure the array is not in alphabetical order.

#• Print your array in its original order.

#• Print your array in alphabetical order without modifying the actual list.

#• Show that your array is still in its original order by printing it.

#• Print your array in reverse alphabetical order without changing the order of the original list.

#• Show that your array is still in its original order by printing it again.

#• Reverse the order of your list. Print the array to show that its order has changed.

#• Reverse the order of your list again. Print the list to show it’s back to its original order.

#• Sort your array so it’s stored in alphabetical order. Print the array to show that its order has been changed.

#• Sort to change your array so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.



# List of places to visit
places_to_visit = ["Tokyo", "Machu Picchu", "Santorini", "Great Barrier Reef", "Grand Canyon"]

# Print the original order
print("Original Order:")
print(places_to_visit)

# Print alphabetical order without modifying the original list
print("\nAlphabetical Order:")
print(sorted(places_to_visit))

# Show that the original order is unchanged
print("\nOriginal Order (unchanged):")
print(places_to_visit)

# Print reverse alphabetical order without modifying the original list
print("\nReverse Alphabetical Order:")
print(sorted(places_to_visit, reverse=True))

# Show that the original order is still unchanged
print("\nOriginal Order (unchanged):")
print(places_to_visit)

# Reverse the order of the list
places_to_visit.reverse()
print("\nReversed Order:")
print(places_to_visit)

# Reverse the order again to get back to the original order
places_to_visit.reverse()
print("\nOriginal Order (reversed again):")
print(places_to_visit)

# Sort the list in alphabetical order
places_to_visit.sort()
print("\nSorted in Alphabetical Order:")
print(places_to_visit)

# Sort the list in reverse alphabetical order
places_to_visit.sort(reverse=True)
print("\nSorted in Reverse Alphabetical Order:")
print(places_to_visit)



# Q19) Working with one of the programs from Exercises 14 through 18, print a message indicating the number of people you are inviting to dinner.


# List of guests
guests = ["Albert Einstein", "Maya Angelou", "Leonardo da Vinci", "Marie Curie", "Nelson Mandela", "Ada Lovelace", "Stephen Hawking"]

# Print the number of people invited to dinner
print(f"We are inviting {len(guests)} people to dinner.")


# Q20) For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items.

# List of countries
countries = ["United States", "Canada", "Brazil", "India", "China", "France", "Germany", "Australia", "Japan", "South Africa"]

# Print the list of countries
print("List of countries:")
for country in countries:
    print(country)




    
#Q31) No Users: Add an if test to Exercise 28 to make sure the list of users is not empty.

# • If the list is empty, print the message We need to find some users!

# • Remove all of the usernames from your array, and make sure the correct message is printed.


users = []

if users:
    for user in users:
        print("Hello admin, would you like to see a status report?" if user == 'admin' else "Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")



# Q32) Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.

#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.

#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.

#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.


# Defining current_users and new_users lists:

current_users = ['john', 'mary', 'alice', 'bob', 'sam']
new_users = ['John', 'sarah', 'Mike', 'bob', 'emily']


# Converting current_users to lowercase:

current_users_lower = [user.lower() for user in current_users]


# Looping through new_users to check for uniqueness:


for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is not available. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")


# Q33) Ordinal Numbers: Ordinal numbers indicate their position in a array, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

#• Store the numbers 1 through 9 in a array.

#• Loop through the array.

#• Use an if-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.


numbers = list(range(1, 10))  # Store numbers 1 through 9 in an array

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


 # Q34) Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a array, and then use a for loop to print the name of each pizza.

#• Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.

#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!


# Define an array of favorite pizza names
favorite_pizzas = ['Margherita', 'Pepperoni', 'BBQ Chicken']

# Print the name of each pizza using a for loop
print("Printing pizza names:")
for pizza in favorite_pizzas:
    print(pizza)

# Modify the loop to print a sentence about each pizza
print("\nPrinting sentences about favorite pizzas:")
for pizza in favorite_pizzas:
    print("I like " + pizza + " pizza.")

# Print an additional sentence expressing love for pizza
print("\nI really love pizza!")



# Q35) Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal. • Modify your program to print a statement about each animal, such as A dog would make a great pet. • Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!


# Define a list of animals with a common characteristic
animals = ['dog', 'cat', 'rabbit']

# Print the name of each animal using a for loop
print("Printing animal names:")
for animal in animals:
    print(animal)

# Modify the loop to print a statement about each animal
print("\nPrinting statements about animals:")
for animal in animals:
    print("A " + animal + " would make a great pet.")

# Print a statement about the common characteristic
print("\nAny of these animals would make a great pet!")


# Q36) T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function.



def make_shirt(size, message):
    print(f"A {size} shirt will be printed with the following message: '{message}'.")

# Calling the function
make_shirt("medium", "Python is awesome!")




# Q37) Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love TypeScript. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



def make_shirt(size='large', message='I love TypeScript'):
    print(f"Creating a {size} shirt with the message: {message}")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size='medium')

# Making a shirt of any size with a different message
make_shirt(size='small', message='Python is awesome!')



# Q38) Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Karachi is in Pakistan. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.


def describe_city(city, country='Pakistan'):
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city('Karachi')
describe_city('Lahore')
describe_city('New York', 'USA')



# Q39) City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:

#"Lahore, Pakistan"

#Call your function with at least three city-country pairs, and print the value that’s returned.


def city_country(city, country):
    return f"{city}, {country}"

# Call the function with at least three city-country pairs and print the returned value
print(city_country("Lahore", "Pakistan"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))



#Q40) Album: Write a function called make_album() that builds a Object describing a music album. The function should take in an artist name and an album title, and it should return a Object containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that Objects are storing the album information correctly. Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s Object. Make at least one new function call that includes the number of tracks on an album.


def make_album(artist_name, album_title, num_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album

# Creating three dictionaries representing different albums
album1 = make_album('Artist 1', 'Album 1')
album2 = make_album('Artist 2', 'Album 2', 12)  # Including number of tracks
album3 = make_album('Artist 3', 'Album 3')

# Printing each return value to show the album information
print(album1)
print(album2)
print(album3)



# Q41) Magicians: Make a array of magician’s names. Pass the array to a function called show_magicians(), which prints the name of each magician in the array.


def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magician_names = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']

show_magicians(magician_names)


# Q42) Great Magicians: Start with a copy of your program from Exercise 39. Write a function called make_great() that modifies the array of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.


def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

magician_names = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']

make_great(magician_names)
show_magicians(magician_names)



# Q43) Unchanged Magicians: Start with your work from Exercise 40. Call the function make_great() with a copy of the array of magicians’ names. Because the original array will be unchanged, return the new array and store it in a separate array. Call show_magicians() with each array to show that you have one array of the original names and one array with the Great added to each magician’s name.


def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []  # Create a new empty list to store modified names
    for magician in magicians:
        great_magicians.append("the Great " + magician)  # Append modified names to the new list
    return great_magicians  # Return the new list

magician_names = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']

great_magician_names = make_great(magician_names[:])  # Pass a copy of the original array
show_magicians(magician_names)
show_magicians(great_magician_names)



# Q44) Sandwiches: Write a function that accepts a array of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.


def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)

# Call the function three times with different numbers of arguments
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese')
make_sandwich('peanut butter', 'jelly')



# Q45) Cars: Write a function that stores information about a car in a Object. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Print the Object that’s returned to make sure all the information was stored correctly.


def car_info(manufacturer, model, **kwargs):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(kwargs)  # Update the dictionary with additional keyword arguments
    return car

# Call the function with required information and additional name-value pairs
car_details = car_info('Toyota', 'Corolla', color='blue', year=2022)

# Print the dictionary to verify the information stored correctly
print(car_details)
