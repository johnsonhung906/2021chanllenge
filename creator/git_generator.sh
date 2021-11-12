set -e

for ((i = 0 ; i < 47 ; i++)); do
    echo "times: ${i}"
    # make for special commit words
    # if [ $i -eq 203 ]
    # then 
    #     echo "hint1 created at ${i} commit"
    #     ./generators/text_hint1_gen.py > trash_words.txt
    #     git add .
    #     git commit --author="Oscar <oscar@dd.org>" -am "words from Oscar"
    #     sleep 1
    # fi
    # if [ $i -eq 50 ]
    # then 
    #     echo "hint2 created at ${i} commit"
    #     ./generators/text_hint2_gen.py > trash_words.txt
    #     git add .
    #     git commit --author="Jeffery <jeffery@dd.org>" -am "Shiba Inu the best"
    #     sleep 1
    # fi
    # txt gen 
    ./generators/text_gen.py > trash_words.txt
    ./generators/mes_gen.py > message.txt
    ./generators/author_gen.py > author.txt
    while IFS= read -r line; do
        commitMessage="$line"
    done < message.txt
    while IFS= read -r line; do
        commitAuthor="$line"
    done < author.txt
    git add .
    # git commit 
    git commit --author="$commitAuthor" -am "$commitMessage"
    # for different git log time
    sleep 1
done