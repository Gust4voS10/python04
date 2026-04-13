import sys
import typing


def recover_file():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"Accessing file {file_path}")
        try:

            file: typing.IO = open(file_path, 'r')
            data_fragment: str = file.read()

            print("---\n")
            print(data_fragment)
            print("---")

            file.close()
            print(f"file '{file_path}' closed")

            print("\nTransform data:")
            att_data_fragment = ""
            lines = data_fragment.splitlines()
            for line in lines:
                att_data_fragment += line + "#\n"

            print("---\n")
            print(att_data_fragment)
            print("---")

            new_file = input("Enter new file name (or empty):")

            if new_file:
                print(f"Saving data to '{new_file}'")
                create_file: typing.IO = open(new_file, 'w')
                create_file.write(att_data_fragment)
                create_file.close()
                print(f"Data saved in file '{new_file}'.")
            else:
                print("Not saving data.")

        except FileNotFoundError:
            print(f"Error opening file '{file_path}': "
                  f"[Errno 2] No such file or directory: '{file_path}'")
        except PermissionError:
            print(f"Error opening file '{file_path}': "
                  f"[Errno 13] Permission denied: '/etc/master.passwd'")
    else:
        sys.stdout.write("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    recover_file()
