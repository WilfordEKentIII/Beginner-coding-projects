#This game tests how gullible a person is lol
print("The Gullible Game, test your luck!")

while True:#Main loop
    print('Do you want to know how to keep a gulluble person bust for hours? (Y/N)')
    response = input('> ')#Get the user input
    if response.lower() =='no' or response.lower() =='n':
        print('Thank you.Have a nice day!')
        break
    if response.lower() == 'yes' or response.lower() == 'y':
        continue # continues the loop 

        print('"{}is not a valid yes/no response.'. format(response))
    
    