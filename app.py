import dash
from dash import html,callback_context
from dash.dependencies import Input, Output
import dash_cytoscape as cyto
import cylo_formatter as cylo
my_dataset = "test.mtx"

# generating the Network data --------------------------------------------------------------------------------

elements = cylo.create_elements(dataset=my_dataset)
GRAPH = elements['graph']

source_nodes = elements['sources']
destination_nodes = elements['destinations']

def get_similar(item:str):
        if item in destination_nodes:
            indices = [i for i, x in enumerate(destination_nodes) if x == 'item' ]
            similar_products = [source_nodes[i] for i in indices]
            return {'similar-items':similar_products,'number-of-similars':len(similar_products)}
        else :
            indices = [i for i, x in enumerate(source_nodes) if x == 'item' ]
            similar_products = [destination_nodes[i] for i in indices]
            return {'similar-items':similar_products,'number-of-similars':len(similar_products)}
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
                children = ["hello"," hello ","hello"]
                )
        ]),
        html.Br(), 
        html.Br(), 
    html.Div(
        className="flex-container",
        children = [
            
            html.Div(
                id='graph-info',
                className = "reco",
                children = [
                    html.H5("hello"),
                    ]
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
    # print(layout)
    if layout:
        return {
        'name': layout,
        'animate': True
    }

@app.callback(
    Output('graph-info', 'children'),
    Input('cytoscape', 'tapNodeData'),
    )
def displayTapNodeData(data):
    if data:
        item = data['id']
        if item in destination_nodes:
            indices = [i for i, x in enumerate(destination_nodes) if x == item ]
            similar_products = [source_nodes[i] for i in indices]
        else :
            indices = [i for i, x in enumerate(source_nodes) if x == item ]
            similar_products = [destination_nodes[i] for i in indices]
            
        
        
        
        return html.P(
            children=[
                f"Product Id: {data['id']}",
                f"{similar_products}"
                ]
            )
    else :
        return " Select a product so we can recommend something similar "

    



if __name__ == '__main__':
    app.run_server(debug=True)



























