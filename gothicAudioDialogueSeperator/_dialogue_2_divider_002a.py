import os

def process_files():
    # Get all files in the current directory
    files = os.listdir('.')
    
    # Look for files that start with "output_"
    output_files = [file for file in files if file.startswith('output_') and file.endswith('.txt')]
    
    # Process each output file
    for output_file in output_files:
        # Generate the new output filenames
        input_filename = output_file.split('_', 1)[1].rsplit('.', 1)[0]
        pc_output_file = f"output2_{input_filename}_div_PC.txt"
        npc_output_file = f"output2_{input_filename}_div_NPC.txt"
        
        # Open the input and output files
        with open(output_file, 'r') as input_file, open(pc_output_file, 'w') as pc_output, open(npc_output_file, 'w') as npc_output:
            # Read each line and write it to the appropriate output file
            for line in input_file:
                if "_15_" in line:
                    pc_output.write(line.strip() + '\n')
                    print(f"Line saved to {pc_output_file}: {line.strip()}")
                else:
                    npc_output.write(line.strip() + '\n')
                    print(f"Line saved to {npc_output_file}: {line.strip()}")

        # Remove the extra newline character at the end of the output files
        with open(pc_output_file, 'rb+') as pc_output:
            pc_output.seek(-1, os.SEEK_END)
            if pc_output.read(1) == b'\n':
                pc_output.seek(-1, os.SEEK_END)
                pc_output.truncate()
        with open(npc_output_file, 'rb+') as npc_output:
            npc_output.seek(-1, os.SEEK_END)
            if npc_output.read(1) == b'\n':
                npc_output.seek(-1, os.SEEK_END)
                npc_output.truncate()

        print(f"All lines saved to {pc_output_file} and {npc_output_file}")

process_files()
