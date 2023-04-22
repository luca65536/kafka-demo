# kafka-demo

## Setup
 
### Create a virtual environment

Depending on your system you may need to install python3.10-venv first:
```bash
sudo apt install python3.10-venv
```

Create and source the virtual environment:
```bash
python3 -m venv .venv  
source .venv/bin/activate
```

### Install Python requirements
```bash
pip install -r requirements/development.txt
```

### VSCode Settings for Python
1. Install the recommended Python extensions.
    1. Create a Python file.
    3. Click on "Yes" when VSCode suggests the installation.
2. Install autopep8
    1. Ctrl + Shift + P on a Python file.
    2. Type in and select the "Format Document" option.
    3. Click on "Yes" when VSCode suggests the installation.
3. Install pylint
    1. Ctrl + Shift + P on a Python file.
    2. Type in and select the "Python: Select Linter" option.
    3. Select the "pylint" option.
    3. Click on "Install" when VSCode suggests the installation.

### Start Docker containers
```bash
docker compose up -d
```
