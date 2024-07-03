#!/bin/bash

end_timestamp=$(date +%s)
current_date=$(date --date="10 days ago" +%s)
Suffix=".L3m_DAY_CHL_chlor_a_4km.nc"
Suffix2=".L3m.DAY.CHL.chlor_a.4km.NRT.nc"
Prefix="AQUA_MODIS."
Prefix2="A"

while [ "$current_date" -le "$end_timestamp" ]; do
    formatted_date=$(date -d "@$current_date" "+%Y-%m-%d")
    doy=$(date -d "@$current_date" "+%j")
    nozero=$(echo $doy | sed 's/^0*//')
    YEAR=$(date -d "@$current_date" "+%Y")
    DAY=$(date -d "@$current_date" "+%d")
    MONTH=$(date -d "@$current_date" "+%m")
    num=$(printf "%03d" $nozero)

    FileName="${Prefix2}${YEAR}${num}${Suffix}"
    FileName2="${Prefix}${YEAR}${MONTH}${DAY}${Suffix2}"
    #echo $FileName $FileName2
    output_file="/home/anuj/Desktop/choloro/${FileName}"
    echo $output_file

    #wget -nc http://169.154.128.44/ob/getfile/$FileName2?appkey=fb95de75edd756ef103e91b2ec74c2dda74a3f93 --no-check-certificate  -O $output_file
    wget -nc https://oceandata.sci.gsfc.nasa.gov/ob/getfile/$FileName2?appkey=fb95de75edd756ef103e91b2ec74c2dda74a3f93 --no-check-certificate  -O $output_file
 
    if [ $? -eq 0 ]; then
        # Check if the file size is 0 KB
        file_size=$(wc -c < "$output_file")

        if [ "$file_size" -eq 0 ]; then
            echo "Downloaded file is 0 KB. Removing."
            rm "$output_file"
        else
            echo "File downloaded successfully."
        fi
    else
        echo "Error downloading the file. Removing empty file if created."
        rm "$output_file"  # Remove the file if it was created but is empty
    fi

    # Add one day to the current date
    current_date=$((current_date + 86400))  # 86400 seconds in a day
done