# Import python packages
import streamlit as st
#import snowflake.connector

#from snowflake.snowpark.functions import col

# Write directly to the app
st.title(" :cup_with_straw: Pending Smoothie orders :cup_with_straw:")
st.write(
    """Orders that need to be filled
    """
)

use st.secrets
cnx=st.connection('snowflake')
session = cnx.session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
#st.dataframe(data=my_dataframe, use_container_width=True)
if my_dataframe:
    editable_df = st.data_editor(my_dataframe)
    Submitted= st.button ("Filled")
    if Submitted:
            
            og_dataset = session.table("smoothies.public.orders")
            edited_dataset = session.create_dataframe(editable_df)
            try:
                og_dataset.merge(edited_dataset
                             , (og_dataset['ORDER_UID'] == edited_dataset['ORDER_UID'])
                             , [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]
                            )
                st.success('Order Updated', icon = '👍')
            except:
                st.write('something went wrong')
else:
    st.success('No Pending order', icon = '👍')

