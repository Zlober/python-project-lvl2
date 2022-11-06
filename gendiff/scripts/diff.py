from gendiff.core import cli, generate_diff


def main():
    file1, file2, output_format = cli()
    result = generate_diff(file1, file2, output_format)
    print(result)


if __name__ == '__main__':
    main()
