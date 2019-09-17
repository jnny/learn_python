import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '4799', 'Shattuck', 'Ave.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '4799', 'Shattuck', 'Ave.'] -> '4799 Shattuck Ave.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://google.com/maps/place/<ADDRESS>
webbrowser.open('https://google.com/maps/place/' + address)
