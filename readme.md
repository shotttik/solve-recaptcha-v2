# Instructions to run the project

### Install ffmpeg

<a href="https://phoenixnap.com/kb/ffmpeg-windows" target="_blank">Instruction for installing ffpmeg</a>

### Install pip

> python -m pip install --user --upgrade pip

### Installing virtualenv

> python -m pip install --user virtualenv

### Creating a virtual environment¶

> python -m venv env

### Activating a virtual environment¶

> source env/bin/activate

### Installing packages

> python -m pip install -r requirements.txt

`Resources/config.json`

```
{
  "browser": "chrome",
  "arguments": [
    "--start-maximized",
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36"
  ],
  "experimental_options": [
    ["prefs", { "download.default_directory": "./Resources/" }],
    ["excludeSwitches", ["enable-automation"]],
    ["useAutomationExtension", false]
  ],
  "wait_time": 10
}
```

`Resrouces/data.json`

```
{
  "start_url": "https://www.google.com/recaptcha/api2/demo",
}
```

## RUN PROJECT

> python main.py

# ATTENTION:

### Make sure you have filled `data.json` and `config.json`
