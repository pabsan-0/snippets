# check if variable is set
# VAR=
if [ -z "$VAR" ]
then
    echo "\$VAR is empty"
else
    echo "\$VAR is NOT empty"
fi
