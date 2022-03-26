from flask import Flask,render_template,request
import joblib

#Creating an object
app=Flask(__name__)#Doubt:Ask about what exactly is happening here - Need to understand the OOPS concept.
#There is an app named 'app' being created here.

#Business Logic Code
##The below code says if someone vists the '/' of the URL, execute the function.
@app.route('/')# This line is the fuction call for the below function
def base():
    return render_template('home.html')

@app.route('/galary')
def gal():
    return render_template('galary.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contact')
def contact():
    return 'Welcome to Contact Page'

@app.route('/hiring')
def hiring():
    return 'Welcome to Hiring Page'

@app.route('/employee/')
def portal():
    return 'Welcome to Emp Portal'

@app.route('/predict',methods=['post'])
def predict():
    exp=request.form.get('Experience')
    phone=request.form.get('Phone_Number')
    mail=request.form.get('Email')
    
    print(exp)
    print(phone)
    print(mail)
#This method tells us that, when the URl reaches this route:
## 1. methods=['post'] : A HTTP post method must be executed.
## 2. exp=request.form.get('Experience') / backend_variable=request.form.get('frontend_variable') : This makes sure that, when the form is submitted, the data of the frontend variable is stored in the backend variable.  

@app.route('/diabetes_check')
def d_check():
    return render_template('diabetes_check.html')

@app.route('/diabetes_prediction',methods=['post'])
def d_pred():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)

    model_db=joblib.load('diabetic_80.pkl')
    pred_db=model_db.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if(pred_db[0]==0):
        return 'Person is not diabetic'
    else:
        return 'Person is diabetic'

   


if __name__=='__main__':
    # The above code means that, if the 'app.py' file is run directly, only then the code within it will run. Otherwise, it will not.(Explore this more)
    #Understand the above line(Will require a knowledge of OOPS concept)
    app.run(debug=True)#Ask about what exactly is happening in this line - Need to understand the OOPS concept.
##The app called 'app' is being run.
##By setting the 'debug' parameter to 'True' we do not need to run the code again everytime we make a change in the Business Logic Code, for the changes to be reflected in the browser. The changes are automatically updated on the browser.
## There is a limitation to this parameter. Only changes made to existing functions and routes are tracked. Adding a new route and function will not be tracked. If a new route and function is added, the entire code will have to run again.
#The above code is the backend code.
#The above code(except the Business Logic Code) creates a basic website in the local host. The link to this website is returned when the code is executed.
