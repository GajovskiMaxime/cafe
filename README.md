# Cafe

Cafe is a coffee-meeting app developed with Python, Postgres, and the Flask web framework.

### Prerequisites

- Start by ensuring that you have Docker, Docker Compose, and Docker Machine installed:

```
$ docker -v
Docker version 17.03.1-ce, build c6d412e
$ docker-compose -v
docker-compose version 1.11.2, build dfed245
$ docker-machine -v
docker-machine version 0.10.0, build 76ed2a6
```

Docker is really all you need. That's all.

### Installing


Build the image:
```
docker-compose up -d --build
```

\
This will take a few minutes the first time. Subsequent builds will be much faster since 
Docker caches the results of the first build. Once done, fire up the container:
```
docker-compose up -d
```

> The -d flag is used to run the containers in the background.\
> However, you don't have any logs from containers with the -d flag.

You can run the following command to verify if your containers are running and up. 
```
docker ps -a

f2b2c5b03461        cafe_cafe_service    "/bin/sh -c 'pytho..."   24 hours ago        Up 24 hours             0.0.0.0:5001->5000/tcp   cafe_service
611c8409b47b        cafe_cafe_database   "docker-entrypoint..."   5 days ago          Up 25 hours (healthy)   0.0.0.0:5435->5432/tcp   cafe_database
```

\
Next you have to re/create the database:
```
docker-compose run cafe_service python manage.py recreate_database
```
> You can  go inside of the container and call the alias 'pmn'
>```
> alias pmr="python manage.py recreate_database"
> ``` 

\
And then you can run the server:
```
docker-compose run cafe_service python manage.py runserver
```
Server will be opened for the url : [http://localhost:5001/](http://localhost:5001/)
> Take a look at docker-compose.yml for more informations.

\
You can reach the ip address of a container by the following command :
```
docker exec -it <container_name> ip addr show eth0 | grep -Po 'inet \K[\d.]+'
```
or
```
docker exec -it <container_name> bash
$ ip addr show eth0 | grep -Po 'inet \K[\d.]+'
```
> It can be useful if you want to connect to the database (cafe_database).

Both of containers are now configured with static_ip.
```
cafe_database ---> 172.20.128.3
cafe_service  ---> 172.20.128.2
```
> 
## Running the tests

You can run tests with the following command : 
```
docker-compose run cafe_service python manage.py test
```

There's no covering test at the moment (14/07/2017)

### Coding style tests

Python has its own coding style - called pep8 - that we expect you to respect.\
 - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
 > Some IDEs supports continuous checking of your code for PEP 8 compliance on the fly, as you type it in the editor. (JetBrains IDEs)

## Deployment

Soon (14/07/2017)

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE for Professional Developers
* [PostgreSQL](https://www.postgresql.org/) - PostgreSQL is an object-relational database management system 
(ORDBMS).
* [Flask](http://flask.pocoo.org/) - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.

## Authors
* **Gajovski Maxime** - *Initial work* - [Cafe](https://github.com/GajovskiMaxime/cafe)

## TO DOs
Last update (15/07/2017)
* Impl. i18n
* Impl. models like User
* Creates relationship between models
* Creates clever routes in order to reach models
* Auth
* Security
* Desployment
* Test Coverage
* Impl. Tests
* Password Crypt.