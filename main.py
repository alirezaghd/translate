

def read_():
    #int
    print('loading')
    f = open('alireza_translate/translate.txt')

    big_text = f.read()

    parts = big_text.split('\n')

    words = []
    i = 0

    while i<len(parts):

        my_dict = {'english': parts[i] , 'persian':parts[i+1]} #empty dic

        words.append(my_dict)

        i += 2


    print('data loaded')
    print('Welcome Dear user, please enter your text')

    user_string = input()

    user_word = user_string.split(' ')

    for j in range(len(user_word)):
        for i in range(len(words)):
            if words[i]['english'] == user_word[j] :
                print(words[i]["persian"])
                break
        else:    
            print(user_word[j],end=' ')


def write_():
    print('loading')
    f1 = open('alireza_translate/translate.txt', "a")
    f1.write('\n')
    i_engilish = input("inster your english Word :")
    f1.write(i_engilish)
    f1.write('\n')
    i_persian = input("inster your persian Word :")
    f1.write(i_persian)

    f1.close







print("1- read transalte" , "2- write translate" , "3- Exit")

m = int(input('insert number of menu : '))

if m == 1:
    read_()
if m == 2 :
    write_()
if m == 3 :
    exit()