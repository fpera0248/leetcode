class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def word_to_value(word):
            return int(''.join(str(ord(char) - ord('a')) for char in word))
    
        return word_to_value(firstWord) + word_to_value(secondWord) == word_to_value(targetWord)