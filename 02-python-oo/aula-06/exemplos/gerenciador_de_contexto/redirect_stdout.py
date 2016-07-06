import sys


class redirect_stdout:
    def __init__(self, stream):
        self.stream = stream
        self.original_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = self.stream

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.original_stdout


if __name__ == '__main__':
    print('antes do redirect')

    with open('stdout.txt', 'w') as stream:
        with redirect_stdout(stream):
            print('estou dentro do gerenciador de contexto')
            print('espero que de certo')

    print('estou fora do redirect')
