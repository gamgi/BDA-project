#! /bin/sh
echo "Downloading entire dataset"
sh bin/fetch_data_sources.sh
echo "Converting municipal.json to municipal.csv"
cat municipal.json | jq '.variables[1] | [.values, .valueTexts] | transpose' | jq -r '.[] | @csv' > municipal.csv
echo "...all done"
