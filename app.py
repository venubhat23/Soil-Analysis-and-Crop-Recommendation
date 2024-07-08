from flask import Flask,render_template,request,redirect,url_for,session
import requests
import MySQLdb
from flask import send_file
from datetime import datetime
from werkzeug.utils import secure_filename
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
import tensorflow as tf
import pandas as pd
import numpy as np
import os
from test_mobilenet import process_image, process


label={"apple":0,"Banana":1,"Blackgram":2,"Chickpea":3,"Coconut":4,"coffee":5,"Cotton":6,"Grapes":7,"Jute":8,"Kidney Beans":9,"Lentil":10,"Maize":11,"Mango":12,"Mouth Beans":13,"Mungbeans":14,"Muskmelon":15,"Orange":16,"Papaya":17,"Pigeon Peas":18,"Pomegranate":19,"Rice":20,"Watermelon":21}


UPLOAD_FOLDER = './static/Schemes/'
ALLOWED_EXTENSIONS = {'jpg','jpeg','png'}
mydb = MySQLdb.connect(host='localhost',user='root',passwd='root',db='croppred')
conn = mydb.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():

        if not session.get('logged_in'):
                return render_template("index.html")
                
        else:
                return render_template('userhomepage.html')
        
            

@app.route("/uregpage")
def uregpage():
        return render_template("reg.html")
@app.route("/uloginpage")
def uloginpage():
        return render_template("uloginpage.html")
def get_key1(val): 
    for key, value in label.items(): 
         if val == value: 
             return key 
@app.route("/predict",methods=['POST','GET'])
def predict():
        
        n=request.form['n']
        p=request.form['p']
        k=request.form['k']
        temperature=request.form['temperature']
        humidity=request.form['humidity']
        ph=request.form['ph']
        rainfall=request.form['rainfall']
        crop_data=pd.read_csv("Crop_recommendation.csv")
        crop_data.rename(columns = {'label':'Crop'}, inplace = True)
        crop_data = crop_data.dropna()
        x = crop_data[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
        target = crop_data['Crop']
        print("Target==",target)
        y = pd.get_dummies(target)
        print("Y==",y)
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25, random_state= 0)
        
        gb_clf = RandomForestClassifier(n_estimators = 100)
        MultiOutputClassifier(estimator=RandomForestClassifier(), n_jobs=-1)
        model = MultiOutputClassifier(gb_clf, n_jobs=-1)
        model.fit(x_train, y_train)
        x_test=[int(n),int(p),int(k),float(temperature),float(humidity),float(ph),float(rainfall)]
        x_test=np.array(x_test)
        x_test=x_test.reshape(1,-1)
        ypred=model.predict(x_test)
        print("Y-pred==",ypred)
        #label1=ypred.argmax(axis=1)
        #print("Predicted crop==",label)
        actallabel=get_key1(np.argmax(ypred))
        
        print("actallabel==",actallabel)
        return render_template("croppage1.html",msg=actallabel)

@app.route("/imagepage")
def imagepage():
        return render_template("imagepage.html")


@app.route("/predictimg",methods=['GET','POST'])
def predictimg():
        print("Entered")
        print("Entered here")
        if request.method == 'POST':
                uploaded_file = request.files['file']
                
                #file = request.files['file'] # fet input
                filename = uploaded_file.filename
                print("Filename==",filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                uploaded_file.save(file_path)
                img = process_image(uploaded_file.stream) 

                pred = process(img)
                return render_template("result.html", pred_output = pred,img_src=UPLOAD_FOLDER + uploaded_file.filename)
        

@app.route("/croppage1")
def croppage1():
        return render_template("croppage.html")
@app.route("/croppage")
def croppage():
        return render_template("croppage1.html")

@app.route("/ureg",methods=['POST'])
def ureg():
        name=request.form['name']
        uname=request.form['uname']
        passw=request.form['pass']
        
        mono=request.form['mono']
        email=request.form['email']
       
        age=request.form['age']
        gen=request.form['gen']
        
        cmd="SELECT * FROM farmer WHERE uname='"+uname+"' or email='"+email+"' "
        print(cmd)
        conn.execute(cmd)
        cursor=conn.fetchall()
        isRecordExist=0
        for row in cursor:
                isRecordExist=1
        if(isRecordExist==1):
                msg="Record Already Exist"
                return render_template("reg.html",data=msg)
        else:
                cmd="INSERT INTO farmer(name,uname,pass,mono,email,age,gen) Values('"+str(name)+"','"+str(uname)+"','"+str(passw)+"','"+str(mono)+"','"+str(email)+"','"+str(age)+"','"+str(gen)+"')"
                print(cmd)
                #print("Inserted Successfully")
                conn.execute(cmd)
                mydb.commit()
                msg="Added Successfully"
                print("msg==",msg)
                session['msg']=msg
                return redirect(url_for('index'))

@app.route("/ulogin",methods=['POST'])
def ulogin():
        uname=request.form['uname']
        passw=request.form['pass']
       
        

        
        cmd="SELECT * FROM farmer WHERE uname='"+uname+"' and pass='"+passw+"'"
        print(cmd)
        conn.execute(cmd)
        cursor=conn.fetchall()
        isRecordExist=0
        if len(cursor)>0:
                for row in cursor:
                        isRecordExist=1
            
        if(isRecordExist==1):
                session['uname']=uname
                session['utype']='user'
                session['logged_in']=True
                return redirect(url_for('index'))
        else:
                return render_template("uloginpage.html",msg="Incorret Password")


@app.route("/logout")
def log_out():
    session.clear()
    return redirect(url_for('index'))
    


                        
# start() 
if __name__=="__main__":
        app.run(host='0.0.0.0', port=5000,debug=True)
        

#flask run --host=0.0.0.0
