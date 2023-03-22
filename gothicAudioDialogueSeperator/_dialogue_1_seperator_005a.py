import os
import re

def modify_text(text):
    # Remove everything before the first "
    text = text.split('"', 1)[1]
    # Replace the ");   " at the end with ".wav|"
    text = text.replace('");\t//', '.wav|')
    # Add the preceding audio filename
    audio_filename = text.split('.wav|', 1)[0] + '.wav'
    text = audio_filename + '|' + text.split('.wav|', 1)[1]
    return text


def process_files():
    # Get all files in the current directory with the ".d" extension
    files = [file for file in os.listdir('.') if file.endswith('.d')]
    
    # Process each file
    for filename in files:
        with open(filename, 'r') as input_file:
            for line in input_file:
                match = re.search(r'^\s*(AI_Output.*)$', line)
                if match:
                    output_filename = f"output_{os.path.splitext(filename)[0]}.txt"
                    with open(output_filename, 'a') as output_file:
                        modified_text = modify_text(match.group(1))
                        output_file.write(modified_text + '\n')
                        print(f"Line saved to {output_filename}: {modified_text}")
        print(f"Output saved to {output_filename}")


process_files()
