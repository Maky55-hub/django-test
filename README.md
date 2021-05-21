# Setting up environments

## Using virtualenv
Use the following method to create a virtual environment and activate it.

1. install virtualenv: pip install virtualenv
2. cd project_folder
3. run: virtualenv venv -> creates a folder "venv" which will contain the python executable files
4. activate: source venv/bin/activate
5. deactivate: deactivate

### Using requirements.txt

1. pip freeze > requirements.txt 
This will create a "requirements.txt" file, which contains a simple list of all the packages in the current environment, and their respective versions. 

2. pip install -r requirements.txt
Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions.

3. pip install <package.name>
Installs a package only for the current environment. run: pip freeze > requirements.txt, to update the requirements.txt file.


## Using Pipenv
Use the following method to setup a virtual environment for a project using pipenv.
Install pipenv using the following command.
pip install pipenv

1. cd project_folder
2. pipenv install -> creates an environment using the Pipfile that is available. If Pipfile is not available, than this creates a new Pipfile.
3. pipenv shell -> launches the environment
4. exit -> exits from the environment

### Using Pipfile

1. pipenv install <package.name> -> installs the package and adds it to the Pipfile.
2. pipenv install -r requirements.txt -> installs the packages from the requirements.txt file and adds them also to the Pipfile.
3. pipenv lock -r > requirements.txt -> adds the packages installed in the environment to the requirements.txt file.
4. pipenv uninstall <package.name> uninstalls a package from the environment and also removes it from the Pipfile


## .env File
Setup the environments file with the credentials for your DB in the folder where settings.py resides
