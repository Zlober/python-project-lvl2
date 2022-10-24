from Gendiff.core import cmd, generate_diff


def main():
    file1, file2 = cmd()
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()