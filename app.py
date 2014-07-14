import os
from flask import Flask, request, make_response, send_file
from presentation import Presentation

app = Flask(__name__)

@app.route('/presentations', methods=['GET', 'POST'])
def hello():
  title = request.args.get("title", "No Title Was Found")
  body = request.args.get("body", "No Body Was Found")
  presentation = Presentation(title, body)  
  response = send_file(presentation.generate(),
                     attachment_filename=title + ".pptx",
                     as_attachment=False)
  return response