secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('Make a guess : '))
    guess_count +=1
    if guess== secret_number:
        print('you won')
        break
else:
    print(f'you ran out of gueses.Correct number was {secret_number} ')