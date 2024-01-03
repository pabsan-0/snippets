# no guarantees on this one, syntax only
FILE=/foo/bar
if [ -f "$FILE" ]; then
    echo "$FILE exists."
elif [ -L "$FILE" ] && [ -d "$FILE" ]
    echo "$FILE is a symlink to a directory"
else 
    echo "$FILE does not exist."
fi

