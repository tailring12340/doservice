import pymysql
import pandas as pd
from sqlalchemy import create_engine

def dbaccess():
    # 데이터베이스 연결 설정
    host = 'localhost'
    user = 'root'
    password = '0000'
    database = 'japonica'

    # 데이터베이스 연결
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine

def dataPreprocessing(engine, tank_id, start_date, end_date):
    #start_date = str(start_date)
    #end_date = str(end_date)
    query = f"SELECT sensor.mea_dt AS mea_dt, sensor.tank_id AS tank_id, sensor.do_mg AS do_mg, sensor.do_temp AS do_temp, sensor.ph AS ph, sensor.orp AS orp, sensor.co2_mg AS co2_mg, sensor.air_oxy AS air_oxy, sensor.light_ma AS light_ma, food_supply.feed_quantity AS feed_quantity, food_supply.water_quantity AS water_quantity FROM sensor LEFT JOIN food_supply ON DATE_FORMAT(sensor.mea_dt, '%%Y-%%m-%%d %%H:%%i') = DATE_FORMAT(food_supply.feed_dt, '%%Y-%%m-%%d %%H:%%i') AND sensor.tank_id = food_supply.tank_id AND sensor.farm_id = food_supply.farm_id WHERE sensor.tank_id = '{tank_id}' and mea_dt BETWEEN '{start_date}' AND '{end_date}';"

    japonica_data = pd.read_sql(query, engine)
    japonica_data.set_index('mea_dt', inplace=True)
    japonica_data = japonica_data.sort_index()
    japonica_data = japonica_data.fillna(0)

    feature_origin = ['tank_id','do_mg','do_temp', 'ph', 'orp', 'co2_mg', 'air_oxy', 'light_ma', 'feed_quantity', 'water_quantity']
    japonica_data = japonica_data[feature_origin]

    return japonica_data

def model(engine, tank_id):
    query = f"SELECT model FROM meta_data where tank_id={tank_id} order by 'id' desc"
    model = pd.read_sql(query, engine)
    model = model.values.tolist()
    model = ' '.join(model[0])
    return model