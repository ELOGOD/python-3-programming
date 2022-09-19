def calPoints(ops: list) -> int :
    """
    :type ops: List[str] - list of operations e.g ["5","2","C","D","+"]
    :rtype: int - Sum of scores after performing all operations
    """
    if len(ops) < 1:
        result = 0
        return result
    record = [int(ops[0])]
    print(record)
    for i in range (1, len(ops)):
        if ops[i] == "C":
            del record[-1]
        elif ops[i] == "D":
            record.append(2 * record[-1])
        elif ops[i] == "+":
            record.append(record[-1] + record[-2])
        else:
            try:
                record.append(int(ops[i]))
            except: continue

    
    result = sum(record)

    return result

if __name__ == '__main__':
    line = input("Enter the correct commands: ")
    ops = line.strip().split()
    print(ops)

    print(calPoints(ops))

