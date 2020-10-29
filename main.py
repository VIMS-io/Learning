print('''
    Start- start the car
    Stop - stop the car
    Quit - quit game
    help - 
    ''')
command = input('Write your command: ')
command=command.lower()
state='stopped'
while command!='quit':
    if command=='help':
        print('''
        Start- start the car
        Stop - stop the car
        Quit - quit game
        help - show help menu
        ''')
    elif command=='start':
        print('Car started')
        state='started'
    elif command=='stop' and state=='started':
        print('Car stopped')
        state='stopped'
    else:
        print(" I do not recognize this command")
