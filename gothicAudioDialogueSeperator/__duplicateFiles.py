import shutil

# specify the path of the text file containing the list of wav files
text_file_path = "R:\_voice\_zFianaldatabase\z_finalG2\_filelists\g_val13G1_D_final_T_file.txt"

# specify the paths of folder A and folder B
##folder_a_path = "path/to/folder_a"
##folder_b_path = "path/to/folder_b"

folder_a_path = "R:\_voice\_zFianaldatabase\z_finalG2\wav4Pass"
folder_b_path = "R:\_voice\_zFianaldatabase\z_finalG2\wav4PassDup"

# open the text file and read the list of wav files
with open(text_file_path, "r") as f:
    wav_files = f.read().splitlines()

# iterate through the list of wav files and copy them from folder A to folder B
for wav_file in wav_files:
    file_path = f"{folder_a_path}/{wav_file}"
    shutil.copy(file_path, folder_b_path)
    
print("Done Dublication")