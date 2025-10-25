# string=('abcdefg')
#
# for i in range(len(string)-1,-1,-1):
#     print(string[i])
def map_word_length_to_words(words):
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        else:
            length_dict[length].append(word)
    return length_dict


words = ["Joy", "Star", "Chill", "Dream", "Hope", "Quick", "Brave", "Fun", "Code", "Smile"]
length_mapping = map_word_length_to_words(words)
print(length_mapping)