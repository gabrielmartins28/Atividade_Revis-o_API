import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(    page_title="Estação Meteorológica",    page_icon="🌡️",    layout="centered")
st.title("🌡️ Estação Meteorológica")
st.write("Monitoramento das condições ambientais")
st.caption("Jaraguá do Sul — Santa Catarina")
st.divider()
try:    
    with st.spinner("Obtendo informações meteorológicas..."):        
        dados = obter_dados_meteorologicos()    
        st.success("Consulta realizada com sucesso!")    
        st.subheader("🌡️ Temperatura")    
        col1, col2 = st.columns(2)    
        col1.metric( "Temperatura do Ar", dados['temperatura'])
        col2.metric( "Sensação Térmica", dados['sensacao'])

except ValueError:
    print(ValueError)