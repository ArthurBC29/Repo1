import pandas as pd
import streamlit as st
from PIL import Image
# Title of the app
st.title("Researcher Profile Page")
# Collect basic information
name = "Arthur BC"
field = "Health Sciences"
institution = "University of Western Cape"
# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    # Apply table styling using st.dataframe()
    def style_dataframe(df):
        return df.style.set_properties(
            **{
                "background-color": "#F9F9F9",
                "border": "1px solid #ddd",
                "text-align": "center",
            }
        ).set_table_styles(
            [
                {"selector": "thead th", "props": [("background-color", "#4CAF50"), ("color", "white"), ("font-weight", "bold"), ("text-align", "center")]},
                {"selector": "tbody tr:nth-child(even)", "props": [("background-color", "#F2F2F2")]},
                {"selector": "tbody tr:hover", "props": [("background-color", "#ddd")]},
            ]
        )
    st.dataframe(style_dataframe(publications))
    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(style_dataframe(filtered))
    else:
        st.write("Showing all publications")
# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")
# Add a contact section
st.header("Contact Information")
email = "achikware@uwc.ac.za"
st.write(f"You can reach {name} at {email}.")
