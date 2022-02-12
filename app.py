import dash
from dash import html,callback_context
from dash.dependencies import Input, Output
import dash_cytoscape as cyto
import cylo_formatter as cylo
my_dataset = "test.mtx"

# generating the Network data --------------------------------------------------------------------------------

GRAPH = cylo.create_elements(dataset=my_dataset)

# ------------------------------------------------------------------------------------------------------------




app = dash.Dash(__name__)

app.layout = html.Div([
    html.Header(
        className = "head marg",
        children = [
            
            html.H3(
                className = "marg" ,
                children = [
                    "Amazon Recommender",
                    html.A(
                        className = "link",
                        href = "https://snap.stanford.edu/data/com-Amazon.html",
                        children = ["Data set link"]
                    )
                    ]
                )
            
            ]
    ) ,
    html.Div(
        className = "center",
        children = [
            html.H4(
                "Recommendation system built using Amazon product co-purshasing network dataset"
            ),
            html.H6(
                className="right",
                children = [
                    "Made by: Hilmi abdelfattah, Berkani Mohamed ...",
                ]
                )
            ]
        ),
        
        html.Br(),

    # Network div --------------------------------------------------------------------------------------------------------------------------------------
    html.Div(
        className="flex-container",
        children = [
            html.Div(
                id = "network",
                className = "network",
                style = {'display':'flex','box-shadow':' 20px,20px, black'},
                children = [

                    cyto.Cytoscape(
                        id = 'cytoscape',
                        style={'width': '100%', 'height': '400px'},
                        layout = { 'name': 'random' }, #TODO ''cose'' splits the graph into communities
                        elements = GRAPH
                    )
                ]),

            html.Div(
                className = "buttons",
                children = [
                    html.P("Change layout"),
                    
                    
                    html.Br(),
                    html.Br(),
                    
                    html.Button(
                        id='random',
                        className = "button",
                        value = "random",
                        n_clicks = 0,
                        children = "Random",
                        ),
                    
                    html.Br(),
                    html.Br(),

                    html.Button(
                        id='circle',
                        className = "button",
                        value = "circle",
                        n_clicks = 0,
                        children = "Circle",
                        ),

                    html.Br(),
                    html.Br(),

                    html.Button(
                        id='cose',
                        className = "button",
                        value = "cose",
                        n_clicks = 0,
                        children = "Communities",
                        ),

                    html.Br(),
                    html.Br(),

                    html.Button(
                        id='grid',
                        className = "button",
                        value = "grid",
                        n_clicks = 0,
                        children = "grid",
                        ),

                    html.Br(),
                    html.Br(),

                    html.Button(
                        id='concentric',
                        className = "button",
                        value = "euler",
                        n_clicks = 0,
                        children = "concentric",
                        ),
                ]
                ),
            html.Div(
                className = "data-info1",
                children = ["hello","hello","hello"]
                )
        ]),
        html.Br(), 
        html.Br(), 
    html.Div(
        className="flex-container",
        children = [
            
            html.Div(
                className = "data-info1",
                children = ["hello"]
                ),
            html.Div(
                className = "data-info1",
                children = ["hello"]
                )
        ])
    ])

@app.callback(Output('cytoscape', 'layout'),
    Input('random', 'n_clicks'),
    Input('circle', 'n_clicks'),
    Input('cose', 'n_clicks'),
    Input('grid', 'n_clicks'),
    Input('concentric', 'n_clicks')
    )
def update_layout(random,circle,cose,grid,concentric):
    changed_id = callback_context.triggered[0]

    layout = changed_id['prop_id'].split('.')[0]
    print(layout)
    if layout:
        return {
        'name': layout,
        'animate': True
    }

    
    
    



if __name__ == '__main__':
    app.run_server(debug=True)


































# dash starting template


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# import dash
# from dash import dcc
# from dash import html
# import plotly.express as px
# import pandas as pd

# app = dash.Dash(__name__)

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div(
#     children = 
#     [

#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
