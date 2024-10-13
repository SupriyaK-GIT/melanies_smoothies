import streamlit as st

st.title(" :cup_with_straw: Pending Smoothie orders :cup_with_straw:")
st.write(
    """Orders that need to be filled testing 
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


from snowflake.snowpark import Session

# Create a Snowflake session
session = Session.builder.configs(snowflake_config).create()

# Fetch data
def fetch_data(query):
    return session.sql(query).collect()
