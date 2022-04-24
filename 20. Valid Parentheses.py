class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["0"]
        check = ")}]"
        j = 0
        for i in range(0, len(s)):
            stack.append(s[i])
            j += 1
            if stack[j] in check:
                if stack[j] == ")" and stack[j-1] == "(":
                    stack.pop()
                    stack.pop()
                    j = j - 2
                elif stack[j] == "}" and stack[j-1] == "{":
                    stack.pop()
                    stack.pop()
                    j = j - 2
                elif stack[j] == "]" and stack[j-1] == "[":
                    stack.pop()
                    stack.pop()
                    j = j - 2
                else:
                    return False
        if stack[-1] == "0":
            return True
        else:
            return False
        