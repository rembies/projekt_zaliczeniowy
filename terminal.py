import os

blocked_commands = ['rm -rf', 'format', 'shutdown']

while True:
    current_path = os.getcwd()
    user_input = input(f'{current_path}> ')

    if user_input.lower() == 'exit':
        print('Zamykanie programu...')
        break

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