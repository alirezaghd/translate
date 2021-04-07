

def read_E_To_P():
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

    user_sen = user_string.split('.')
    user_word = user_string.split(' ')
    
    #####################################

    if '.' in user_string:
        for j in range(len(user_sen)):
            for i in range(len(words)):
                if words[i]['english'] == user_sen[j] :
                    print(words[i]["persian"])
                    

    elif ' ' in user_string :               
        for j in range(len(user_word)):
            for i in range(len(words)):
                if words[i]['english'] == user_word[j] :
                    print(words[i]["persian"])
                    break
            else:    
                print(user_word[j],end=' ')

def read_P_To_E():
    #int
    print('loading')
    f2 = open('alireza_translate/translate.txt')

    big_text1 = f2.read()

    parts1 = big_text1.split('\n')

    words1 = []
    i = 0

    while i<len(parts1):

        my_dict1 = {'persian': parts1[i+1] , 'english':parts1[i]} #empty dic

        words1.append(my_dict1)

        i += 2


    print('data loaded')
    print('Welcome Dear user, please enter your text')

    user_string1 = input()

    user_word1 = user_string1.split(' ')

    for j in range(len(user_word1)):
        for i in range(len(words1)):
            if words1[i]['persian'] == user_word1[j] :
                print(words1[i]["english"])
                break
        else:    
            print(user_word1[j],end=' ')

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






print("Wellcome to Alireza Translate")
print(" 1- Add New word \n" , "2- translate Engilish to persin \n" , "3- translate persian to Engilish \n ", "4- Exit")


m = int(input('insert number of menu : '))

if m == 1 :
    write_()
if m == 2:
    read_E_To_P()
if m == 3:
    read_P_To_E()
if m == 4 :
    exit()