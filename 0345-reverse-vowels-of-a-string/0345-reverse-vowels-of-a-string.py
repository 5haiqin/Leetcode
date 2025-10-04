class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        arr = list(s)
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] not in vowels:
                i += 1
            elif arr[j] not in vowels:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return ''.join(arr)
