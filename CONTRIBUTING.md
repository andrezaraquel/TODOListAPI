## Development environment setup

To clone the project run the following command:
```bash
git clone https://github.com/andrezaraquel/TODOListAPI.git
```

### For the next commands on this page, you must be at the **root** of the project

#### There are 3 simple ways to run this code and install all dependencies. They are as follows:

##### 1 - Using docker-compose:

```bash
docker-compose up
```

##### 2 - Using Dockerfile (If, for some reason, you do not want to use docker-compose):

```bash
docker build --tag todo-list-compose .

docker run -p 127.0.0.1:5000:5000 todo-list-compose
```
##### 2 -  Using a virtual environment

```bash
python3 -m venv venv
```

After setup, the development is activated through the command:

```bash
source venv/bin/activate
```

To install the required libs, run the following command:

```bash
pip install -r requirements.txt 
```
