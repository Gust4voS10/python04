

def secure_archive(file_path: str, action: int, write: str) -> tuple[bool, str]:
    try:
        if action == 0:
            print(f"Using '{file_path}' to read from a nonexistent file")
            with open(file_path, 'r') as file:
                data_fragment = file.read()
                print(f"True, {data_fragment}\n")
                return [True, data_fragment]
        elif action == 1:
            print(f"Using '{file_path}' to "
                  f"write previous content to a new file")
            with open(file_path, 'w') as file:
                file.write(write)
                print("True, Content successfully written to filezn\n")
                return [True, "'Content successfully written to file'"]

    except FileNotFoundError:
        print(f"False, [Errno 2] No such file or directory: '{file_path}'\n")

    except PermissionError:
        print(f"(False, [Errno 13] Permission denied: '{file_path}'")


def main() -> None:
    print("=== Cyber Archives Security ===")
    secure_archive("c.txt", 0, "a")
    secure_archive("bca.txt", 0, "a")
    secure_archive("abc.txt", 0, "a")
    secure_archive("a", 1, "abcbcabac")


if __name__ == "__main__":
    main()
