import os


def display_prompt():
    current_directory = os.getcwd()
    print(f"{current_directory}>", end=" ")


def help_command(args):
    print("help - Wyświetla sposób użycia programu oraz informacje o komendach")
    print("quit lub exit - Kończy program")
    print("ls - Wyświetla pliki w aktualnym katalogu")
    print("cr <nazwa> - Tworzy plik o podanej nazwie")
    print("cd <katalog> - Przechodzi do podanego katalogu")
    print("mkdir <katalog> - Tworzy katalog o podanej nazwie")
    print("o <filename> - Wyświetla zawartość pliku tekstowego")
    print("stat <filename> - Podsumowuje zawartość pliku: ilość znaków")
    print("rename <n1> <n2> - Zmienia nazwę pliku <n1> na <n2>")
    print("find <p> <file> - Wyświetla linijki z pliku <file>, w którym znaleziono tekst <p>")


def ls_command(args):
    files = os.listdir()
    for i, file in enumerate(files, start=1):
        print(f"[{i}]{file}", end=" ")
    print()


def cr_command(args):
    if args:
        try:
            with open(args[0], 'w'):
                print(f"Plik '{args[0]}' został utworzony.")
        except Exception as e:
            print(f"Błąd podczas tworzenia pliku '{args[0]}': {e}")
    else:
        print("Podaj nazwę pliku.")


def o_command(args):
    if args:
        try:
            with open(args[0], 'r') as file:
                content = file.read()
                print(content)
        except Exception as e:
            print(f"Błąd podczas odczytu pliku '{args[0]}': {e}")
    else:
        print("Podaj nazwę pliku.")


def stat_command(args):
    if args:
        try:
            with open(args[0], 'r') as file:
                content = file.read()
                char_count = len(content)
                print(f"Ilość znaków w pliku '{args[0]}': {char_count}")
        except Exception as e:
            print(f"Błąd podczas odczytu pliku '{args[0]}': {e}")
    else:
        print("Podaj nazwę pliku.")


def rename_command(args):
    if len(args) == 2:
        try:
            os.rename(args[0], args[1])
            print(f"Zmieniono nazwę pliku z '{args[0]}' na '{args[1]}'.")
        except Exception as e:
            print(f"Błąd podczas zmiany nazwy pliku: {e}")
    else:
        print("Podaj dwie nazwy plików.")


def find_command(args):
    if len(args) == 2:
        try:
            pattern = args[0]
            filename = args[1]
            with open(filename, 'r') as file:
                lines = file.readlines()
                matching_lines = [line.strip() for line in lines if pattern in line]
                if matching_lines:
                    print(f"Znaleziono linijki w pliku '{filename}', zawierające tekst '{pattern}':")
                    for line in matching_lines:
                        print(line)
                else:
                    print(f"Nie znaleziono linijek w pliku '{filename}', zawierających tekst '{pattern}'.")
        except Exception as e:
            print(f"Błąd podczas przeszukiwania pliku '{filename}': {e}")
    else:
        print("Podaj wzorzec i nazwę pliku.")


def cd_command(args):
    if args:
        try:
            os.chdir(args[0])
        except Exception as e:
            print(f"Błąd podczas zmiany katalogu: {e}")
    else:
        print("Podaj nazwę katalogu.")


def mkdir_command(args):
    if args:
        directory_name = args[0]
        os.makedirs(directory_name, exist_ok=True)
        print(f"Utworzono katalog: {directory_name}")
    else:
        print("Użycie: mkdir <nazwa_katalogu>")


def quit_command(args):
    exit()


def unknown_command(args):
    print("Nieznana komenda. Wpisz 'help' aby uzyskać pomoc.")


def main():
    commands = {
        'help': help_command,
        'quit': quit_command,
        'exit': quit_command,
        'ls': ls_command,
        'cr': cr_command,
        'o': o_command,
        'cd': cd_command,
        'mkdir': mkdir_command,
        'stat': stat_command,
        'rename': rename_command,
        'find': find_command,
    }

    while True:
        display_prompt()
        user_input = input().split()
        command = user_input[0].lower()
        args = user_input[1:]

        commands.get(command, unknown_command)(args)


if __name__ == "__main__":
    main()
