# yield list with each line in the file
fname = "with_file_open.py"
with open(fname) as file:
    line_list = file.readlines()
