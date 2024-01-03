# whole file into single string
fname = "with_file_open_read.py"
with open(fname) as file:
    file_content_str = file.read()
