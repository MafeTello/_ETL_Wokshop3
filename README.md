# Workshop_03 - Machine Learning Prediction and streaming data 
Autor: [@MafeTello](https://github.com/MafeTello)

---

## Welcome
Given the 5 CSV files which have information about happiness score in different countries, train a regression machine learning model to predict the happiness score.

Throughout this process, specific technologies were used including:

- _Python_ <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px"> 

- _Jupyter Notebook_  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">

- _PostgreSQL_ as the relational database management system (this was chosen by personal preference). <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">

- _Apache Kafka_  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Apache_kafka.svg/1200px-Apache_kafka.svg.png" width="21px" height="25px">

## Objectives

- **Data Analysis and Preparation (EDA and ETL)**: Performed exploratory data analysis and prepared the dataset for modeling processes by cleaning, preprocessing, and selecting the most relevant features.

- **Regression Model Development**: Built a regression model using a 70% training and 30% testing data split, optimizing its performance to obtain accurate results.

- **Data Streaming Implementation with Kafka**: Designed a data streaming architecture using Kafka, allowing real-time processing of data from the EDA and ETL stages for predictive modeling.

- **Prediction and Results Storage**: Used the trained model to generate real-time happiness score predictions and stored those predictions along with associated features in a database.


## Folder path

```
Workshop3
├── .env                          # Archivo de configuración de entorno
├── .vscode                       # Configuraciones específicas de VS Code
├── data                          # Contiene archivos de datos CSV
│   ├── 2015.csv                  # Datos del año 2015
│   ├── 2016.csv                  # Datos del año 2016
│   ├── 2017.csv                  # Datos del año 2017
│   ├── 2018.csv                  # Datos del año 2018
│   ├── 2019.csv                  # Datos del año 2019
│   └── datos_limpios.csv         # Archivo CSV con datos limpios
├── database                      # Módulos relacionados con la base de datos
│   └── connection.py             # Script para la conexión a la base de datos
├── docker                        # Archivos de configuración para Docker
│   ├── pgadmin-workshop3         # Configuración de pgAdmin
│   ├── postgres-db-volume-kafka  # Volumen de base de datos para Kafka
│   ├── docker-compose.yml        # Archivo de configuración de Docker Compose
│   ├── docker-secrets            # Archivo de secretos de Docker
│   └── docker-secrets-pgadmin    # Secretos específicos para pgAdmin
├── document
│   └── kafka_app                 # Aplicación relacionada con Kafka
│       ├── consumer.py           # Script del consumidor en arquitectura de microservicios
│       ├── main.py               # Script principal para Kafka
│       └── producer.py           # Script del productor en arquitectura de microservicios
├── Model                         # Carpeta para almacenar el modelo entrenado
│   └── model.pkl                 # Archivo pickle con el modelo entrenado
├── notebooks                     # Notebooks Jupyter para análisis de datos
│   ├── 001_EDA_mt.ipynb          # Notebook para análisis exploratorio de datos (EDA)
│   ├── 002_model_training.ipynb  # Notebook para entrenamiento de modelos
│   └── 003_score_metrics.ipynb   # Notebook para evaluación de métricas del modelo
├── .gitignore                    # Archivo para ignorar ciertos archivos en control de versiones
└── README.md                     # Archivo README con información del proyecto

```




## Run this project

First of all here is the requierements

Install Python : [Python Downloads](https://www.python.org/downloads/)  
Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)  
Install Docker : [Docker Downloads](https://www.docker.com/get-started/)

1. Clone this repository:
```bash
   git clone https://github.com/MafeTello/_ETL_Wokshop3.git
 ```

2. Go to the project directory  
```bash
   cd WORKSHOP3
```

3. Create a virtual enviroment  
```bash
  python -m venv venv
```

4. Start the virtual enviroment  
  ```bash  
  ./venv/Scripts/activate
  ```


5. Create a database in PostgreSQL


6. Start with the notebook:
- 001_EDA_mt.ipynb
  
7. Run the streaming
- Open a terminal and run:
    
  ```bash
  docker-compose up
  ```
    
- Open a new terminal and get into container terminal running:
  ```bash
    docker exec -it kafka-test bash
  ```
     
- Create a new topic:
  
  ```bash
    kafka-topics --bootstrap-server kafka-test:9092 --create --topic predict-happiness
  ```

- Run producer and consumer:

  - **producer**
    
    ```bash
    python producer.py
    ```
    
  - **consumer**
    
    ```bash
    python consumer.py
    ```

  Now go to:
  - 002_model_training.ipynb

  and see the performance of the model.

## Thank you for visiting this repository.
