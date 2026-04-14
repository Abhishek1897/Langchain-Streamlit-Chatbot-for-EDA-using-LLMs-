import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company[insights]')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
countries = ['France', 'United States', 'China', 'Japan', 'Germany', 'Brasil', 'Spain', 'Colombia', 'Australia', 'South Korea', 'United Kingdom', 'Belgium', 'Poland', 'Austria', 'España', 'Deutschland']
return_percentages = [9.56, 10.02, 9.88, 10.05, 9.67, 9.74, 10.4, 7.69, 10.09, 10.17, 9.42, 9.31, 12.93, 0.00, 25.00, 0.00]

# Plotting
plt.figure(figsize=(10, 8))
plt.bar(countries, return_percentages, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Return Percentage')
plt.title('Return Percentages by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot()
