import streamlit as st
import pandas as pd
import numpy as np
def pagina_inicio():
    st.title("SoLia - Machine Learning com Solo")    
    st.header('Introdução', divider='rainbow')
    st.text('''    
            os dados do solo se referem na qualidade dos solos do paraná-PR entre os
            períodos de 2004-2017''')
    st.link_button("Acesse nossa tabela de dados",
                    "https://drive.google.com/drive/folders/1oSO1hy6gGMhOKCEz_lgOoqcMMHE8O35f?usp=drive_link")
    st.header('Objetivo', divider='rainbow')
    text_01 = '''
        aplicar conhecimentos de machine learning, modelos estatísticos e IOT,
    para solucionar o problema de identificar a qualidade de solo necessária
    que gere uma alta produtividade em identificar o nivel de produtividade
    
    Sendo o projeto dividido em 04 etapas:
    °DataPrep
    °Criação Modelo
    °Hardware - Arduino
    °EDA - Conclusão


    '''
    st.text(text_01)       

def pagina_DataPrep():
    st.title("DataPrep")
    tab1, tab2, tab3 = st.tabs(["Agro", "Produtividade", "Arduíno"])
    #Dados Normalização dos dados Agro
    with tab1:
        st.header("Agro")
        st.write("os dados Agro foram tratados de acordo com o principal a seguir:", width=200)
        st.dataframe((pd.read_csv('agroclimatology.csv')).head(4))
        st.text('''
                primeiro passo numa EDA para tratarmos os dados para aplicação do modelo
                - variáveis explicativas
                - Normalização de Dados
                                ''')
        st.image('normalização.png')
        st.text('''
                a normalização de dados é realização de um tratamento incial na preparação 
                do DataPrep, Esta característica pode ser especialmente benéfica para modelos
                que demonstram sensibilidade às escalas das variáveis de entrada,
                pois assegura que nenhum elemento exerça uma influência desproporcional 
                sobre o modelo devido à sua escala. 
                ''')
        st.dataframe((pd.read_csv('variáveis_explicativas_agro.csv').head(4)))
        st.text('T2M_RANGE = Faixa de Temperatura e QV2M = Faixa de  Umidade')
    # Definição do Target de Produtividade
    with tab2:
        st.header("Produtividade")
        st.write("os dados de Produtividade foram tratados de acordo com o principal a seguir:", width=200)
        st.dataframe((pd.read_csv('produtividade_soja.csv').head(4)))
        st.text('''
                Dados de Produtividade serão nossos Target para indicar qual o Y de relação
                para que o modelo estatístico identifique, aqui  ocorre o mesmo 
                passo de normalização de dados e sum de linhas para uma tendência média móvel de 10 n_jobs
                                ''')
        st.dataframe((pd.read_csv('dados_pro_target_model.csv').head(4)))       
    # Tratando dados Arduíno
    with tab3:
        st.header("Arduíno")
        st.write("https://static.streamlit.io/examples/owl.jpg", width=200)
def pagina_Modelo():
    st.title("Modelo")
    # Adicione o conteúdo da sua página inicial aqui
    arquivo = st.file_uploader('suba seu arquivo aqui', type=['jpg','png','json','csv','pdf'])

def Graf():
    st.title('Gráficos da Solução')
    st.image('gráficos_de_dispersão.png') #gráfico de dispersão
    st.image('images.png') #imagem dos resíduos
    
def main():
    st.sidebar.title("Navegação")
    opcoes = ["Página Inicial", "DataPrep", "Modelo",'Gráficos']
    escolha = st.sidebar.selectbox("Escolha uma página", opcoes) #radio 

    if escolha == "Página Inicial":
        pagina_inicio()    
    elif escolha == "DataPrep":
        pagina_DataPrep()
    elif escolha == "Modelo":
        pagina_Modelo()
    elif escolha == 'Gráficos':
        Graf()

if __name__ == "__main__":
    main()
