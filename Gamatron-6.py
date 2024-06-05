from Buble_sort import bubble_sort



file_name = input(f'please write the full name of the file: ')

with open(file_name, "r") as file:
    content = file.read()
# להציג כמה משפטים יש בטקסט כאשר משפטים מופרדים בנקודה


def count_sentences(content):
    counter = 0

    index_counter = 0
    for i, char in enumerate(content):
        if char == ".":
            if i + 1 < len(content) and (content[i + 1] == " " or content[i + 1] == "\n"):
                if i + 2 < len(content) and content[i + 2].isupper():
                    counter += 1
    print(f'This file contains {counter} sentences')

def common_word(content):

    # להציג את המילה הכי נפוצה בטקסט וכמה פעמים היא מופיעה

    # רשימה של כל המילים
    array = []
    word = ""
    for char in content:
        if char == " " or char == '\n':
            array.append(word)
            word = ""
        else:
            word += char

    # ממיין את המילים
    array_sorted = bubble_sort(array)
    #מציג את המילה הכי נפוצה בטקסט
    counter = 0

    most_common_word = None
    main_counter_most_common_word = {"most common word": most_common_word , "shows": counter}
    for word in range(len(array_sorted) - 1):
        if array_sorted[word] == array_sorted[word + 1]:
            most_common_word = array_sorted[word]
            counter += 1
        elif main_counter_most_common_word["shows"] < counter:
                main_counter_most_common_word["most common word"] = most_common_word
                main_counter_most_common_word["shows"] = counter

    print(main_counter_most_common_word)


def longest_word(content):
    # להציג את המילה הכי ארוכה בטקסט, אם יש כמה מילים באותו האורך, להציג
    # את כולן
    # רשימה של כל המילים
    array = []
    word = ""
    for char in content:
        if char == " " or char == '\n':
            array.append(word)
            word = ""
        else:
            word += char

    # ממיין את המילים
    array_sorted = bubble_sort(array)

    counter = 0
    longest_word = None
    main_counter_longest_word = {"longest word": longest_word, "counter": counter}

    for word in array:
        if len(word) > counter:
            counter = len(word)
            main_counter_longest_word["longest word"] = word
            main_counter_longest_word["counter"] = counter
        elif len(word) == counter:
            main_counter_longest_word["longest word"] += f', {word}'
        else:
            continue

    print(main_counter_longest_word)

def different_words(content):
    # להציג את כמות המילים השונות שיש בטקסט
    array = []
    word = ""
    for char in content:
        if char == " " or char == '\n':
            array.append(word)
            word = ""
        else:
            word += char

    # ממיין את המילים
    array_sorted = bubble_sort(array)

    amount_different_words = 0

    different_words = array_sorted
    i = 0
    while i < len(different_words) - 1:
        if different_words[i] == different_words[i + 1]:
            del different_words[i]
        else:
            i += 1

    print(f'the amount of different words in the text is {len(different_words)}')


    #להציג את כל המילים התואמות בכמות הופעתן בטקסט ע"פ קלט משתמש
    # amount = int(input('Please enter the number of impressions of the word: '))
    # # לאתחל המשתנים
    array = []
    word = ""
    for char in content:
         if char == " ":
             array.append(word)
             word = ""
         else:
             word += char

    array_sorted = bubble_sort(array)

    # להציג את כל המילים התואמות בכמות הופעתן בטקסט ע"פ קלט משתמש
    # רציתי כאן לעשות אינדקס וככה לעדכן בFOR את המילים שהופעתם הוא במספר הנקוב
    for word in array_sorted:
        #לא הספקתי לסיים


count_sentences(content)
common_word(content)
different_words(content)
