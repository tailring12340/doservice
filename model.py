from keras import backend as K
from keras.models import load_model

# r_squared 평가 함수
def r_squared(y_true, y_pred):
    ss_res = K.sum(K.square(y_true - y_pred))
    ss_tot = K.sum(K.square(y_true - K.mean(y_true)))
    return (1 - ss_res/(ss_tot + K.epsilon()))

# 모델 평가 함수
#def grapeNEva(model, X_test_shape, y_test):

    # 그래프 생성
 #   plt.figure(figsize=(15, 7))
 #   plt.plot(y_test.index, y_test, label='DO')  # x축에 년월일, y축에 값
 #   plt.plot(y_test.index, X_pred, color='red', label='Regressor')  # x축에 년월일, y축에 시분
  #  plt.xlabel('date')
   # plt.ylabel('DO')
   # plt.title('DO Regressor')
   # plt.legend(['y_test','X_pred'])
   # plt.show()
    

    

# def doRegressorTrainingPreprocessing (sensor, food_spply):
#     #자포니카 훈련 데이터 시계열 변환
#     sensor["mea_dt"] = sensor["mea_dt"].apply(str)
#     sensor["mea_dt"] = sensor["mea_dt"].str.slice(start=0, stop=16)
#     food_spply['feed_dt'] = pd.to_datetime(food_spply['feed_dt'], format='%Y%m%d%H%M', errors='raise')
#     food_spply["feed_dt"] = food_spply["feed_dt"].apply(str)
#     food_spply["feed_dt"] = food_spply["feed_dt"].str.slice(start=0, stop=16)

#     # 자포니카 훈련 데이터 및 시계열 데이터 병합
#     japonica_training = pd.merge(left = sensor, right = food_spply, how = "left", left_on = ["farm_id","tank_id", "mea_dt"], right_on = ["farm_id","tank_id", "feed_dt"])
#     japonica_training['mea_dt'] = pd.to_datetime(japonica_training['mea_dt'], format='%Y-%m-%d %H:%M', errors='raise')
#     japonica_training.set_index('mea_dt', inplace=True)
#     japonica_training = japonica_training.sort_index()
#     feature_origin = ['tank_id','do_mg','do_temp', 'ph', 'orp', 'co2_mg', 'air_oxy', 'light_ma', 'feed_quantity', 'water_quantity']
#     japonica_training_features = japonica_training[feature_origin]
#     japonica_training_features = japonica_training_features.fillna(0)


#     feature_Learning = ['do_temp', 'ph', 'orp', 'co2_mg', 'air_oxy', 'light_ma', 'feed_quantity', 'water_quantity']
#     feature_number = len(feature_Learning)

#     # 자포니카 검증 데이터의 한 개 탱크
#     tank = 1
#     japonica_training_features_tank = japonica_training_features[japonica_training_features['tank_id']==tank]

#     japonica_training_features_X = japonica_training_features_tank[feature_Learning]

#     # LSTM학습을 위해 데이터 reshape를 해야함. reshape를 위해 배열형으로 변환
#     japonica_training_features_X_reshape = np.asarray(japonica_training_features_X, dtype=np.float64)

#     japonica_training_features_X_reshape = japonica_training_features_X_reshape.reshape((-1, 1, feature_number))
    # 가중치를 통해 변수 중요도 획득
#    weights = model.layers[0].get_weights()[0]
#print(weights)
# 변수 중요도 시각화
# fig, ax = plt.subplots(figsize=(8, 4))
# ax.bar(range(feature_number), weights[:, 0])
# ax.set_xticks(range(feature_number))
# ax.set_xticklabels(feature_Learning)
# ax.set_ylabel('Weight')
# ax.set_title('Variable Importance')
# plt.show()
    # # 평가 생성
    # result = model.evaluate(X_test_shape, y_test)
    # print("MSE // MAE // R-squared ", result)


def X_pred(model, japonica_data_X_reshape):
    model = load_model(model, custom_objects={'r_squared': r_squared})
    X_pred = model.predict(japonica_data_X_reshape)

    return X_pred