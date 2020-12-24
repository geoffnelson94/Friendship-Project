class WordToSyllable:
    # List of single sound exceptions for double consonants
    single_sound_pairs = ['th', 'sh', 'ph', 'ch', 'wh']
    # English vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'y' ]
    # Used to keep track of last syllable break
    last_break=0
    # Lists to hold syllables
    syllables = []

    def __init__(self,word):
        self.word = word
        # Iterate over the word, character by character
        char_types=[]
        for i,v in enumerate(self.word):
            char_types.append(self.VowelCheck(v))

            #
            # Check rules for syllables
            #

            # Cannot check rules on first character
            if i == 0:
                continue

            # If two consecutive consonants
            if char_types[i] == 'c' and char_types[i-1] == 'c':

                # Handle exception of if two consonants make a single sound
                char_pair = word[i-1] + word[i]
                if char_pair not in self.single_sound_pairs:
                    if i <= self.last_break+1:
                        continue
                    self.BreakHandler(i)
                    self.last_break = i
                else:
                    if len(self.syllables) != 0:
                        self.syllables[-1]+=char_pair
                        self.last_break+=2

        # End of rules, add remaining part of word to last_syllables
        self.BreakHandler(i)

    def VowelCheck(self,char):
        # List of vowels
        if char in self.vowels:
            return 'v'
        else:
            return 'c'

    def BreakHandler(self,char_idx):
        if char_idx == len(self.word)-1:
            # If at the end, at the remaining characters to the syllables list
            self.syllables.append(self.word[self.last_break:])
        else:
            # If a break rule was hit, add the characters to the left as a syllable
            self.syllables.append(self.word[self.last_break:char_idx])

test_tool = WordToSyllable('birthday')
print(test_tool.syllables)
