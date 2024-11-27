# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)

program_on = True
while program_on:
    word = input("Enter a word: ").upper()
    if word != "":
        try:
            output_list = [phonetic_dict[letter] for letter in word]
            print(output_list)
        except KeyError as error_message:
            print(f"That '{error_message}' is not in the dictionary list. Please re-enter a legit word. ")
        else:
            while 1<2:
                more = input("Do you want to play more? YES or NO: ")
                if more.upper() == "YES":
                    break
                elif more.upper() == "NO":
                    program_on = False
                    break
                else:
                    print("please re-input YES or NO correctly")
                    pass
        # else:
        #     pass
    elif word.upper() == "EXIT":
        program_on = False
    else:
        print("Please enter, do not leave blank!")
        pass

