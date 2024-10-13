import streamlit as st
from snowflake.snowpark import Session

st.title(" :cup_with_straw: Pending Smoothie orders :cup_with_straw:")
st.write(
    """Orders that need to be filled
    """
)

# Snowflake connection parameters
snowflake_config = {
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

# Fetch data
def fetch_data(query):
    return session.sql(query).collect()
