# print_two_markdowns.py

def print_md():
    files = ["f25_Billiet.md", "f25_Thomas.md"]

    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"error: '{file_path}' not found")
        except Exception as e:
            print(f"error while reading '{file_path}' {e}")


if __name__ == "__main__":
    print_md()
