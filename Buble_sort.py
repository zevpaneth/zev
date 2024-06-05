def bubble_sort(words):
    n = len(words)
    for i in range(n):
        check = False
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
                check = True
        if not check:
            break
    return words


