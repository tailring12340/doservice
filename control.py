import numpy as np
import dbaccess
import model
import pandas as pd

databaseAccess = dbaccess.dbaccess()

# def japonica_data_X_reshape(viewdata):

#     japonica_data_X = viewdata[['do_temp', 'ph', 'orp', 'co2_mg', 'air_oxy', 'light_ma', 'feed_quantity', 'water_quantity']]

#     japonica_data_X_reshape = np.asarray(japonica_data_X, dtype=np.float64)
#     japonica_data_X_reshape = japonica_data_X_reshape.reshape((-1, 1, 8))
    
#     return japonica_data_X_reshape

def viewdata(tank_id, start_date, end_date, regressor):
    japonica_data = dbaccess.dataPreprocessing(databaseAccess, tank_id, start_date, end_date)
    viewdata = japonica_data[['do_mg']]

    if regressor:
        dbmodel = dbaccess.model(engine=databaseAccess, tank_id=tank_id)
        japonica_data_X = japonica_data[['do_temp', 'ph', 'orp', 'co2_mg', 'air_oxy', 'light_ma', 'feed_quantity', 'water_quantity']]
        japonica_data_X_reshape = np.asarray(japonica_data_X, dtype=np.float64)
        japonica_data_X_reshape = japonica_data_X_reshape.reshape((-1, 1, 8))
        X_pred = model.X_pred(model=dbmodel,japonica_data_X_reshape=japonica_data_X_reshape)
        viewdata['do_regressor'] = pd.Series(X_pred.reshape(-1)).values
    
    return viewdata

def doregreesor(tank_id, viewdata):
    
    return viewdata