from flask import Flask
from flask import Response
import json
import os

CYTONIC_PATH = __path__[0]

class Cytonic(Flask):
    def __init__(self,name):
        super().__init__(name)
        self.methods = {}
        super().add_url_rule('/method/<method>/', 'method_route', 
                                                    self.method_route)
        super().add_url_rule('/style.css', 'cytonic_style', 
                                                    self.cytonic_style)
    
    def cytonic_style(self):
        with open(os.path.join(CYTONIC_PATH, "data", "style.css")) as f:
            return Response(f.read(), mimetype="text/css")

    def format_content(self, content):
        result = "<!DOCTYPE html>"
        result += "<html>"
        result += "<head>"
        result += '<link rel="stylesheet" href="/style.css">'
        result += '<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Ubuntu+Mono"/>'
        result += "</head>"
        result += "<body>" 
        result += content
        result += "</body>"
        result += "</html>"
        return result

    def add_method(self, id, descriptor):
        self.methods[id] = descriptor

    def method_route(self, method):
        result = "<h1>{}</h1><br>{}".format(method,json.dumps(self.methods[method]))
        return self.format_content(result)
    