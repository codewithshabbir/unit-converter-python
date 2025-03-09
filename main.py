import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Unit Converter</h1>", unsafe_allow_html=True)
st.write("Convert units easily with this simple tool!")

st.sidebar.markdown("## 📌 Available Units")

# Length Section
st.sidebar.markdown("### 📏 Length")
st.sidebar.markdown("""
- **✔ Meter (m)**  
- **✔ Kilometer (km)**  
- **✔ Centimeter (cm)**  
- **✔ Millimeter (mm)**  
- **✔ Inch (in)**  
- **✔ Foot (ft)**  
- **✔ Yard (yd)**  
- **✔ Mile (mi)**  
""")

# Weight Section
st.sidebar.markdown("### ⚖️ Weight")
st.sidebar.markdown("""
- **✔ Gram (g)**  
- **✔ Kilogram (kg)**  
- **✔ Pound (lb)**  
- **✔ Ounce (oz)**  
""")

# Temperature Section
st.sidebar.markdown("### 🌡️ Temperature")
st.sidebar.markdown("""
- **✔ Celsius (°C)**  
- **✔ Fahrenheit (°F)**  
""")

st.divider()

def convertUnits(value, unitFrom, unitTo):
    conversions = {
        # Length
        "meter_kilometer": 0.001, "kilometer_meter": 1000,
        "meter_centimeter": 100, "centimeter_meter": 0.01,
        "meter_millimeter": 1000, "millimeter_meter": 0.001,
        "inch_centimeter": 2.54, "centimeter_inch": 0.393701,
        "foot_meter": 0.3048, "meter_foot": 3.28084,
        "yard_meter": 0.9144, "meter_yard": 1.09361,
        "mile_kilometer": 1.60934, "kilometer_mile": 0.621371,

        # Weight
        "gram_kilogram": 0.001, "kilogram_gram": 1000,
        "pound_kilogram": 0.453592, "kilogram_pound": 2.20462,
        "ounce_gram": 28.3495, "gram_ounce": 0.035274,
    }

    if unitFrom == unitTo:
        return "Same unit conversion is not needed."

    key = f"{unitFrom}_{unitTo}" #Generate a key based on input and output units

    if unitFrom == "celsius" and unitTo == "fahrenheit":
        return (value * 9/5) + 32
    elif unitFrom == "fahrenheit" and unitTo == "celsius":
        return (value -32) * 5/9

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
value = st.number_input("🔢 Enter Value to Convert::", min_value=1.0, step=1.0)

units = ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile",
         "gram", "kilogram", "pound", "ounce", "celsius", "fahrenheit"]

col1, col2 = st.columns(2)
with col1:
    unitFrom = st.selectbox("📤 Convert From:", units)
with col2:
    unitTo = st.selectbox("📤 Convert To:", units)

st.divider()
if st.button("🔄 Convert", use_container_width=True):
    result = convertUnits(value, unitFrom, unitTo)
    st.success(f"✅ Converted Value: {result}")

st.divider()
st.write("Made with ❤️ by [Muhammad Shabbir](https://codewithshabbir.vercel.app/)")