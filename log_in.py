
import time

username = 'tcm9798'
password = 'tcm123456'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Authorization successful')
    print('Loading, please stand by...')
    time.sleep(5)
    print('Hang tight… spinning up the gears…')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Access confirmed. Summoning the ultra-top-secret screen of mysteries...')
elif username_input == username and password_input != password:
    print('Nice try, but that password is wrong.')
elif username_input != username and password_input == password:
    print('Hmm… that username doesn’t seem right.')
else:
    print('Both inputs are acting suspicious… give them another try.')
