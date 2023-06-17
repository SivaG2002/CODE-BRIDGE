from flask import Flask,render_template,request,jsonify
from source import inpo,clear
import subprocess
import os, sys
from subprocess import check_output
import time
import json
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/background_process')
def background_process():
    try:
        inp = request.args.get('proglang', type=str)
        inpo(inp)
        #lang=int(lang)
        #res=red.test.Fibonacci(lang)
        process()
        text=open('output.txt','r+')
        res=text.read()
        text.close()
        return jsonify(result=res)
    except Exception as e:
        return str(e)

def process():
    subprocess.call(['python','pseudo.py',],
    stdout=open('output.txt','wb'))


@app.route('/convertor',methods=['GET','POST'])
def convertor():
    return render_template('display.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
