import streamlit as st
import pandas as pd

st.title("Schedule Generator")

st.header("Flight Data")

col1, col2 = st.columns(2)

with col1:
    i1 = st.number_input("Flight One In / Chkn: ", step = 1)
    i2 = st.number_input("Flight Two In / Chkn: ", step = 1)
    i3 = st.number_input("Flight Three In / Chkn: ", step = 1)
    i4 = st.number_input("Flight Four In / Chkn: ", step = 1)

with col2:
    o1 = st.number_input("Flight One Out Time: ", step = 1)
    o2 = st.number_input("Flight Two Out Time: ", step = 1)
    o3 = st.number_input("Flight Three Out Time: ", step = 1)
    o4 = st.number_input("Flight Four Out Time: ", step = 1)

st.header("Company Requirements & Data")

col3, col4, col5, col6 = st.columns(4)

with col3:
    c1 = st.number_input("FTE? ", step = 0.5)

with col4:
    c2 = st.number_input("Hours per flight worked? ", step = 0.5)

with col5:
    c3 = st.number_input("FT Headcount? ", step = 1)

with col6:
    c4 = st.number_input("PT Headcount? ", step = 1)

st.header("Custom Data & Scenarios")

col7, col8, col9, col10, col11, col12 = st.columns(6)

with col7:
    c5 = st.number_input("Headcount Flight 1: ", step = 1)

with col8:
    c6 = st.number_input("Headcount Flight 2: ", step = 1)

with col9:
    c7 = st.number_input("Headcount Flight 3: ", step = 1)

with col10:
    c8 = st.number_input("Headcount Flight 4: ", step = 1)

with col11:
    c9 = st.number_input("Days per week worked FT: ", step = 1)

with col12:
    c10 = st.number_input("Days per week worked PT: ", step = 1)

###############################################################################

# Flight Schedule plus custom hours per flight worked plus headcount per flight

io1 = (o1 - i1) / 100
ioe1 = ((io1 + c2) - io1) * c5
io2 = (o2 - i2) / 100
ioe2 = ((io2 + c2) - io2) * c6
io3 = (o3 - i3) / 100
ioe3 = ((io3 + c2) - io3) * c7
io4 = (o4 - i4) / 100
ioe4 = ((io4 + c2) - io4) * c8

# Generates lims based on inputs

fteh = c1 * 40
ftept = fteh - (c3 * 40)
fteft = fteh - ftept

# Generates hours based on corp desired, priority of hours per flight worked

envoy_hours_pt = float((ftept / c4) / c10)

envoy_hours_pt_2 = (envoy_hours_pt // c2) * c2  # = 6

corporate_weekly_allowance = (envoy_hours_pt_2 * c10) * (c4 / 10)
# Generates hours based on the FTE which does not waste hours like hpfw

custom_hours_pt = ftept / c4

custom_hours_daily_pt = custom_hours_pt / c10

df1 = pd.DataFrame({
    'Alloc': [envoy_hours_pt_2, custom_hours_daily_pt, corporate_weekly_allowance, custom_hours_pt]
}, index = ['Corp Daily', 'FTE Daily', 'Corp Weekly', 'FTE Weekly'])

st.bar_chart(df1)

st.header("Data Output")

st.write(f"{fteh}, {fteft}, {ftept}")
st.write(f"{envoy_hours_pt}, {custom_hours_pt}")

#################################################################################









