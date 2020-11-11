student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

data = pandas.read_csv("nato_phonetic_alphabet.csv")
d = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phoenetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [d[letter] for letter in word]
    except KeyError:
        print("Please enter a valid word")
        generate_phoenetic()
    else:
        print(output_list)


generate_phoenetic()