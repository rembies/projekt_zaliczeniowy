import os

blocked_commands = ['rm -rf', 'format', 'shutdown']

while True:
    current_path = os.getcwd()
    user_input = input(f'{current_path}> ')

    if user_input.lower() == 'exit':
        print('Zamykanie programu...')
        break

    if user_input.startswith('cd '):
        new_directory = user_input[3:].strip()
        try:
            os.chdir(new_directory)
        except FileNotFoundError:
            print(f'Katalog nie istnieje: {new_directory}')
        except Exception as e:
            print(f'Wystąpił błąd podczas zmiany katalogu: {e}')
    elif user_input.startswith('open '):
        file_name = user_input[5:].strip()
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f'Plik nie istnieje: {file_name}')
        except Exception as e:
            print(f'Wystąpił błąd podczas otwierania pliku: {e}')
    elif user_input.startswith('ls '):
        path = user_input[3:].strip()
        try:
            print(os.listdir(path))
        except FileNotFoundError:
            print(f'Katalog nie istnieje: {path}')
        except Exception as e:
            print(f'Wystąpił błąd podczas listowania katalogu: {e}')
    else:
        blocked = any(command in user_input for command in blocked_commands)
        if blocked:
            print('Nie można wykonać zablokowanej komendy.')
            continue

        try:
            result = os.system(user_input)
            if result != 0:
                print(f'Wystąpił błąd podczas wykonywania komendy. Kod błędu: {result}')
        except Exception as e:
            print(f'Wystąpił błąd: {e}')

print('Program został zamknięty.')
