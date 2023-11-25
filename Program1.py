# Ask user for the input  
name = input("What is your name : ");

# Remove Whitespace from string
name = name.strip(); 

# Capitalize user's name
name = name.capitalize();

# Capitalize Every first char in sentance 
name = name.title();

# Remove Whitespace from string and Capitalize user's name
# name = name.title().strip();


# Say hello to user
print(f"hello, {name}");

# Another way

# name = input("What is your name : ").strip().title();

# Split user name into first name and last name 
first, last = name.split(" ");
print(f"hello, {first}"); 
  