import dash
import dash_cytoscape as cyto
from dash import html
import cylo_formatter as cylo

my_dataset = "test.mtx"

GRAPH = cylo.create_elements(dataset=my_dataset)

app = dash.Dash(__name__)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '600px','background': 'linear-gradient(90deg, rgba(241,188,162,1) 0%, rgba(244,255,128,0.8379945728291316) 46%, rgba(255,89,193,0.7539609593837535) 100%)'},
        elements=GRAPH
        
        # elements=[
        #     #---------------------nodes aka vertecies--------------------
        #     {'data': {'id': 'one', 'label': 'Node 1'}, },
        #     {'data': {'id': 'two', 'label': 'Node 2'}, },
        #     {'data': {'id': 'three', 'label': 'Node 3'}, },
        #     {'data': {'id': 'four', 'label': 'Node 4'}, },

        #     #---------------------edges aka edges hhh--------------------
        #     {'data': {'source': 'one', 'target': 'two'}},
        #     {'data': {'source': 'one', 'target': 'three'}},
        #     {'data': {'source': 'two', 'target': 'three'}},
        #     {'data': {'source': 'three', 'target': 'four'}},
            
        # ]
    )
])

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
