# airflow-packaged-dag
A git repo that shows a minimal airflow packaged dag

# Installation

* Clone the repository

    `git clone git@github.com:nitinpandey-154/airflow-packaged-dag.git`


* Recursively zip the contents of project

    ```
    cd airflow-packaged-dag
    zip -r my_dag.zip *

    ```
    
* Move the dag to airflow dags folder

    `mv my_dag.zip ~/airflow/dags/`
