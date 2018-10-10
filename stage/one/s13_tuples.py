from utils.form import blank_form
from utils import fields_generate

# YOU SHOULD PROPERLY EDIT FEW SECTION:
# route:       dict for good Sanic route setup and auto import.
# data:        dict for present at Frontend
# answer:      function is to judge stdout result is correct or wrong.
#              This must be manually write in order to judge.

route = {
    'type': blank_form,
    'url': '/stage/one/_tuples',
    'methods': [ 'GET', 'POST' ]
}
data = {
    'title': 'Tuples',
    'description': [
        'A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.',
        'Try to say Hello to me!'
    ],
    'code': [
        '_____(\'_____\')'
    ],
    'fields': []
}
data['fields'] = fields_generate(data)  

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
            return stdout[0].decode() == 'Tuples\n'
    except:
        return False
