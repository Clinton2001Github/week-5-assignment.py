def read_and_modify_file():
    try:
        # Prompt user for the filename to read
        input_filename = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modify content (e.g., add line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        # Prompt for the output file name
        output_filename = input("Enter the name of the file to write the modified content: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except IOError as e:
        print(f"Error: Could not read or write to file. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
