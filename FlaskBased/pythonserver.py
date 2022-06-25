from flask import Flask, json, jsonify, send_from_directory
import os
from pykml import parser
from zipfile import ZipFile
app = Flask(__name__)
app.config['filePath'] = "static"
kmlfile = os.path.join("/static/AGI_HQ.kmz")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    print(kmlfile)
    fkml = os.path.join(APP_ROOT, "static/")
    # with ZipFile(fkml, 'r') as kmz:
    #     kml = kmz.open(kmz.filelist[0].filename, 'r').read()
    # kmz = ZipFile(fkml, 'r')
    # kml = kmz.open('doc.kml', 'r').read()
    return send_from_directory(fkml, "tileset.json")


if __name__ == '__main__':
    app.secret_key = os.urandom(32)
    app.run(debug=True)
