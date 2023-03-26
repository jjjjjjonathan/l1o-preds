#! python3
import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    print('no args?')