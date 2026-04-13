import sys
import typing


def recover_file():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        sys.stdout.write(f"Accessing file {file_path}\n")
        try:

            file: typing.IO = open(file_path, 'r')
            data_fragment = file.read()

            sys.stdout.write("---\n\n")
            sys.stdout.write(data_fragment)
            sys.stdout.write("\n---\n")

            file.close()
            sys.stdout.write(f"file '{file_path}' closed\n")

            sys.stdout.write("\nTransform data:\n")
            att_data_fragment = ""
            lines = data_fragment.splitlines()
            for line in lines:
                att_data_fragment += line + "#\n"

            sys.stdout.write("---\n\n")
            sys.stdout.write(att_data_fragment)
            sys.stdout.write("\n---\n")

            sys.stdout.write("Enter new file name (or empty):")
            sys.stdout.flush()

            new_file_input = sys.stdin.readline()
            new_file = new_file_input.strip()

            if new_file:
                sys.stdout.write(f"Saving data to '{new_file}'")
                create_file = open(new_file, 'w')
                create_file.write(att_data_fragment)
                create_file.close()
                sys.stdout.write(f"Data saved in file '{new_file}'.")
            else:
                sys.stdout.write("Not saving data.")

        except FileNotFoundError:
            sys.stderr.write(f"Error opening file '{file_path}': "
                             f"[Errno 2] No such file "
                             f"or directory: '{file_path}'")
        except PermissionError:
            sys.stderr.write(f"Error opening file '{file_path}': "
                             f"[Errno 13] Permission denied"
                             f": '/etc/master.passwd'")
    else:
        sys.stdout.write("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    sys.stdout.write("=== Cyber Archives Recovery ===\n")
    recover_file()
