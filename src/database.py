import mysql.connector

database = mysql.connector.connect(
    host='localHost',
    database='tienda',
    user='crud',
    password='',
    port='3306'
)

# BASE DE DATOS

# CREATE DATABASE IF NOT EXISTS tienda;
# USE tienda;

# CREATE TABLE cliente (
#     cliente_id INT(11) NOT NULL AUTO_INCREMENT,
#     nombres VARCHAR(45) NOT NULL,
#     telefono varchar(10),
#     PRIMARY KEY (cliente_id)
# );

# CREATE TABLE articulo (
#     articulo_id INT(11) NOT NULL AUTO_INCREMENT,
#     nombre VARCHAR(45) NOT NULL,
#     precio INT(11) NOT NULL,
#     stock INT(11) NOT NULL,
#     PRIMARY KEY (articulo_id)
# );

# CREATE TABLE pedido (
#     pedido_id INT(11) NOT NULL AUTO_INCREMENT,
#     articulo_id INT(11) NOT NULL,
#     cliente_id INT(11) NOT NULL,
#     unidades INT(11) NOT NULL,
#     precio_total INT(11) NOT NULL,
#     fecha DATE NOT NULL,
#     PRIMARY KEY (pedido_id),
#     FOREIGN KEY (articulo_id) REFERENCES articulo(articulo_id),
#     FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
# );