import webmachine

if __name__ == '__main__':
    wm = webmachine.WebMachine('')
    while True:
        command = input('Input command here: ')
        print(wm.execute_command(command))