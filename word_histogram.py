# Word Summary

# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# $ python3 word_histogram.py
# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}




def word_summary(sentence):
    words = sentence.lower().split()
    hist_dictionary = {}
    for word in words: 
        word = word.strip(".,?!")
        if word.isalpha():
            if word in hist_dictionary:
                hist_dictionary[word] += 1
            else :
                hist_dictionary[word] = 1
    return hist_dictionary

user_input = input("Type a sentence: ")
result = word_summary(user_input)
print(result)












# def word_summary(sentence):
# # this function takes a single argument "sentence"
#     words = sentence.lower().split()
#     # this variable word makes sentence lowercase and splits string into a list, making each word individual
#     hist_dictionary = {}
#     # this creates a blank dictinary for us to store all these words in it
#     for word in words: 
#     # for loop to find each word in words/sentence input
#         word = word.strip(".,?!")
#         # removes extra special characters
#         if word.isalpha():
#         # if conditional statement to make it all alphabetic characters
#             if word in hist_dictionary:
#             # if word is in hist_dict then....
#                 hist_dictionary[word] += 1
#                 # if its there already, then add one more count to it 
#             else :
#             # if its not there...
#                 hist_dictionary[word] = 1
#                 # if its not there then give it a count 
#     return hist_dictionary
#     # returns the dictionary containing the count of each word 

# user_input = input("Type a sentence: ")
# # what user types in
# result = word_summary(user_input)
# # calls the word_summary function to the user_input and assigns this to variable result
# print(result)
# # prints the result of the function 