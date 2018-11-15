#! /bin/bash
beginswith() { case $2 in "$1"*) true;; *) false;; esac; }

echo "Fetching data..."
while IFS=$'\t' read -r col1 col2
do
  if beginswith \# "$col1"; then
    : # no-op
  elif beginswith http "$col2"; then
    echo "Fetching $col2 to $col1"
    curl --silent --show-error -o "data/$col1" "$col2"
  else
    echo "Skipping \"$col2\", not a valid url"
  fi
done < data_sources.tsv

echo "...data fetched"
