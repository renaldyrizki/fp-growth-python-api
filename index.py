from bottle import request, route, run, response
import json
from types import SimpleNamespace
from fpgrowth_lib import fpgrowth as fpgrowth_library


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


@route('/hello')
def hello():
    return "Hello World!"

@route('/getFPG', method='POST')
def getFPG():
    PythonDict = request.body.read()
    transaksi = json.loads(PythonDict, object_hook=lambda d: SimpleNamespace(**d))

    minSupRatio= float(transaksi.support)
    minConf= float(transaksi.confidence)

    freqItemset, orderedItemset, freqPattern, rules = fpgrowth_library(transaksi.data, minSupRatio, minConf)
    
    data = {
        # "item": itemSetList,
        "freqItemset": freqItemset,
        "orderedItemset": orderedItemset,
        "freqPattern": freqPattern,
        "rules": rules
    }
    
    response.content_type = 'application/json'
    return data

run(host='localhost', port=2000, debug=True, reloader=True)