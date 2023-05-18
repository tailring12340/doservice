import streamlit as st
import datetime
import control
#import dbaccess
# import model
# import pandas as pd

#databaseAccess = dbaccess.dbaccess()
#japonica_data = dbaccess.dataPreprocessing(databaseAccess)


st.title('용존 산소 확인')

start_date = st.date_input(
    "조회 시작일을 선택해 주세요. 2021.07.15.",
    datetime.datetime(2021, 7, 15)
)

end_date = st.date_input(
    "조회 종료일을 선택해 주세요. 2022.01.06.",
    datetime.datetime(2021, 7, 15)
)

tank_id = st.selectbox(
    '확인할 탱크를 선택해 주세요',
    ('1', '2', '3', '4', '5'))

regressor = st.checkbox('DO 예측값',value=False)

# with st.sidebar:
#     date = st.date_input(
#         "조회 시작일을 선택해 주세요",
#         datetime.datetime(2022, 1, 1)
#     )

#     code = st.text_input(
#         '종목코드', 
#         value='',
#         placeholder='종목코드를 입력해 주세요'
#     )

start_date = datetime.datetime.combine(start_date,datetime.time(00,00,00))
end_date = datetime.datetime.combine(end_date,datetime.time(23,59,59))
tank_id = int(tank_id)

if tank_id and start_date and end_date:
    viewdata = control.viewdata(tank_id=tank_id,start_date=start_date,end_date=end_date, regressor=regressor)

    #if regressor:
        # dbmodel = dbaccess.model(engine=databaseAccess, tank_id=tank_id)
        # japonica_data_X_reshape = control.japonica_data_X_reshape(japonica_data=data)
        # X_pred = model.X_pred(model=dbmodel,japonica_data_X_reshape=japonica_data_X_reshape)
        # viewdata['do_regressor'] = pd.Series(X_pred.reshape(-1)).values
        #control.doregreesor(tank_id=tank_id,viewdata=viewdata)

    tab1, tab2 = st.tabs(['차트', '데이터'])

    with tab1:    
        st.line_chart(viewdata)

    with tab2:
        st.dataframe(viewdata.sort_index(ascending=False))
