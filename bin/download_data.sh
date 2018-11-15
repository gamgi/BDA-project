#! /bin/sh
command -v jq >/dev/null 2>&1 || { echo >&2 "You need to install jq first."; exit 1; }
mkdir -p data
echo "Downloading entire dataset"
sh bin/fetch_data_sources.sh
echo "Converting municipal.json to municipal.csv"
cat data/municipal.json | jq '.variables[1] | [.values, .valueTexts] | transpose' | jq -r '.[] | @csv' > data/municipal.csv
echo "...all done"
