#sed -e 's/\s/\n/g' < dracula.txt | sort | uniq -c | sort -nr | head -11 > top10_words.txt
tr -c '[:alnum:]' '[\n*]' < dracula.txt | sort | uniq -c | sort -nr | head -11 > top10_words.txt
sed -i '1d' top10_words.txt
mkdir -p top10_files
while read FILE; do touch "${FILE}";mv "${FILE}" top10_files; done < top10_words.txt
# mv "${FILE}" ./top10_files;
cd top10_files
for f in *; do mv "$f" `echo $f | tr ' ' '_'`; done

