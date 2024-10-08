import streamlit as st 

# Use the get method since the keys won't be in session_state 
# on the first script run 
if st.session_state.get('clear'): 
	st.session_state['name'] = '' 
	
if st.session_state.get('streamlit'): 
	st.session_state['name'] = 'Streamlit' 
	
st.text_input('Name', key='name') 

# assign a key to a button, you can condition code on a button's state by using its value in st.session_state
st.button('Clear name', key='clear') 


st.write("end")