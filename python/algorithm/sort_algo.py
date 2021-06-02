def bubble(l):
    num = len(l) - 1
    for index1 in range(num):
        for index2 in range(num - index1):
            if l[index2+1] < l[index2]:
                l[index2], l[index2+1] = [l[index2 + 1], l[index2]]

def bubble_recursive_py3(l):
    num = len(l) - 1
    for index in range(num):
        if l[index+1] < l[index]:
            l[index], l[index+1] = [l[index + 1], l[index]]

            bubble(l)
