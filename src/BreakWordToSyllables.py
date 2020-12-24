class WordToSyllable:
    # List of single sound exceptions for double consonants
    single_sound_pairs = ['th', 'sh', 'ph', 'ch', 'wh','ck']
    # English vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Used to keep track of last syllable break
    last_break=0
    # Lists to hold syllables
    syllables = []

    def ProcessWord(self,word):
        self.word = word

        # Clear any previous uses of class
        self.CleanUp()

        # Iterate over the word, character by character
        char_types=[]
        for c in self.word:
            char_types.append(self.VowelCheck(c))
        # If no other vowels, make 'y' a vowel
        if char_types.count('v') == 0:
            if 'y' in self.word:
                y_idx = self.word.index('y')
                char_types[y_idx] = 'v'

        for i in range(0,len(char_types)):

            #
            # Check rules for syllables
            #

            # Cannot check rules on first character
            if i == 0:
                continue

            # RULE 1: If two consecutive consonants
            if char_types[i] == 'c' and char_types[i-1] == 'c':

                # Handle exception of if two consonants make a single sound
                char_pair = word[i-1] + word[i]
                if char_pair not in self.single_sound_pairs:
                    if i <= self.last_break+1:
                        continue
                    self.BreakHandler(i)
                    self.last_break = i
                else:
                    if len(self.syllables) != 0 and self.last_break==i-1:
                        self.syllables[-1]+=char_pair
                        self.last_break+=2

            # RULE 2: consonants surrounded by vowels
            if i > 2:
                if char_types[i] == 'v' and char_types[i-1] =='c':
                    if char_types[i-2] == 'v':
                        # Short sound vowel case; if only 1 vowel in the word
                        if char_types.count('v') == 1:
                            self.BreakHandler(i)
                            self.last_break = i+1
                        # Long sound vowel case;
                        else:
                            self.BreakHandler(i)
                            self.last_break = i

        self.BreakHandler(i)

    def CleanUp(self):
        self.syllables.clear()
        self.last_break = 0

    def VowelCheck(self,char):
        # List of vowels
        if char in self.vowels:
            return 'v'
        else:
            return 'c'

    def BreakHandler(self,char_idx):
        word_size = len(self.word)-1
        if char_idx == word_size:
            # If at the end, at the remaining characters to the syllables list
            if self.last_break < word_size:
                self.syllables.append(self.word[self.last_break:])
        else:
            # If a break rule was hit, add the characters to the left as a syllable
            self.syllables.append(self.word[self.last_break:char_idx])

# test_tool = WordToSyllable()
# from OldEnglishName import OldEnglishName
# for i in range(1,10):
#     test_tool.ProcessWord(OldEnglishName('female'))
#     print(test_tool.syllables)
