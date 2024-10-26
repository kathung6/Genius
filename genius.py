from itertools import product
import nltk
nltk.download('words')
from nltk.corpus import words


dictionary = set(words.words())

def check_word(word):
    return word in dictionary

def generate_words(letters, gold_letter):
    length = 4
    found_words = set()
    
    while True:
        for comb in product(letters, repeat=length):
            word = ''.join(comb)
            
            if gold_letter in word and check_word(word):
                found_words.add(word)
                
        if found_words:
            yield found_words
            found_words = set()
            
        length += 1

while True:
    try:
        letters = input("Please input the 7 letters: ").strip().lower()
                
        if len(letters) != 7 or not letters.isalpha():
            print("Error: too few letters. Please input 7 letters.")
            continue
        
        gold_letter = input("Please input the 'gold' letter (one of the 7 letters): ").strip().lower()
        
        if len(gold_letter) != 1 or gold_letter not in letters:
            print("Error: the gold letter must be a single character from the 7 letters provided.")
            continue
        
        word_generator = generate_words(letters, gold_letter)
            
        
        for words in word_generator:
            for word in sorted(words):
                if len(set(word)) ==  len(set(letters)):
                    print(f"PANGRAM!----{word}")
                else:
                    print(word)  
                    
    except KeyboardInterrupt:
        print("ERROR: Invalid input. Please input letters")
        break