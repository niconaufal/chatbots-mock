
Clone repo and create a virtual environment
diCMD bukanya
```
$ cd chatbot-deployment
$ python3 -m pip install --user virtualenv
$ python3 -m venv ini-env (ini-env itu nama enviromentnya bisa diganti)
$.\ini-env\Scripts\activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot
jangan lupa pas di terminal vscode tulis ini 'pip install -r requirements.txt'

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```
kalau udah semua tinggal dicoba tinggal run dan start debugging di file app.py di vscode
Now for deployment follow my tutorial to implement `app.py` and `app.js`.

