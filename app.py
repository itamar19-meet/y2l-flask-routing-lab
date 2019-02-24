from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/item')
def item_page():
    return render_template("item.html")

    
@app.route('/shop' , methods=['GET','POST'])
def shop_page():
    if(request.method == 'GET'):
        return render_template("item.html" , request.form["item"])
        
    else:
        return render_template("shop.html" , items("lamp","table","chair","computer")

# @app.route('/item')
# def 
# @app.route('/item')
# def item_page():
#     return render_template("item.html")

if __name__ == '__main__':
   app.run(debug = True)
