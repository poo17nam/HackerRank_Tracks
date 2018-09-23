if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)

    unique_list = []
    for i in range(0,n):
        if arr[i] not in unique_list:
            unique_list.append(arr[i])

    unique_list.sort(reverse=True)
    print(unique_list[1])
