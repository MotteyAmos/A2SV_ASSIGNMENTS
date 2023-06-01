class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_string = ""
        i = 0
        while i < len(word1) and i < len(word2):
            merge_string += word1[i] + word2[i]
            i += 1
        if (len(word1) > len(word2)):
            merge_string += word1[i:]
        else:
            merge_string += word2[i:]
        
        return merge_string
