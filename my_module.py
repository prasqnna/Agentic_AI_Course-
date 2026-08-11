'''
in this file we can create some user difined functions,variables,classes...
'''
def greet(name):
    """user defined function"""
    return (f"hello {name}")
#greet("codegnan")

names={"Students":['sai','akash','ajay'],
        'age':[14,25,35]}
#if __name__=="__main__":
    #print(__name__)

def display():
    """subjects covered"""
    yield "python"
    yield "genai"
    yield "rag"
    yield "agents"


print(__name__)