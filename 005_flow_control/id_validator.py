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
                pass
            elif user_choice == '2':  # DD.MM.YYYY
                pass
            elif user_choice == '3':  # Not in list (was not born in Estonia)
                pass
            elif user_choice == '4':
                pass
            elif user_choice == '5':
                break
            elif user_choice == '0':
                print('Good bye!')
                quit()
            else:
                print('Choice is out of range!')
