if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list_tuple = tuple(integer_list)
    hashValue = hash(integer_list_tuple)
    print(hashValue)
