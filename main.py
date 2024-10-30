import streamlit as st
import plotly.express as px
from backend import get_data

# Add widgets on the screen
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help = "Select the number of days")
option = st. selectbox("Forecast Option", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} day in {place}")

if place:
    # Get the temperature/Sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
    # Create a temperature plot
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png",}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(images_paths, width=150)