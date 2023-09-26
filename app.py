from flask import Flask,render_template,request,redirect,url_for




## Flask app routing
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Your first app is ready"

@app.route("/index",methods=['GET'])
def index():
    return "<h1>index function trigered</h1>" 

##variable rule

@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is:  "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has fail and the score is:  "+str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('calculate.html')
    
@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)

if __name__=="__main__":
    app.run(debug=True)

