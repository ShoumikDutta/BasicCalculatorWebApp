from flask import Flask,render_template,request
from calculator import calc
app= Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    
    if request.method=="GET":
        print("working1")
        return render_template("index.html",debug=True)
    else:
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        btn=request.form.get('buttonName')
        ans=calc(num1,num2,btn)
        return render_template("index.html",answer=ans)



        


if __name__=="__main__":
    app.run(debug=True)
    