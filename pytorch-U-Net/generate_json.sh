if [ $# -eq 2 ]
then
    sed 's/Orig_U-net/'$2'/g' $1 > config.json
else
    echo "Invalid argument"
fi
