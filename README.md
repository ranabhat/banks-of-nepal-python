# Banks of Nepal

## Purpose

This is developed to build API that provides the list of commercial banks in Nepal. The goal is to provide all the data such as savings account interest, interest rate, exchange rates, housing loan interest etc. You can follow the [quick start guide](#quickstart) to start building the API. At the moment, it just provides the list of commercial banks in Nepal. It is in development phase. 

## Contents
- [Quick start guide](#quickstart)
    - [Requirements](#requirements)
    - [Download the source code](#download)
    - [Starting development](#startingdevelopment)
- [License](#license)

## <a name="quickstart">Quick start guide</a>

### <a name="requirements">Requirements</a>
- If you don't already have it, install [Postgresql](https://www.postgresql.org/download/linux/ubuntu/)
- If you are installing Postgres in Ubuntu [follow this steps to get started](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
- Create a user and database
- If you don't already have it, install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


### <a name="download">Download the source code</a>
1. Open up your favorite kind of console
2. Navigate to the folder in which you want to store the source code
3. Run `git clone https://github.com/ranabhat/banks-of-nepal-python.git`


### <a name="startingdevelopment">Starting development</a>
1. Open up the source code in your code editor (I recommend [Visual Studio Code](https://code.visualstudio.com/) if you don't have a preference)
2. In the root of the project directory create a virtualenv
```
mkdir banks-of-nepal-python
cd banks-of-nepal-python
python3 -m venv venv
```
3. Activate the environment
```
. venv/bin/activate 
```
4. Install the packages required for the project `pip3 install -r requirements.txt ` 
5. Start migrating database
```
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```
3. Start modifying the code to build your own application
4. Run `FLASK_APP=app.py flask run` in console
5. Open your browser in the address printed to the console
6. Modify the code with your editor

## <a name="license">License</a>

All of the code is licensed under the [MIT license](LICENSE)