def secure_archive(file_path: str, action: int,
                   write: str = "") -> tuple[bool, str]:
    try:
        if action == 0:
            print(f"Using '{file_path}' to read from a nonexistent file")
            with open(file_path, 'r') as file:
                data = file.read()
            return (True, data)
        elif action == 1:
            print(f"Using '{file_path}' to "
                  f"write previous content to a new file")
            with open(file_path, 'w') as file:
                file.write(write)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action specified.")

    except (FileNotFoundError, PermissionError) as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print(secure_archive("c.txt", 0))
    print()
    print(secure_archive("t2.txt", 0))
    print()
    print(secure_archive("t1.txt", 0))
    print()
    print(secure_archive("a.txt", 1, "abcbcabac"))
    print()


if __name__ == "__main__":
    main()
