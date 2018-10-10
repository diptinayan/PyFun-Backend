from utils.form import blank_form
from utils import fields_generate

# YOU SHOULD PROPERLY EDIT FEW SECTION:
# route:       dict for good Sanic route setup and auto import.
# data:        dict for present at Frontend
# answer:      function is to judge stdout result is correct or wrong.
#              This must be manually write in order to judge.

route = {
    'type': blank_form, 
    'url': '/stage/one/module',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Modules',  
   
    'description': [
        'Consider a module to be the same as a code library.',
        'A file containing a set of functions you want to include in your application.',
       
    ],
    
    'code': [
        'def greeting(name):'
 ' print("Hello, " + name)'
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
            return stdout[0].decode() == 'Module\n'
    except:
        return False
