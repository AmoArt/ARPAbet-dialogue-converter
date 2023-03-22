import os
import re

def extract_audio_files():
    # Get all files in the current directory that start with "output2_"
    files = os.listdir('.')
    output_files = [file for file in files if file.startswith('output2_') and file.endswith('.txt')]
    
    # Process each output file
    for output_file in output_files:
        # Generate the new filename for the audio file
        input_filename = output_file.split('_', 2)[2].rsplit('.', 1)[0]
        audio_file = f"audiofiles_{input_filename}.txt"
        
        # Open the input and output files
        with open(output_file, 'r') as input_file, open(audio_file, 'w') as output:
            # Read each line, remove everything after the "|" and write it to the output file
            for line in input_file:
                line = re.sub(r'\|.*?$', '', line)
                output.write(line)

        # Remove the extra newline character at the end of the output files
        with open(audio_file, 'rb+') as output:
            output.seek(-1, os.SEEK_END)
            if output.read(1) == b'\n':
                output.seek(-1, os.SEEK_END)
                output.truncate()

        print(f"All lines saved to {audio_file}")
        output.close()

extract_audio_files()
