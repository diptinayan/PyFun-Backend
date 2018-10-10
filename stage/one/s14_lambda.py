from utils.form import blank_form
from utils import fields_generate

# YOU SHOULD PROPERLY EDIT FEW SECTION:
# route:       dict for good Sanic route setup and auto import.
# data:        dict for present at Frontend
# answer:      function is to judge stdout result is correct or wrong.
#              This must be manually write in order to judge.

route = {
    'type': blank_form, # Right now only provide *blank_form* one kind of form 181004.
    'url': '/stage/one/lambda',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': ''Lambda,  
    'description': [
        'A lambda function is a small anonymous function.',
        'A lambda function can take any number of arguments, but can only have one expression.

',
      
    ],
   
    'code': [
        'x = lambda a : a + 10',
'print(x(5))'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)  # NEVER remove this line!!

async def sanic_request(request):
    try:
        return override(request)
    except NameError:
        global data, route
        return route['type'](data, request, answer)


# def override(request):
#     pass

def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            return stdout[0].decode() == 'Lambda\n'
    except:
        return False
