import streamlit as st

################################################################

def wbrs(oem, oew):
    p = st.number_input("Pilot Weights:", value=0.0)
    x = st.number_input("Pax Weights:", value=0.0)
    f = st.number_input("Fuel in Gals:", value=0.0) * 6
    c1 = st.number_input("Cargo Zone 1:", value=0.0)
    c2 = st.number_input("Cargo Zone 2:", value=0.0)

    # Weight conversion factors and limits
    pmr, pwr = 15, 400
    pxmr, pxwr = 29, 400
    fmr, fr = 15.5, 320
    bg1mr, c1r = 12, 120
    bg2mr, c2r = 6, 50

    ttlw = oew + p + x + f + c1 + c2
    st.write("Gross Weight is:", ttlw)

    pev = (p / pwr) * pmr
    pxev = (x / pxwr) * pxmr
    fev = (f / fr) * fmr
    bg1ev = (c1 / c1r) * bg1mr
    bg2ev = (c2 / c2r) * bg2mr

    ttlmm = (pev + pxev + fev + bg1ev + bg2ev + oem) * 1000

    if p + x + f + c1 + c2 == 0:
        final_cg = ttlmm
    elif p + x + f + c1 + c2 > 0:
        final_cg = ttlmm / ttlw
    else:
        final_cg = None  # Handle edge cases

    if final_cg is not None:
        st.write("Final Center of Gravity is:", final_cg)

    return final_cg 


################################################################

def wblm(oem, oew):
    p = st.number_input("Pilot Weights:", value=0.0)
    x = st.number_input("Pax Weights:", value=0.0)
    f = st.number_input("Fuel in Gals:", value=0.0) * 6
    c1 = st.number_input("Cargo Zone 1:", value=0.0)
    c2 = st.number_input("Cargo Zone 2:", value=0.0)

    # Weight & Balance Calculation
    pmr, pwr = 15, 400
    pxmr, pxwr = 28.5, 400
    fmr, fr = 12.5, 288
    bg1mr, c1r = 13, 120
    bg2mr, c2r = 7, 50

    ttlw = oew + p + x + f + c1 + c2
    st.write("Gross Weight is:", ttlw)

    pev = (p / pwr) * pmr
    pxev = (x / pxwr) * pxmr
    fev = (f / fr) * fmr
    bg1ev = (c1 / c1r) * bg1mr
    bg2ev = (c2 / c2r) * bg2mr

    ttlmm = (pev + pxev + fev + bg1ev + bg2ev + oem) * 1000

    if p + x + f + c1 + c2 == 0:
        final_cg = ttlmm
    elif p + x + f + c1 + c2 > 0:
        final_cg = ttlmm / ttlw
    else:
        final_cg = None  

    if final_cg is not None:
        st.write("Final Center of Gravity is:", final_cg)

    return final_cg  


################################################################

def wbnp(oem, oew):
    p = st.number_input("Pilot Weights:", value=0.0)
    x = st.number_input("Pax Weights:", value=0.0)
    f = st.number_input("Fuel in Gals:", value=0.0) * 6
    c1 = st.number_input("Cargo Zone 1:", value=0.0)
    c2 = st.number_input("Cargo Zone 2:", value=0.0)

    pmr, pwr = 15, 400
    pxmr, pxwr = 29.25, 400
    fmr, fr = 14.5, 258 #43 usable gallons
    bg1mr, c1r = 11.5, 120
    bg2mr, c2r = 6, 50

    ttlw = oew + p + x + f + c1 + c2
    st.write("Gross Weight is:", ttlw)

    pev = (p / pwr) * pmr
    pxev = (x / pxwr) * pxmr
    fev = (f / fr) * fmr
    bg1ev = (c1 / c1r) * bg1mr
    bg2ev = (c2 / c2r) * bg2mr

    ttlmm = (pev + pxev + fev + bg1ev + bg2ev + oem) * 1000

    if p + x + f + c1 + c2 == 0:
        final_cg = ttlmm
    elif p + x + f + c1 + c2 > 0:
        final_cg = ttlmm / ttlw
    else:
        final_cg = None  

    if final_cg is not None:
        st.write("Final Center of Gravity is:", final_cg)

    return final_cg  

################################################################

def wbg(oem, oew):
    p = st.number_input("Pilot Weights:", value=0.0)
    x = st.number_input("Pax Weights:", value=0.0)
    f = st.number_input("Fuel in Gals:", value=0.0) * 6
    c1 = st.number_input("Cargo Zone 1:", value=0.0)
    c2 = st.number_input("Cargo Zone 2:", value=0.0)

    pmr, pwr = 15, 400
    pxmr, pxwr = 29, 400
    fmr, fr = 16.25, 336
    bg1mr, c1r = 11.5, 120
    bg2mr, c2r = 6, 50
    oem = 72.23411

    ttlw = oew + p + x + f + c1 + c2
    st.write("Gross Weight is:", ttlw)

    pev = (p / pwr) * pmr
    pxev = (x / pxwr) * pxmr
    fev = (f / fr) * fmr
    bg1ev = (c1 / c1r) * bg1mr
    bg2ev = (c2 / c2r) * bg2mr

    ttlmm = (pev + pxev + fev + bg1ev + bg2ev + oem) * 1000

    if p + x + f + c1 + c2 == 0:
        final_cg = ttlmm
    elif p + x + f + c1 + c2 > 0:
        final_cg = ttlmm / ttlw
    else:
        final_cg = None  

    if final_cg is not None:
        st.write("Final Center of Gravity is:", final_cg)

    return final_cg  


################################################################

st.title("Weight and Balance Calculator")
st.header("Aircraft Selection")

################################################################

aircraft_data = {
    "SP": {"oem": 65.292, "oew": 1637.2},
    "NFH": {"oem": 57.57257, "oew": 1443.52},
    "FTS": {"oem": 58.00281 ,"oew": 1488.82 },
    "FJ": {"oem": 56.64439, "oew": 1440.6},
    "GT": {"oem": 56.78931, "oew": 1442.98},
    "BC": {"oem": 56.2343, "oew": 1425.3},
    "FB": {"oem": 72.23411,"oew": 1740.8 },
    "ME": {"oem": 68.07986, "oew": 1672.8},
    "MA": {"oem": 67.99701, "oew": 1673.44},
    "ER": {"oem": 66.6327, "oew": 1644.93},
    "SSX": {"oem": 65.68937, "oew": 1677.04},
    # Add more aircraft as needed
}

################################################################

options = ["172R/S", "172L/M", "172N/P", "G1000"]
selected_model = st.selectbox("Select a Model:", options)

################################################################

if selected_model == "172R/S":
    opt_rs = ["N575SP", "N351ME", "N827MA", "N529ER", "N2476X"]
    selected_tail = st.selectbox("Select a Tail:", opt_rs)

    if selected_tail == "N575SP":
        data = aircraft_data["SP"]
        wbrs(data["oem"], data["oew"])
            
    elif selected_tail == "N351ME":
        data = aircraft_data["ME"]
        wbrs(data["oem"], data["oew"])  

    elif selected_tail == "N827MA":
        data = aircraft_data["MA"]
        wbrs(data["oem"], data["oew"])  
    
    elif selected_tail == "N2476X":
        data = aircraft_data["SSX"]
        wbrs(data["oem"], data["oew"])  

################################################################

elif selected_model == "172L/M":
    opt_lm = ["N6794H"]
    selected_tail = st.selectbox("Select a Tail:", opt_lm)

    if selected_tail == "N6794H":
        data = aircraft_data["NFH"]
        wblm(data["oem"], data["oew"])

################################################################

elif selected_model == "172N/P":
    opt_np = ["N62527", "N7140J", "N275GT", "N733BC"]
    selected_tail = st.selectbox("Select a Tail:", opt_np)

    if selected_tail == "N62527":
        data = aircraft_data["FTS"]
        wbnp(data["oem"], data["oew"])

    elif selected_tail == "N7140J":
        data = aircraft_data["FJ"]
        wbnp(data["oem"], data["oew"])

    elif selected_tail == "N7275GT":
        data = aircraft_data["GT"]
        wbnp(data["oem"], data["oew"])

    elif selected_tail == "N733BC":
        data = aircraft_data["BC"]
        wbnp(data["oem"], data["oew"])

################################################################

elif selected_model == "G1000":
    opt_g1000 = ["N114FB"]
    selected_tail = st.selectbox("Select a Tail:", opt_g1000)
    
    if selected_tail == "N114FB":
        data = aircraft_data["FB"]
        wbg(data["oem"], data["oew"])

################################################################

