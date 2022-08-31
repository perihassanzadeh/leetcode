class Solution:
    def isValid(self, s: str) -> bool:
        sList = list(s)
        parenList = []
        
        for item in sList:
            if item == '(' or item=='{' or item=='[':
                parenList.append(item)
            elif item == ')' or item == '}' or item==']':
                if len(parenList) != 0:
                    if item == ')' and parenList[-1] == '(':
                        parenList.pop()
                    elif item == '}' and parenList[-1] == '{':
                        parenList.pop()
                    elif item == ']' and parenList[-1] == '[':
                        parenList.pop()   
                    else:
                        return False
                else:
                    return False
            else:
                return False
            
        if len(parenList)==0:
            return True
        else:
            return False