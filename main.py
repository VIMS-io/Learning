command=''
started=False
while True:
    command=input("> ").lower()
    if command== 'start':
        if started:
            print('Car already started')
        else:
            print('Car started...')
            started=True
    elif command=='stop':
        if started:
            print('Car stopped')
            started=False
        else:
            print('Car already stopped')
    elif command=='help':
        print('''
start - start the car
stop - stop the car
quit- quit game
        ''')
    elif command=="quit":
        print('quiting game')
        break
    else:
        print("Sorry I don't understand that")
    