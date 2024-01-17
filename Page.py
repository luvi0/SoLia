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
#DataPrep page
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
        st.write('''para a parte física de coleta de dados 
                 via sensores de umidade, no projeto colocamos leds para indicar a taxa de umidade
                 , no qual segundo artigos e publicações, cerca de 40% de volume 
                 de água em solo já é considerado úmido''')
        st.image('projeto arduino.png')
        st.write('''Modelo Físico projeto no laboratório de Potência - IFCE
                 ''')
        st.image('modelo_físico.jpeg')
        st.image('formula_Umidade.png')
        st.text('''
                 Detalhe que aconteceu foi como metrificar o sensor de umidade, em que 
                 tive ajuda de professores da faculdade e o conselho de utilizar o volume de água 
                 como meio físico medidor, detalhe que se deu por percentual ocupado a mais de água no solo
                 obedecendo a regra de 
                 U < 10% - Seco 
                 20% >  U > 10% - Pouco Úmido
                 40% >  U > 20% - Úmido
                 U > 40% - Molhado para plantio (soja neste caso)        
                 ''')
        st.video('dispositivo.mp4',format="video/mp4")
def pagina_Modelo():
    st.title("Modelo")
    st.write('''para a análise, primeiro entendendo que o problema é uma problema supervisionado de regressão
             logo as métricas como a aplicação do modelo foram para otimizar essa estimação de valores baseados pelos dados
             a aplicação da regressão logística
            ''')
    st.image('rl.png')
    st.line_chart(pd.read_csv('dados_model.csv'))
def Graf():
    st.title('Gráficos da Solução')
    st.write('''algo que teve de análise importante foi que devido a uma alta correlação identificada
             nos dados de faixa de temperatura dos dados Agro, foi interessante verificar o quão dispersos estão os dados dentro do modelo
             retornando somente um erro de 0.026 em aplicar regressão logística
            ''')
    st.image('gráficos_de_dispersão.png') #gráfico de dispersão
    st.title('Resíduos')
    st.write('''A análise de resíduos em gráficos é essencial 
             para aprimorar a interpretação de dados. Ela permite
              avaliar a adequação do modelo estatístico, identificar padrões não capturados,
              detectar outliers, verificar suposições estatísticas e melhorar a precisão preditiva, no mais, peça ao chatgpt
            ''')
    st.image('images.png') #imagem dos resíduos
    st.write(''' verificando os resíduos podemos verificar a presença dos outliers ao mesmo tempo que 
             a distribuição gaussiana cresce, ou seja quanto mais correlações(características) os dados vão tendo entre si
             maior vai ser a taxa de outliers crescendo entre eles            
            ''')
    
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
