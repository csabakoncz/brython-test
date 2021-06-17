Create a virtual environment (I used Python 3.9.5):

```
python3 -m venv --copies venv

source venv/bin/activate

pip install -r requirements.txt
```

Start a webserver:
```
python -m http.server
```