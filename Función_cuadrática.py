import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_player import st_player
from streamlit_option_menu import option_menu

tab1, tab2, tab3, tab4 = st.tabs(['Definición', 'Componentes', 'Gráficos', 'Práctica'])
with tab1:     
    col1, col2, col3 = st.columns(3)   
    with col2:
        st.image('imagen.PNG', 'Matemática')

    """
    **Una funcion cuadrática** es un tipo de función que se caracteriza por ser un polinomio de segundo grado. En este tipo de funciones uno de los  elementos lleva un 2 pequeño como índice superior.
    \n __*Para leer y recordar*__ \n

    * Se llama funcion cuadrática a toda función que se exprese en la forma: \n
            f(x) = a.x\u00b2+b.x+c (a, b y c son números reales y a distinto 0).\n
            Por ejemplo, si f(x) = 3x\u00b2 - 15x, resulta a = 3, b = -15 y c = 0.\n
    * Al representar gráficamente una función cuadrática, se obtienen dos puntos que pertenecen a una curva llamada *parabola*.\n
    * La orientacion de la parabola depende del signo de a.\n
    * a > 0 las ramas de la parabola van hacia arriba (función concava)\n
    * a < 0 las ramas de la parabola van hacia abajo (Función convexa)\n
    """
    
    st.write('$ f(x) = a \cdot x^2 + b \cdot x + c $')

with st.sidebar:
    x = st.slider('¿Te resulto util la aplicación? (Puntuación de 1-10)', 1, 10)
    st.write("Puntos:", x)
    
with st.sidebar:
    st.write('****Material realizado por:****') 
    st.write('*Prof. Yanina Maidana*') 
    st.write('*Prof. Valeria Rosillo*') 






with tab2:
    """
    **Elementos caracteristicos de una función cuadrática**\n
    Los elementos de mayor relevancia para poder representar  gráficamente una función polinomica de segundo grado son las raíces, la ordenada en el origen, las coordenadas al vértice y el eje de simetría.\n
    
    **Concavidad** \n
    
    Esta dada por el signo del coeficiente principal a. Es decir que si a > 0, la concavidad es positiva y si a < 0, la concavidad es negativa.\n
    """
    
    st.image('./concavidad.PNG')                 
    
    """ 
    **Ordenada en el origen**\n
    Es la ordenada del punto de intersección entre la parábola y el eje de las ordenadas. Se halla, calculando la imagen de cero, **f(0)**.
    Si la función se encuentra expresada en forma polinómica la orednada en el origen coincide con el termino independiente **(c)**.
    """
    st.image('./ordenada en el origen.PNG')
    """
    **Raíces**\n
    Son los valores del dominio para los cuales la función vale cero. Se hallan resolviendo la ecuación cuadrática.\n
    __a.x\u00b2+b.x+c = 0__\n
    """
    st.image('./raices.PNG')

    """ 
    **Eje de simetría**\n
    
    Es la recta paralela al eje 0y que divide a la curva en dos ramas simétricas.\n
    Se Halla como\n
    x = -b/2a\n

    **Vértice**\n
    Es el punto de intersección de la parábola con el eje de simetría. Las coordenadas del vértice.\n
    """
    st.image('./vertice.PNG')

with tab3:
    """
    **Representación gráfica de funciones cuadráticas**\n 
    La representación gráfica de una función cuadrática es una curva llamada parábola de eje paralelo a **Oy**.\n
    **Graficar mediante tabla de valores**\n
    Esta forma de representar una función involucra la creación de una tabla de valores para obtener puntos (x,f(x)) del gráfico. damos valores a x, para luego calcular sus imagenes f(x). Luego graficamos  cada uno de los puntos obtenidos en un sistema de ejes cartesianos. La parábola es la curva que pasa por cada uno de los puntos.\n
    """
    valores1 = [-3, -2, -1, 0, 1, 2, 3]
    valores2 = [9, 4, 1, 0, 1, 4, 9]

    tabla = {'x': valores1, 'f(x)': valores2}
    df = pd.DataFrame(data=tabla)
    df
    x= [-3, -2, -1, 0, 1, 5, 6]
    y= [9, 4, 1, 0, 1, 4, 9]
    f = plt.figure()
    plt.plot(x, y, lw=2, c='r',)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.grid()
    plt.suptitle('Gráfica de la función', fontsize=10)
    f
    # plt.show()

    
with tab4:

    """
    **Actividad 1:**\n

    En el cuadro se muestran las caracteristicas de la función polinomica dependiendo del signo de los coeficientes. Elegir cual es la respuesta correcta.\n

    """
    col1, col2 = st.columns(2)

    with col1:
        st.image('./concava.PNG')
        st.write('Función')

    with col2:
        st.image('./convexa.PNG')
        st.write('Función')
        
    
    col1b, col2b = st.columns(2)

    with col1b:
        opciones = ['Seleccione', 'cóncava', 'convexa']
        opcion_seleccionada = st.selectbox('Seleccionar opción', opciones)
        

    with col2b:
        opciones = ['Seleccione', 'concava', 'convexa']
        opcion_seleccionada = st.selectbox('Selecionar opción', opciones)

