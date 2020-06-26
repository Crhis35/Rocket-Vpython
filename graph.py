import plotly.offline as plt
import plotly.graph_objs as go
import pandas as pd

def graph(file):
    data = pd.DataFrame(file)

    traces = [go.Scatter(
        x=data['Tiempo'],
        y=data[col],
        mode='lines',
        name=col
    ) for col in data.columns if col!="Tiempo"]

    fig = {
        'data': traces,
        'layout': go.Layout(title='Estadisticas del Cohete',hovermode='closest')
    }
    
    plt.plot(fig, filename='./datos.html')