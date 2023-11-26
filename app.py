from flask import Flask,render_template,request,redirect,url_for, g
from init import create_app
from init import get_db

app=create_app()
#home
@app.route('/')
def index():
    return render_template('index.html')
#menu
@app.route('/menu')
def menu():
   return render_template('menu.html')

#order
@app.route('/order',methods=['GET','POST'])
def order():
 if request.method=='POST':
    db=get_db()
    name=request.form.get('f2')
    result = db.execute('SELECT Name,Price,dish_image FROM dishes WHERE Name=?',(name,)).fetchone()
    if result:
       value1,value2,value3= result
    else:
        print("No matching records found.")
    return render_template('order.html',var1=value1,var2=value2,var3=value3)

# customer order data
@app.route('/order/details',methods=['GET','POST'])
def details():
   
   if request.method == 'POST':
       name=request.form.get('name')
       mobile_num=request.form.get('number')
       address=request.form.get('Address')
       
       dish_name=request.form.get('dish')
       price =request.form.get('price')
       
       db=get_db()
      
       db.execute("INSERT INTO orders VALUES (?, ?, ?,?,?)", (name,mobile_num,address,dish_name,price))
       db.commit() 
   return render_template('order_success.html')

#admin login
@app.route('/login',methods=['GET','POST'])
def login():
   
   if request.method == 'POST':
       
       username=request.form.get('name')
       password=request.form.get('pwd')
      
       db=get_db()
       
       result = db.execute('SELECT username,password FROM login WHERE username=? and password=?',(username,password)).fetchone()

       if result:
            return render_template('admin_home.html')
       else:
            value='Incorrect credentials'
            return render_template('login.html',flag=value)
   return render_template('login.html')

#order mdetails
@app.route('/order_details',methods=['GET','POST'])
def order_details():
  
   if request.method == 'POST':
    
       db=get_db()
       result = db.execute('SELECT *  from orders')
       if result:
            return render_template('order_details.html',items=result.fetchall())
       else:
            print("No records.")
            
   return render_template('order_details.html')

#review
@app.route('/review',methods=['GET','POST'])
def review():
   
   if request.method == 'POST':
       
       db=get_db()
       result = db.execute('SELECT *  from contact')
       if result:
            return render_template('review.html',items=result.fetchall())
       else:
            print("No records.")
            
   return render_template('review.html')

#customer review
@app.route('/cust_review',methods=['GET','POST'])
def cust_review():
   
   if request.method == 'POST':
       
       name=request.form.get('name')
       email=request.form.get('email')
       message=request.form.get('message') 
       
       db=get_db()
       db.execute("INSERT INTO contact VALUES (?, ?, ?)", (name,email,message))
       
       db.commit() 
   return render_template('cust_review.html')


@app.route('/cont')
def cont():
   return render_template('cont.html')

if __name__=='__main__':
    app.run(
       host="0.0.0.0",
       port=8080
    )





