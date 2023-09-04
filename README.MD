# Install
1. 插件environment: `python -m venv .venv`
2. 激活virtual environment: `. .venv/bin/activate`
3. `pip install -r requirements.txt`
4. 退出virtual environment: `deactivate`

# Start
1. `FLASK_DEBUG=1 FLASK_APP=app.py flask run` 
2. 


# Notebooks

1. `conda create --name tools.python --clone base`
1. `conda activate tools.python`
2. `pip install -r requirements.txt`
3. `jupyter notebook`
4. `conda remove --name tools.python --all`