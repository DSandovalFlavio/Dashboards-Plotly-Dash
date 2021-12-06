import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Data Science',
                                        style = {'textAlign': 'center',
                                                'color': '#0FD08D',
                                                'font-size': '50px'}),
                                html.H2('La carrera mas sexy del siglo XXI',
                                        style = {'textAlign': 'center',
                                                'color' : '#009A64'}),
                                html.P('Factores clave:'),
                                html.Ul(children = [html.Li('Factor 1'),
                                                html.Li('Factor 2'),
                                                html.Li('Factor 3'),
                                                html.Li(['Source: ',
                                                        html.A('https://www.excelsior.com.mx/nacional/ciencia-de-datos-la-carrera-mas-sexy-del-xxi-en-la-unam/1323946',
                                                                href = 'https://www.excelsior.com.mx/nacional/ciencia-de-datos-la-carrera-mas-sexy-del-xxi-en-la-unam/1323946')
                                                ])
                                ])
])

if __name__ == '__main__':
    app.run_server(debug=True)