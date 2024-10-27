<h1 align="center">Lost Needle</h1>
<p align="center">
  <img alt="Funny Needle" src="./assets/Needle.jpg" width="300"><br>
</p>


Keep your Doors Locked!\
A Net Scanner which finds (PHP) files on the internet

Current features:
<br>
<ls>
* Debug Logging 
* Pooling of the requests
* Config System
</ls>
</br>

## How to setup 

1. you need [Python](https://www.python.org/downloads/ "Python Installation") installed

2. you install the requirements


``` 
pip install -r requriements.txt
```

Now just run the main.py file

```
python main.py
```

### Customize File list 
Add your own files to the search query by adding them to the json file.
```json
{
  "files": [
    "FILE1",
    "FILE2",
    "FILE3"
  ]
}
