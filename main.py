from flask import Flask, render_template, request, redirect, url_for, flash
from DB_Operations import fetch_all_items, insert_item, fetch_item_by_id, update_item, delete_item

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home-page')
def homepage():
    list = fetch_all_items()
    return render_template('home-page.html', list=list)

@app.route('/add_item', methods=["POST","GET"])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        harga = request. form['harga']
        qty = request. form['qty']
        #insert item to db
        insert_item(name, harga, qty)
        flash('Item Added Successfully!')
        return redirect(url_for('homepage'))
    return render_template('add.html')


@app.route('/edit/<id>', methods=["GET","POST"])
def edit_item(id):
    list = fetch_item_by_id(id)
    if request.method == 'POST':
        name = request.form['name' ]
        harga = request.form['harga' ]
        qty = request.form['qty' ]
        #update item
        update_item(id,name, harga, qty)
        flash('Item Updated Successfully!')
        return redirect(url_for('homepage'))
    return render_template('edit.html', list=list)

@app.route('/delete/<id>', methods=["GET","POST"])
def delete_item_route(id):
    delete_item(id)
    flash('Item Deleted Successfully!')
    return redirect(url_for('homepage'))

if __name__== '__main__':
    app.run(debug=True)