class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        length = len(ransomNote)
        many = 0
        much = 0
        for i in range(0, length):
            if ransomNote[i] in magazine:
                many = ransomNote.count(ransomNote[i])
                much = magazine.count(ransomNote[i])
                if many > much:
                    return False
            else:
                return False
        return True



# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         cnt = collections.Counter(magazine)
#         for c in ransomNote:
#             if cnt[c]:
#                 cnt[c] -= 1
#             else:
#                 return False
#         return True