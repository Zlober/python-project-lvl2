from gendiff.core import cmd, generate_diff


def main():
    file1, file2 = cmd()
    result = generate_diff(file1, file2)
    print(result)


if __name__ == '__main__':
    main()
