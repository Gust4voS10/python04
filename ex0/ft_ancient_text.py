import sys


def recover_file() -> None:
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"Accessing file {file_path}")
        try:
            file = open(file_path, 'r')
            data_fragment = file.read()
            print("---\n")
            print(data_fragment, end='')
            print("\n\n---")
            file.close()
            print(f"file '{file_path}' closed")
        except FileNotFoundError:
            print(f"Error opening file '{file_path}': "
                  f"[Errno 2] No such file or directory: '{file_path}'")
        except PermissionError:
            print(f"Error opening file '{file_path}': "
                  f"[Errno 13] Permission denied: '/etc/master.passwd'")
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    recover_file()
