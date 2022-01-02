echo $OSTYPE

if [[ $OSTYPE == "Win32" ]];
then 
    echo "Oh no! Win32 unsupport."
else 
    python3 server.py
fi