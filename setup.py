import os
import webbrowser

url = 'http://127.0.0.1:5000/'


res = os.system('pip install -r requirements.txt && npm i')

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

if res == 0:
    print('dependecies installed!')
    print('Running server and client...')
    webbrowser.get(chrome_path).open(url)
    os.system('flask run')
else:
    print('oops... something happened')
