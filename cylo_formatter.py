'''
this script takes the raw data from the dataset and formats its fron dash cytoscape element:
the final data format should look like this :
elements = [
            #---------------------nodes aka vertecies--------------------
            {'data': {'id': 'one', 'label': 'Node 1'}, },
            {'data': {'id': 'two', 'label': 'Node 2'}, },
            {'data': {'id': 'three', 'label': 'Node 3'}, },
            {'data': {'id': 'four', 'label': 'Node 4'}, },

            #---------------------edges aka edges hhh--------------------
            {'data': {'source': 'one', 'target': 'two'}},
            {'data': {'source': 'one', 'target': 'three'}},
            {'data': {'source': 'two', 'target': 'three'}},
            {'data': {'source': 'three', 'target': 'four'}},
            
        ]
'''


from venv import create


def get_data_from(filepath:str) -> list :
    '''
    get dataset raw lines 
    '''

    with open(filepath) as file:
        lista = file.readlines()
        return lista


def create_elements(dataset:str) -> list:

    data = get_data_from( dataset )

    data = [ (s[:-1]).split() for s in data ]
    
    
    # unzip the data list i.e: if data = [(a,b),(c,s)] then source = (a,c) and dest = (b,d)
    source_nodes, destination_nodes = zip( *data ) 

    nodes = [
        {
            'data':{'id':f'{i}','label': f'p {i}' } 
            }for i in source_nodes + destination_nodes
    ]

    edges = [
        {
            'data':{'source':f'{i}','target': f'{j}'}   
            }for i,j in data
    ]

    return {'sources':source_nodes,'destinations':destination_nodes,'graph':nodes+edges}



if __name__ == "__main__":

    data = get_data_from( "test.mtx" )

    data = [ (s[:-1]).split() for s in data ]
    
    source_nodes, destination_nodes = zip( *data )
    nodes= source_nodes+destination_nodes

    def get_similar(item:str):
        if item in destination_nodes:
            indices = [i for i, x in enumerate(destination_nodes) if x == '1' ]
            similar_products = [source_nodes[i] for i in indices]
            return {'similar-items':similar_products,'number-of-similars':len(similar_products)}
    print(get_similar('1'))

     
