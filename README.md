## Getting Started

```
Pipenv shell
pipenv run init-db
aerich init -t app.database.TORTOISE_ORM
aerich init-db
```

##Database data
Import data to postgresql tables, found in `/DatabaseTables`
The database and tables have already been created the database is called `stayplugged` and each csv is named with the name of the table.

##Run Server
```
pipenv run server
```

##API Documentation
Go to: http://localhost:8000/docs