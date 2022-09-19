def isValid(s: str) -> bool:
    """
    :type s: str - String to be tested for validity
    :rtype: bool - Returns true if the string is valid else false
    """

    opening = ['(','[','{']
    closing = [')',']','}']

    if len(s) % 2 == 1:
        return False
    if s[0] not in opening:
        return False

    cl_pos = [opening.index(s[0])]
    op = 1
    cl = 0
    for i in range(1, len(s)):
        if s[i] in opening:
            op += 1
            cl_pos.append(opening.index(s[i]))
        else:
            cl += 1
            if s[i] != closing[cl_pos[-1]]:
                return False
            else:
                del cl_pos[-1]
    if op != cl:
        return False
    else: return True

if __name__ == "__main__":
    line = input("Enter parentheses: ")
    if isValid(line):
        print("valid")
    else:
        print("invalid")