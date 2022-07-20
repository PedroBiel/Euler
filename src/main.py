"""
Método de Euler
Toma la pendiente en la forma de la primera derivada al inicio del intervalo como una aproximación de la pendiente
promedio sobre todo el intervalo.

__author__ = Pedro Biel
__version__ = 0.0.220719
__email__ = structural.biel@gmail.com

Versión 0.0.220719: Primera edición.
"""

# Librerías
# ---------
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Métodos
# -------

def euler(x, y, dydx, dx):
    """Método de Euler."""
    i = 1
    for i in range(0, len(x) - 1):
        y[i + 1] = y[i] + dydx[i] * dx
    return y

def tabla_valores(x, y, y_euler):
    """Siendo x, y e y_euler numpy arrays, devuelve el dataframe cuyas columasn corresponden a x e y."""
    d = {
        'x': x,
        'y': y,
        'y_euler': y_euler
    }
    return pd.DataFrame(d)

# Barra lateral
# -------------
sb = st.sidebar
sb.subheader('Función y su derivada')
fx = sb.text_input('Función y = f(x)')
der_fx = sb.text_input("Derivada de la función y' = f'(x)")

sb.subheader('Intervalo de la integración')
xi = sb.text_input('x inicial')
xf = sb.text_input('x final')

sb.subheader('Variables iniciales')
x_ini = xi
y_ini = sb.text_input('y inicial')

sb.subheader('Tamaño de paso')
dx = sb.text_input('Tamaño de paso')

if sb.button('Mostrar resultado'):
    if '' not in [fx, der_fx, xi, xf, x_ini, y_ini, dx] or dx <= (xf - xi):
        xi = float(xi)
        xf = float(xf)
        x_ini = float(x_ini)
        y_ini = float(y_ini)
        dx = float(dx)
        nc = int((xf - xi + 1) / dx)

        x = np.arange(xi, xf + dx/10, dx)

        y = eval(fx)

        dydx = eval(der_fx)

        y_euler = np.zeros(len(x))
        y_euler[0] = y_ini
        y_euler = euler(x, y_euler, dydx, dx)

        df = tabla_valores(x, y, y_euler)
    else:
        sb.text('Oops!')

# Contenedor de texto de introducción
# -----------------------------------

with st.container():
    st.title('Método de Euler')
    st.markdown(
        'De acuerdo con este método, la pendiente estimada $\phi$ se usa para extrapolar desde un valor anterior $y_i$ \
        a un nuevo valor $y_{i+1}$ en una distancia $h$. Esta fórmula se aplica paso a paso para calcular un valor \
        posterior y, por lo tanto, para trazar la trayectoria de la solución.'
    )
    st.text('Nuevo valor = valor anterior + pendiente * tamaño de paso')
    st.markdown('O en términos matemáticos:')
    st.markdown('$y_{i+1} = y_i + \phi · h$')
    st.markdown(
        'En otras palabras, se toma la pendiente al inicio del intervalo como una aproximación de la pendiente \
        promedio sobre todo el intervalo.'
    )
    st.markdown(
        'Esta técnica en general se conoce como el método de Runge-Kutta.'
    )
    st.markdown(
        'En esta aplicación se comparará los falores relaes de la función con los valores predichos por el método de \
        Euler.'
    )
    st.markdown(
        """
        Los datos de entrada de la aplicación son los siguientes:
        
        - Una función $y = f(x)$ para obtener los valores reales de $y$
        - La derivada de la función $y' = f'(x)$ para obtener los valores de la pendiente $\phi$
        - Valores inicial $x_i$ y final $x_f$ de la integración
        - Valor inicial de la variable $y$
        - El tamaño del paso $h$
        
        Nota 1: la función y su dserivada deben escribirse en \
        [formato de Python](https://www.easypythondocs.com/arithmetic.html).
        
        Por ejemplo, la función
        
        $2 x^3 + \sin(x)$
        
        debe introducirse como
        
        ```python
        2 * x ** 3 + math.sin(x)
        ```
        
        Nota 2: para conocer la derivada de una función [WolframAlpha](https://www.wolframalpha.com/).
        """
    )

# Contenedor de la tabla de valores
# ---------------------------------

with st.container():
    st.subheader('Tabla de resultados')
    st.markdown(
        """
        Muestra la tabla de resultados para los valores de
        
        - $x$
        - $y$
        - $y_{Euler}$
        """
    )
    try:
        st.dataframe(df)
    except Exception as e:
        print('Oops!', e)

# Contenedor de la gráfica de resultados
# --------------------------------------

with st.container():
    st.subheader('Gráfica de resultados')
    try:
        fig, ax = plt.subplots()
        ax.plot(x, y_euler, 'bo--', label='Euler')
        ax.plot(x, y, 'go-', label='Exacta')
        plt.title('Soluciones exacta y aproximada para una ODE', fontsize=15)
        plt.xlabel('x', fontsize=15)
        plt.ylabel('f(x)', fontsize=15)
        plt.grid()
        plt.legend(loc='lower right')
        st.pyplot(fig)
    except Exception as e:
        print('Oops!', e)

