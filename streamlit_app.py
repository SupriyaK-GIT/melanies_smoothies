# streamlit_app.py

import streamlit as st



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
# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from mytable;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")




