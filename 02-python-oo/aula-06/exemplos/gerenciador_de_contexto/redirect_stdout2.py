from contextlib import contextmanager
import sys


@contextmanager
def redirect_stdout(stream):
    original_stdout = sys.stdout
    sys.stdout = stream
    yield
    sys.stdout = original_stdout
