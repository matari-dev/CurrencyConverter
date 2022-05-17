# make an list of all the letters
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()  

double_alphabet = {}  # start with empty dictionary

# add to dictionary 
for letter in letters:
    double_alphabet[letter] = letter + letter
