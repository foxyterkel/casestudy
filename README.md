# JustPlay case study
## Composition
This is a docker-compose build that consists of 4 parts:
+ python_app - Processing container with python application.
+ pg_data_wh - Postgres container that stores processed data.
+ grafana - Grafana service.
+ pg_grafana - Postgres db for Grafana.  

to run the whole project - `docker-compose up`

### python_app
The application is encapsulated in a Docker container in order to make it lift-and-shift solution.
This approach gives as ability to choose any orchestration we like and still run this application without any updates.
We can trigger it through Airflow, GCP scheduler, Amazon EventBridge Scheduler etc.
The application composed of 3 extendable pieces:
+ data-provider - provides the data, current implementation rely on local file, but we can easily extend it to use GCS or S3 
+ processor - the place where all processing logic encapsulated, it's straightforward atm but can be extended to have some aggregations and complex transformations.
+ writer - writes transformed data to datasource, currently writes at Postgres but can be extended to handle other types of storage.

### pg_data_wh
Postgres database that has result data of the computations. You can easily connect to it to query the tables
`psql -h localhost -p 5488 -U my_data_wh_user -d my_data_wh_db -W`
password is `my_data_wh_pwd`

Query sample:
`select * from student_performance;`

Tables are created in the `init.sql` script that runs during table initialisation.

POSTGRES_DB: my_data_wh_db
POSTGRES_USER: my_data_wh_user
POSTGRES_PASSWORD: my_data_wh_pwd

### grafana
Default dataSource is configured in `datasource.yaml` 
Default user `admin` with password `admin`
