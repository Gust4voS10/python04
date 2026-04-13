

def secure_archive(file_path: str, action: int, write: str) -> tuple[bool, str]:
    try:
        if action == 0:
            print(f"Using '{file_path}' to read from a nonexistent file")
            with open(file_path, 'r') as file:
                data_fragment = file.read()
        elif action == 1:
            print(f"Using '{file_path}' to write previous content to a new file")
            with open(file_path, 'w') as file:
                file.write(write)
        return [True, data_fragment]

    except (FileExistsError, PermissionError) as e:
        return [False, e]


def main() -> None:
    print("=== Cyber Archives Security ===")
    print(secure_archive("c.txt", 0, "a"))
    print(secure_archive("bca.txt", 0, "a"))
    print(secure_archive("abc.txt", 0, "a"))
    print(secure_archive("a", 1, "abcbcabac"))


if __name__ == "__main__":
    main()
