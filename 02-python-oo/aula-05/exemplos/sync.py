import requests


if __name__ == '__main__':
    import sys
    verbose = '-v' in sys.argv

    for _ in range(25):
        response = requests.get('http://httpbin.org/get')
        print(response.status_code)
        if verbose:
            print(response.text)
