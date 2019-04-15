

# open test.txt file 

# initialize a dit 

# loop over each line in opened file 
    # split line at space " " to get list of words
    # loop over list of words
        # use .get method to either initialize 
        # or increment value of the word

# print each key value pair 

def get_word_counts(file_name):
    """Given text file return count of each space-separated string."""

    word_count_dict = {}

    with open(file_name) as opened_file:

        for line in opened_file:
            line = line.rstrip()
            words_list = line.split(" ")

            for word in words_list:

                word_count_dict[word] = word_count_dict.get(word, 0) + 1

    for pair in word_count_dict.items():
        print(pair[0], pair[1])

get_word_counts('test.txt')





