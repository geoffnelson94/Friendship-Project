
def BreakWordToSyllables(word):
    # List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'y' ]

    # List of single sound exceptions for double consonants
    single_sound_pairs = ['th', 'sh', 'ph', 'ch', 'wh']

    # Iterate over the string, character by character
    num_vowels=0
    for i, v in enumerate(word):
        # If at end of the word, nothing to do
        if i == len(word)-1:
            break
        # Determine if hit a vowel
        if v in vowels:
            num_vowels+=1
        else: # Must be a consonant.
        # First check for double consonant, indicating a break

            print(word[i+1])





BreakWordToSyllables('test')
