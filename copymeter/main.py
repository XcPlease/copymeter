
from flask import Flask, redirect, render_template, request
from pyparsing import Word
import requests
import random
app = Flask(__name__)
sb = ['בגלל' , 'מפני' , 'משום' , 'מכיוון', 'לאור']
vv = ['אף על פי' , 'אפילו', 'למרות' , 'גם אם']

@app.route("/")
def home():
   return render_template("index.html") # HOME

@app.route("/action", methods = ['POST'])
def doing():
   output = request.form['content']
   return Handle(output)


def Handle(output): 
        # סיבה ותוצאה
        a = output.replace('בגלל', random.choice(sb)) 
        b = a.replace('מפני', random.choice(sb)) 
        c = b.replace('משום', random.choice(sb)) 
        d = c.replace('מכיוון', random.choice(sb)) 
        e = d.replace('לאור', random.choice(sb)) 
        # סיבה ותוצאה

        f = e.replace('גם אם', random.choice(vv))
        g = f.replace('למרות', random.choice(vv))
        h = g.replace('אפילו', random.choice(vv))
        i = h.replace('אף על פי', random.choice(vv))
        return render_template("index.html", output=i)



app.run()