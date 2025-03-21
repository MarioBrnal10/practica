from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash
from db import mysql

# Inicialización de la aplicación
app = Flask(__name__)
app.secret_key = "mysecretkey"

# Creación del Blueprint
contacts = Blueprint('contacts', __name__, template_folder='app/templates')


@contacts.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts=data)


@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)",
                (name, phone, email)
            )
            mysql.connection.commit()
            flash('Contact added successfully')
        except Exception as e:
            flash(f"Error: {str(e)}")
        finally:
            cur.close()
        return redirect(url_for('contacts.Index'))


@contacts.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id,))
    data = cur.fetchall()
    cur.close()
    if data:
        return render_template('edit-contact.html', contact=data[0])
    else:
        flash("Contact not found")
        return redirect(url_for('contacts.Index'))


@contacts.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET name = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (name, email, phone, id))
        mysql.connection.commit()
        cur.close()
        flash('Contact Updated Successfully')
        return redirect(url_for('contacts.Index'))


@contacts.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = %s', (id,))
    mysql.connection.commit()
    cur.close()
    flash('Contact Removed Successfully')
    return redirect(url_for('contacts.Index'))


# Registro del Blueprint
app.register_blueprint(contacts)

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
