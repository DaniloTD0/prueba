from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__, template_folder='template')

# Rutas de la aplicación

@app.route('/')
def home():
    return render_template('index.html')


# articulos


@app.route('/archivo')
def archivos():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM articulo")
    myresult = cursor.fetchall()

    # Convertir datos a diccionarios
    insertObject = []
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    return render_template('archivo.html', data=insertObject)

@app.route('/add', methods=['POST'])
def addArt():
   
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']

        if nombre and precio and stock:
            cursor = db.database.cursor()
            sql = "INSERT INTO articulo (nombre, precio, stock) VALUES (%s, %s, %s)"
            data = (nombre, precio, stock)
            cursor.execute(sql, data)
            db.database.commit()
            cursor.close()
        return redirect(url_for('archivo'))

@app.route('/delete/<string:articulo_id>')
def delete(articulo_id):
    cursor = db.database.cursor()
    sql = "DELETE FROM articulo WHERE articulo_id=%s"
    data = (articulo_id,)
    cursor.execute(sql, data)
    db.database.commit()
    cursor.close()
    return redirect(url_for('archivo'))

@app.route('/edit/<string:articulo_id>', methods=['POST'])
def edit(articulo_id):
    # Verificar que todos los campos están presentes en el formulario
    required_fields = ['nombre', 'precio', 'stock']
    for field in required_fields:
        if field not in request.form:
            return f"Missing form field: {field}", 400

    # Si todos los campos están presentes, proceder con la actualización
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']

    if nombre and precio and stock:
        cursor = db.database.cursor()
        sql = "UPDATE articulo SET nombre = %s, precio= %s, stock = %s WHERE articulo_id = %s"
        data = (nombre, precio, stock, articulo_id)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
    return redirect(url_for('archivo'))

# clientes

@app.route('/clientes')
def clientes():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM cliente")
    myresult = cursor.fetchall()

    # Convertir datos a diccionarios
    insertObject = []
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    return render_template('clientes.html', data=insertObject)

@app.route('/addCli', methods=['POST'])
def addCli():
        nombres = request.form['nombres']
        telefono = request.form['telefono']
      

        if nombres and telefono: 
            cursor = db.database.cursor()
            sql = "INSERT INTO cliente (nombres, telefono) VALUES (%s, %s)"
            data = (nombres, telefono)
            cursor.execute(sql, data)
            db.database.commit()
            cursor.close()
        return redirect(url_for('clientes'))

@app.route('/deleteCli/<string:cliente_id>')
def deleteCli(cliente_id):
    cursor = db.database.cursor()
    sql = "DELETE FROM cliente WHERE cliente_id=%s"
    data = (cliente_id,)
    cursor.execute(sql,data)
    db.database.commit()
    cursor.close()
    return redirect(url_for('clientes'))

@app.route('/editCli/<string:cliente_id>', methods=['POST'])
def editCli(cliente_id):
    required_fields = ['nombres', 'telefono']
    for field in required_fields:
        if field not in request.form:
            return f"Missing form field: {field}", 400

    nombres = request.form['nombres']
    telefono = request.form['telefono']
      
    if nombres and telefono:
        cursor = db.database.cursor()
        sql = "UPDATE cliente SET nombres = %s, telefono= %s WHERE cliente_id = %s"
        data = (nombres, telefono, cliente_id)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
    return redirect(url_for('clientes'))

#pedidos

@app.route('/pedidos')
def pedidos():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM pedido")
    myresult = cursor.fetchall()

    # Convertir datos a diccionarios
    insertObject = []
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    return render_template('pedidos.html', data=insertObject)



@app.route('/addPed', methods=['POST'])
def addPed():
   
        articulo_id = request.form['articulo_id']
        cliente_id = request.form['cliente_id']
        unidades = request.form['unidades']
        precio_total = request.form['precio_total']
        fecha = request.form['fecha']


        if articulo_id and cliente_id and unidades and precio_total and fecha:
            cursor = db.database.cursor()
            sql = "INSERT INTO pedido (articulo_id, cliente_id, unidades, precio_total, fecha) VALUES (%s, %s, %s, %s, %s)"
            data = (articulo_id, cliente_id, unidades, precio_total, fecha)
            cursor.execute(sql, data)
            db.database.commit()
            cursor.close()
        return redirect(url_for('pedidos'))

@app.route('/deletePed/<string:pedido_id>')
def deletePed(pedido_id):
    cursor = db.database.cursor()
    sql = "DELETE FROM pedido WHERE pedido_id=%s"
    data = (pedido_id,)
    cursor.execute(sql, data)
    db.database.commit()
    cursor.close()
    return redirect(url_for('pedidos'))

@app.route('/editPed/<string:pedido_id>', methods=['POST'])
def editPed(pedido_id):
    print(request.form)
    required_fields = ['cliente_id', 'articulo_id', 'unidades', 'precio_total', 'fecha']
    for field in required_fields:
        if field not in request.form:
            return f"Missing form field: {field}", 400

    cliente_id = request.form['cliente_id']
    articulo_id = request.form['articulo_id']
    unidades = request.form['unidades']
    precio_total = request.form['precio_total']
    fecha = request.form['fecha']

    if cliente_id and articulo_id and unidades and precio_total and fecha:
        cursor = db.database.cursor()
        sql = "UPDATE pedido SET cliente_id = %s, articulo_id = %s, unidades = %s, precio_total = %s, fecha = %s WHERE pedido_id = %s"
        data = (cliente_id, articulo_id, unidades, precio_total, fecha, pedido_id)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
    return redirect(url_for('pedidos'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
