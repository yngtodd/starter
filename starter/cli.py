"""Command line interface for starter."""
import argh


def greet() -> None:
    r"""Say hello, starter"""
    print(f'Hello, world!')


def main():
    parser = argh.ArghParser()
    parser.add_commands([greet])
    parser.dispatch()


if __name__=='__main__':
    main()
