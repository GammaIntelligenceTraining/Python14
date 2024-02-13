# 38803160272

while True:
    user_id = input('Enter national ID: ')
    try:
        int(user_id)
        if len(user_id) != 11:
            raise Exception
    except ValueError:
        print('Code is not numeric. Try again.')
    except Exception:
        if len(user_id) > 11:
            print('Code is too long. Try again.')
        else:
            print('Code is too short. Try again.')
    else:
        while True:
            user_choice = input('1.Gender\n'
                                '2.Date of birth\n'
                                '3.Region\n'
                                '4.Validate\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '--> ')
            if user_choice == '1':
                if user_id[0] not in '09':
                    if int(user_id[0]) % 2 == 0:
                        print('You are female.')
                    else:
                        print('You are male.')
                else:
                    print('Error in ID code.')


            elif user_choice == '2':  # DD.MM.YYYY
                cent = ''
                if user_id[0] not in '09':
                    if user_id[0] in '12':
                        cent = '18'
                    elif user_id[0] in '34':
                        cent = '19'
                    elif user_id[0] in '56':
                        cent = '20'
                    else:
                        cent = '21'
                print(f'{user_id[5:7]}.{user_id[3:5]}.{cent}{user_id[1:3]}')
            elif user_choice == '3':  # Not in list (was not born in Estonia)
                if int(user_id[7:10]) in range(1, 11):
                    print('Kuressaare haigla')
                elif user_id[7:10] > '000' and user_id[7:10] <= '010':
                    print('Tartu Ülikooli Naistekliinik')
                elif user_id[7:10] >= '021' and user_id[7:10] <= '150':
                    print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')

            elif user_choice == '4':
                chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                result = 0
                for i in range(10):
                    result += int(user_id[i]) * chk1[i]
                if result % 11 == 10:
                    result = 0
                    for i in range(10):
                        result += int(user_id[i]) * chk2[i]

                if result % 11 == int(user_id[-1]):
                    print('Your ID is valid.')
                else:
                    print('Your ID is invalid.')

            elif user_choice == '5':
                break
            elif user_choice == '0':
                print('Good bye!')
                quit()
            else:
                print('Choice is out of range!')