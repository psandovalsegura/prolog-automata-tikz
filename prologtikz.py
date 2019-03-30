#
# Script to convert prolog automata to tikz code
#
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert prolog code to tikz')
    parser.add_argument('prolog_file', type=argparse.FileType('r'),
                                       help='Prolog file with automata definition')
    args = parser.parse_args()

    with args.prolog_file as f:
        print(f.read())

if __name__ == '__main__':
    main()