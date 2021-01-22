import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


if __name__ == "__main__":
    app = dash.Dash(__name__)
   

    df_boston_housing = pd.read_csv('./data/BostonHousing.csv')
    df_lin_model_params = pd.read_csv('./data/lin-model-params.csv', names=['param', 'coef'])



    bar_chart = px.bar(df_lin_model_params, x='param', y='coef')
    histogram = px.histogram(df_boston_housing, x="ptratio")
    scatter = px.scatter(df_boston_housing, x="age", y="medv")
    
    app.layout = html.Div(
        children=[
                dcc.Graph(
                    id='bar',
                    figure=bar_chart
                 ),
                dcc.Graph(
                    id='hist',
                    figure=histogram
                 ),
                dcc.Graph(
                    id='scat',
                    figure=scatter
                 ),
        ]
    )
    app.run_server(debug=True)