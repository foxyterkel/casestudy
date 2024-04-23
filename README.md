# Case study
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
+ processor - the place where all processing logic encapsulated, we also can do validation and metrics consolidation here.
+ writer - writes transformed data to datasource, currently writes at Postgres but can be extended to handle other types of storage.

### pg_data_wh
Postgres database that has result data of the computations. You can easily connect to it to query the tables
`psql -h localhost -p 5488 -U my_data_wh_user -d my_data_wh_db -W`
password is `my_data_wh_pwd`

Query sample:
`select * from student_performance;`

Tables are created in the `init.sql` script that runs during table initialisation.

- POSTGRES_DB: my_data_wh_db
- POSTGRES_USER: my_data_wh_user
- POSTGRES_PASSWORD: my_data_wh_pwd

### grafana
Default dataSource is configured in `datasource.yaml` 
Default user `admin` with password `admin`



Q: What could be done if data volume increases 100x?
A: At the moment source file size is 57 kb. I would say we're on a safe side here to increase the load 10 000 times and the solution will handle it.
Container resource adjustments might be needed. For the further increase it's a good practice to split files in chunks and we can easily orchestrate the solution to process different files in parallel.


Q: What could be done if data is delivered frequently at 6am every two days?
A: As processing is made on the Docker container we have flexibility to schedule processing as we need it, so there is no issue in this matter.

Q: What could be done if the data has to be made available to a bigger organization of 1000+ people?
As Grafana performs read only the solution should perform well at this scale. However, for the further user increase we might consider read-only replicas.