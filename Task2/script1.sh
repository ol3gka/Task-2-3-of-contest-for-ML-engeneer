tr -c '[:alnum:]' '[\n*]' < dracula.txt | sort | uniq -c | sort -nr > top_words.txt
#sed -e 's/\s/\n/g' < dracula.txt | sort | uniq -c | sort -nr | > top_words.txt
sed -i '1d' top_words.txt
echo 'Top 30 words are shown'
head -30 top_words.txt
