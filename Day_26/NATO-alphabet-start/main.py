
import pandas
data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

my_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Write a word: ").upper()

output_list = [my_dict[letter] for letter in user_input]
print(output_list)
 

