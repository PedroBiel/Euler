# Método de Euler

De acuerdo con este método, la pendiente estimada $\phi$ se usa para extrapolar desde un valor anterior $y_i$ a un nuevo valor $y_{i+1}$ en una distancia $h$. Esta fórmula se aplica paso a paso para calcular un valor posterior y, por lo tanto, para trazar la trayectoria de la solución.

Nuevo valor = valor anterior + pendiente * tamaño de paso

O en términos matemáticos:

$y_{i+1} = y_i + \phi · h$

Esta fórmula se conoce como método de Euler (o de Euler-Cauchy o de punto pendiente). Se predice un nuevo valor de y usando la pendiente (igual a la primera derivada en el valor original de x) para extrapolar linealmente sobre el tamaño de paso h.

![alt text]("https://github.com/PedroBiel/Euler/img1.png")

En otras palabras, se toma la pendiente al inicio del intervalo como una aproximación de la pendiente promedio sobre todo el intervalo.

Esta técnica en general se conoce como el método de Runge-Kutta.

En esta aplicación se compara los falores relaes de la función con los valores predichos por el método de Euler.

Los datos de entrada de la aplicación son los siguientes:
  
- Una función $y = f(x)$ para obtener los valores reales de $y$
- La derivada de la función $y' = f'(x)$ para obtener los valores de la pendiente $\phi$
- Valores inicial $x_i$ y final $x_f$ de la integración
- Valor inicial de la variable $y$
- El tamaño del paso $h$

Más información: [Wikipedia, método de Euler](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Euler)
        
Nota 1: la función y su dserivada deben escribirse en [formato de Python](https://www.easypythondocs.com/arithmetic.html).
        
Por ejemplo, la función
        
$2 x^3 + \sin(x)$
        
debe introducirse como
        
```python
2 * x ** 3 + math.sin(x)
```
      
Nota 2: para conocer la derivada de una función [WolframAlpha](https://www.wolframalpha.com/).
