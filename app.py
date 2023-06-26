import streamlit as st
import numpy as np
import joblib
from predict_cost import predict

st.set_page_config(page_title="Insurance App", page_icon = ":house_with_garden:")


st.title('Insurance App')


st.write("""
		### Fill in the details below to get an estimate of the price of your Insurance
		---
		""")


st.header('Age')
Age = st.slider('Select the area of the house (in sq. ft.)', 0, 100, 30)

st.header('Salary')
Salary = st.number_input('Enter your salary earned in years (highest $50,000)', min_value=10, step=1000)



st.header('Country')
Country = st.selectbox('Select the town/city where the house is located',("Canada", "Nigeria", "USA"))


if Country == "Canada":
	st.image("canada's flag.jpg", caption = "Canada", use_column_width = True)
	country_values = (1, 0)

elif Country == "Nigeria":
	st.image("Nigeria's flag.png", caption = "Nigeria", use_column_width = True)
	country_values = (0,1)

elif  Country == 'USA':
	st.image("america's flag.webp", caption = "USA", use_column_width = True)
	country_values = (0,0)


	

input_data = np.array([[Age, Salary] + list(country_values)])


if st.button('Predict Insurance Purchase'):
	cost = predict(input_data)
	st.subheader('Purchase Insurance')
	#st.write(cost[0])
	if cost[0] == 1:
		st.write("Purchase Insurance.")
		st.image("money.jpeg", use_column_width = False)

	else:
		st.write("Insurance was not purchased")

