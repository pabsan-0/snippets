# load json into dict 
import json
fname = "foo.json"
with open(fname) as file:
    my_dict = json.load(file)
