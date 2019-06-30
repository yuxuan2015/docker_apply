import os
from sanic import Sanic
from sanic import response
import json
from pyhanlp import *
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


HanLP.Config.ShowTermNature = False

app = Sanic(__name__)


##
@app.route('/cut', methods=['POST'])
async def get_segment(request):
    request_json = request.body
    print(request_json)
    input_json = json.loads(request_json.decode('utf8'))
    query = input_json["query"]
    print(query)
    res = ' '.join([str(term) for term in HanLP.segment(query)])
    return response.json({"res": res})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
