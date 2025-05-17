import math, shutil, sys, time
#Get the size of the terminal window
WIDTH,HEIGHT = shutil.get_terminal_size()
#newline automatically,so reduce the width one:
WIDTH -= 1

print('Sine Message')
print('(Press Ctr-C to quit)')
print()
print('What message do you want to display?(Max ', WIDTH // 2, 'chars.)')
while True:
    message = input('> ') #user input for what the  want the sine wave is suppossed to say
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be up 1 to', WIDTH // 2, 'characters long')

    step = 0.0 #The step determines how far into the sine wave we are
    multiplayer = (WIDTH - len(message)) / 2
    try:
        while True: #Main Loop program
            sinOfStep = math.sin(step)
            padding = ' ' * int((sinOfStep + 1) * multiplayer)
            print(padding + message)
            time.sleep(0.1)
            step += 25
    except KeyboardInterrupt:
        sys.exit()