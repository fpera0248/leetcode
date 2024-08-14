class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:



        res = []

        for sentence in sentences:
# Split the sentence into words
            words = sentence.split()
            # Count the number of words in the sentence
            total = len(words)
            # Append the count to the res list
            res.append(total)

        # Return the maximum number of words found in any sentence
        return max(res)
