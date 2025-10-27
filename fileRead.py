# Program: Read from one file and write a modified version to another

# Define file names
input_filename = "input.txt"
output_filename = "output_modified.txt"

try:
    # Open the input file for reading
    with open(input_filename, 'r', encoding='utf-8') as infile:
        # Read the entire content
        content = infile.read()
        
        # Modify the content (Example: convert to uppercase)
        modified_content = content.upper()
        
    # Write the modified content to a new file
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content)
    
    print(f"✅ Modified content successfully written to '{output_filename}'")

except FileNotFoundError:
    print(f"❌ Error: The file '{input_filename}' was not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
