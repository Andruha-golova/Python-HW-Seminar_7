def poem(x):
    str_1 = x.split()
    print(str_1)
    str_2 = []
    for i in str_1: 
        sum = 0
        vowels = set('аеёиоуыэюя')   
        for letter in i:
            if letter in vowels:
                sum += 1
        str_2.append(sum)
    if len(set(str_2)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')
my_text = 'пам-па-пам па-рам-па-пам па-пам пам пам'
poem(my_text)