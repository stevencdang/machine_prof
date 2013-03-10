list_path = 'wordList'
out_path = 'sat_words'
list_file = open(list_path, 'r')
out_file = open(out_path, 'w')
word_lines = list_file.readlines()
for line in word_lines:
    word = line.split()[0]
    out_file.write(word + '\n')
list_file.close()
out_file.close()
