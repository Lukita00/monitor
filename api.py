from flask import Flask
from monitor import Monitor
import json

app = Flask(__name__)


monitor = Monitor()
@app.route('/')
def stats():
    resp = {}
    resp.update(monitor.getCpu())
    resp.update(monitor.getMem())
    resp.update(monitor.getTemp())
    resp.update(monitor.getBattery())
    return json.dumps(resp,indent=4, allow_nan = True, skipkeys = True)

if __name__ == '__main__':
    app.run(debug=True, port=5500)