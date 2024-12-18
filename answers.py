# File Read & Write Challenge
# This program reads a file and writes a modified version to a new file

def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been successfully modified and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to read or write file. Details: {e}")


# Error Handling Lab
# Ask the user for a filename and handle errors
if __name__ == "__main__":
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified content: ")

    read_and_write_file(input_filename, output_filename)