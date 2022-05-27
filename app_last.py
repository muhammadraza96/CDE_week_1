

import streamlit as st
import plotly.express as px
import pandas as pd
from googleapiclient.discovery import build
import json
from google.oauth2 import service_account

#DATA_URL = "C:\Users\Muhammad Raza\Desktop\KarachiDotAI\week10\final_assignment\modules\final_api_test_sheet.csv"
#df_read=pd.read_csv(DATA_URL)

credentials =  service_acc = '''
        {
        "type": "service_account",
        "project_id": "cde-week-2-341812",
        "private_key_id": "5334611ad4de6905efaa57ea884db890a86c0c85",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCWFFWuYTdUtz8l\nrmMwikT8ZnGFghJ1vTVEdaTX2PhO7xTHNatllOUXzhJxfbdOKAR/AActOI1EzX1o\n022YGsGGn2sqHftya8q5ud+R/fx1Do09KkWSx1Z0Zp1BbGrElguuMBPF6gZepCy7\nDKHVPBCKsELISwf2LpDUzWRF5D5GXC6j/D5GkOoSqREu0ZByYLu2N8vmPK2ud8Gb\nZsuVZQDPvqzMlkYZbdKCnVcqlQn6tCCunaecYSyRve4+x9/zbfvZUpYp2AL/3O1b\nBSfkywH/XqSsFtEUW5+SRvl0Fya/lmQ7EMN1aughQMtcSCmerhVaaUCId/KUi2lz\nl+4vNf0xAgMBAAECggEABnaovAJe1iywMQjCJ9iEoRQuZnAUKHL2JNUmPM+Q3iFo\n1S2IDK9tcGmFHNMrvld13hxbssRhPSnWcVnNugPI+unJvT4eUq62w+nv6YM1SLtQ\nNOapqWkhXZD/y84GCSJnLWDPsTHjhVbvwDyKibr1AWwW7DZjCOS3gxq3a1Upo3EK\n+TRpWoQOSA+4v8lvQkqVfl2U+AiuXGcucRVu48dgit+2qrDxyHeewKk2EB/AwqWc\nAwCwZ+awItGPp0vy6scmrznYnUFKAFoSF6GStctBV2upjJ2eMtNXWfiFWmG29sD2\nH2ejGDwEeugAJdMeK4l1B5Ns/TCoLGy4FcBrZ2hoiwKBgQDTB9d/Vf3yF6U5scsA\nXg5Layc+oCoKJ0illRQ682ICMFcuZKOGz/qJ2DZCmvbzs8i94llfgZeeaXtMU63+\nQ1Bi1YnbS5da6rcqp/GDxTZws3pleVb26CUJ1hSoOgrCEreX3vv3cxPx3UeShA0t\num6XWZfv3FOcy28JATzwKIW6rwKBgQC2D3qK4np/hUlVvdv5oiUy8H5+tLZ/VMvl\n5fQ9We0ykiOOVR4x2UN3FBI13N1zhoMFgMlNFb62m9bWoLfQ17MqPHf58M82mr3e\new38nO42Q2kriVo9ct1dm+tFII4+cr0RtjaVJb9tuVc6OJMlAoe6fzY2cx+4xuYA\nWl1tVJI+HwKBgBoLJbU5T5XJBUMRhhQNh4YXO0inS4jlQDnvJAgCcV4DyT6YfPXu\nROUuIcQmi8OXtHZ6sLzwqV2LdwP8b8SpWgpYgCLoOU2nGePRxiSU+hr+i2RqjSj7\njVahbPs17o308WN0yXPIZ/W5cVPLqDS0hWF4VR/s+QSotpNN689XsOlRAoGAXIaz\nVcBSV1rK8XuDP3RriV72OrjnAwF6esWKgl+gkBH7ZgvWQ6lSg0M9Ggi8t0jGb9aK\n99U0TqQW5I9bvBTTpoSCyRDcjrjIBDjv29F5szRBT/IHXbFx1XA3erNX917ivgyn\n4tcDWeVW8mzsQ2PszRh32eZaWdMj80v5rWXMySsCgYAw1tppABFcVU9QSnQZOwz5\nSfaft510XkWMfukoDJLf5Tcq4CADUmvEWtyOm6/SsUG/ADWFiyIiV/R++DEBrCLh\nJbQ+Y8RCjZlJerdlSWs/GZsOSxq/ypRuRH/sEmBi9ySkLLvCtxJr7uOjFGbhJlRy\nTGYRJEKS+DPGtqOm+hQ7wQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "cde-cloud-storage@cde-week-2-341812.iam.gserviceaccount.com",
        "client_id": "106666145060703654752",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cde-cloud-storage%40cde-week-2-341812.iam.gserviceaccount.com"
        }'''

credentials = service_account.Credentials.from_service_account_info(
    json.loads(service_acc, strict=False),
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)


sheet_client = build(
    'sheets', 'v4', 
    credentials=credentials,
    cache_discovery=False)
range_name = 'Sheet1'
sheet_id = '1j_CbxGjvhlg1u7NbJIRdeQ2DRz-MGQgkoTbvfIaoEB0'

try:
    results = sheet_client.spreadsheets().values().get(
        spreadsheetId=sheet_id, range=range_name).execute()
except Exception as e:
        print("exception in get_set_jobid: ",str(e))

df = pd.DataFrame(results['values'][1:] , columns = results['values'][0])


# https://discuss.streamlit.io/t/how-to-increase-the-width-of-web-page/7697/3
st.set_page_config(layout="wide")

st.title("Consumer Financial Protection Bureau ")
st.markdown("Complaint Details")

state = st.selectbox('Select Filter Here:',options = df['State'].unique())
df_select = df.query("State == @state")


col2, col3,col4 = st.columns(3)

with col2:
    total_no_complaints = pd.to_numeric(df_select['Complaint_id']).sum()
    st.text('Total Complaints')
    st.text(total_no_complaints)

with col3:
    total_complaints_with_closed_status = pd.to_numeric(df_select.loc[df['Company_Response'] == 'Closed with explanation', 'Complaint_id']).sum()
    st.text('Total Complaints Closed')
    st.text(total_complaints_with_closed_status)

with col4:
    total_complaints_with_in_progress = pd.to_numeric(df_select.loc[df['Company_Response'] == 'In progress', 'Complaint_id']).sum()
    st.text('Complaints with in progress')
    st.text(total_complaints_with_in_progress)

# print(total_no_complaints, total_complaints_with_closed_status, total_complaints_with_in_progress)


with st.container():
    col5, col6 = st.columns(2)
    with col5:
        #https://plotly.com/python/pie-charts/
        st.text('Number of Complaints by Product')
        pie_figure = px.pie(df_select, values='Complaint_id', names='Submitted_via', color_discrete_sequence=px.colors.sequential.RdBu)
        col5.plotly_chart(pie_figure, use_container_width=True)