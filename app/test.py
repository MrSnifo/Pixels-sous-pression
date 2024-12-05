import os



print("Current directory files:")
print(os.listdir("."))  # This will list the files in the current working directory

# Print the files in the templates directory
print("\nFiles in 'templates' directory:")
print(os.listdir("app/templates"))  # Adjust this path if necessary

# Print the files in the static directory
print("\nFiles in 'static' directory:")
print(os.listdir("app/static"))  # Adjust this path if necessary