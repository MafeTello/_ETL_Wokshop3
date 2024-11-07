import datetime
from kafka import KafkaConsumer
import joblib
import json
from sqlalchemy.orm import sessionmaker
import pandas as pd
import sys
sys.path.append("../database")
from connection import connection

# Cargar el modelo
model = joblib.load("../database/model.pkl")

# Conectar a la base de datos
conn = connection()

# Consumidor de Kafka
consumer = KafkaConsumer("happiness", bootstrap_servers="localhost:9092",
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

results = pd.DataFrame(columns=['happiness_score', 'gdp_per_capita', 'social_support',
       'health_life_expectancy', 'freedom', 'perceptions_of_corruption',
       'generosity', 'year', 'continent_africa', 'continent_asia',
       'continent_europe', 'continent_north_america', 'continent_oceania',
       'continent_south_america'])

for message in consumer:
    kafka_value = message.value
    new = pd.DataFrame([kafka_value], columns=['happiness_score', 'gdp_per_capita', 'social_support',
       'health_life_expectancy', 'freedom', 'perceptions_of_corruption',
       'generosity', 'year', 'continent_africa', 'continent_asia',
       'continent_europe', 'continent_north_america', 'continent_oceania',
       'continent_south_america'])
    
    predicted = model.predict(new)[0]
    kafka_value['Predicted_Score'] = predicted
    results = pd.concat([results, pd.DataFrame([kafka_value])], ignore_index=True)

    y_true = results['Score']
    y_pred = results['Predicted']

# Cargar el DataFrame a Postgres
Session = sessionmaker(bind=conn)
session = Session()
results.to_sql("happiness", con=conn, if_exists="replace", index=False)

print(f"[{datetime.now()}] - Datos cargados exitosamente en la tabla 'happiness'")

conn.close()

