## Development environment setup

To clone the project run the following command:
```bash
git clone https://github.com/andrezaraquel/TODOListAPI.git
```

### For the next commands on this page, you must be at the **root** of the project

#### There are 2 simple ways to run this code and install all dependencies. They are as follows:

##### 1 - Using docker-compose:

```bash
docker-compose up --build --force-recreate
```

##### 2 -  Using a virtual environment

```bash
python3 -m venv venv
```

After setup, the development is activated through the command:

```bash
source venv/bin/activate
```
Install the PostgreSQL database. Then, set the correct credentials in the .env file.

To install the required libs, run the following command:

```bash
pip install -r requirements.txt 
```

Then run the following command to start the application:

```bash
python -m flask --app app/main run --debug --host=0.0.0.0
```
