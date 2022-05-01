# My code
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        dec = 1
        while digits:
            num += (digits.pop() * dec)
            dec *= 10
        num += 1
        num = str(num)
        digits = (list(num))
        return list(map(int, digits))
    
#         # num = list(map(str, digits))
#         # num = ''.join(num)
#         # num = int(num)
#         # num += 1
#         # num = str(num)
#         # digits = (list(num))
#         # return list(map(int, digits))

# # Neetcode
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = digits[::-1]
#         one, i = 1, 0
        
#         while one:
#             if i < len(digits):
#                 if digits[i] == 9:
#                     digits[i] = 0
#                 else:    
#                     digits[i] += 1
#                     one = 0
#             else:
#                 digits.append(1)
#                 one = 0
#             i += 1
#         return digits[::-1]