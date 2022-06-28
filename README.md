Welcome to the web app for Model Monitoring project.


# Run a Notebook, web app:

1. Pull current repo:
```buildoutcfg
git clone https://github.com/galinadychko/titanic
```
2. Create a virtual environment and install requirements
```
# Windows
PATH_TO_PYTHON\python -m venv .venv

.venv\Scripts\pip install -r requirements.txt
```
3. a. To run notebooks:
```
.venv\Scripts\jupyter notebook
```
3. b. To run application:
```
.venv\Scripts\streamlit run start.py
```

## About Repo:
* `/notebooks` contains EDA of titanic data and generate necessary documents for the web app. 
That's important to run it before start web app!
* `/data` - data to display in web app
* `/pages` - pages of the web app
* `/tools` - folder with metrics
