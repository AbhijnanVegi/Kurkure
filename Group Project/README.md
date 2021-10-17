# Group Project
**Team Name** : Kurkure

# About
A model database of an online shopping website created as a part of Data and applications course@IIITH.

# Installation
You will need `docker` and `docker-compose` to run this project.  
After installing the above dependencies run the following commands  
```
docker-compose up -d

pip install -r requirements.txt
```
Initialise the database by running the following command
```
docker exec -i mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < dump.sql
```
To run the application run
```
python main.py
```
# Useful commands
To access the mysql console run
```
docker exec -it mysql mysql -uroot --password=password
```
To create a new dump file run
```
docker exec mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > dump.sql
```