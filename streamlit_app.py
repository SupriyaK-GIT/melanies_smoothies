# streamlit_app.py
import streamlit as st
from snowflake.snowpark import Session

st.title(" :cup_with_straw: Pending Smoothie orders :cup_with_straw:")
st.write(
    """Orders that need to be filled testing 
    """
)
# Snowflake connection parameters
snowflake = {
    'account': 'NONGWKL-MOB76819',
    'user': 'SupriyaK',
    'password': 'L3arnSFlake',
    'role': 'SYSADMIN',  # Optional
    'warehouse': 'COMPUTE_WH',  # Optional
    'database': 'SMOOTHIES',  # Optional
    'schema': 'PUBLIC',  # Optional
}


# Create a Snowflake session
session = Session.builder.configs(snowflake_config).create()


