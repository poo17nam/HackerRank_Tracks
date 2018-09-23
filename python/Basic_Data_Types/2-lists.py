if __name__ == '__main__':
    N = int(input())
    command_list = []
    for i in range(0,N):
        command_list.append(input())

    arr = []
    for command in command_list:
        eachCommand = command.split()
        if eachCommand[0] == 'insert':
            arr.insert(int(eachCommand[1]),int(eachCommand[2]))
        elif eachCommand[0] == 'print':
            print(arr)
        elif eachCommand[0] == 'remove':
            arr.remove(int(eachCommand[1]))
        elif eachCommand[0] == 'append':
            arr.append(int(eachCommand[1]))
        elif eachCommand[0] == 'sort':
            arr.sort()
        elif eachCommand[0] == 'pop':
            arr.pop()
        elif eachCommand[0] == 'reverse':
            arr.reverse()
