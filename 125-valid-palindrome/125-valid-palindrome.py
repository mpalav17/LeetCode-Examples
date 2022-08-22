import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = new_str.lower()
        mid = floor(len(s)/2)
        if len(s) ==0:
            return True
        elif len(s) == 1:
            return True
        elif len(s)%2 != 0:#odd
            for i in range(1,mid+1):
                if s[mid+i] == s[mid-i]:
                    pass
                else:
                    return False
            return True
        else:#even
            for i in range(1,mid+1):
                if s[mid+(i-1)] == s[mid-i]:
                    pass
                else:
                    return False
            return True
