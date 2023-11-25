x = float (input("What is X's?"))
y = float(input("What is y's?"))

# z = x + y;
# # Output (1+2) : 12  

# # int is a function and a data type also
# z = int(x) + int(y);

# # if you are going use a variable once in code so it is not necessary
# '''
# x = int(input("What is X's?"))
# y = int(input("What is y's?"))

# print(x + y)

# '''

# # Float 

z = round(x + y);

print(z);
print(f"{z:,}") 

# rounding up the number after decimal 

z = x / y;

# first method 
print(round(z,2))

# Second method is 
print(f"{z:.2f}");