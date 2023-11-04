def swap_case(s):
    text=s
    list=[]
    for i in text:
        if i==i.lower():
            i=i.upper()
            list.append(i)
        elif i==i.upper():
            i=i.lower()
            list.append(i)
    list=''.join(list)
    return list

    """or you can use just s.swapcase()"""

  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)