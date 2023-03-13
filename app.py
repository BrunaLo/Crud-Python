import mysql.connector
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '130810'
app.config['MYSQL_DB'] = 'crud_python'

mysql = MySQL(app)


# GET
@app.route("/")
def data():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM crud_python.vendas_crm''')
    rv = cursor.fetchall()
    cursor.close()
    return str(rv)


# POST
@app.route("/", methods=['POST'])
def insert_data():

    cursor = mysql.connection.cursor()

    produto = request.json['nome_produto']
    cliente = request.json['nome_cliente']
    email = request.json['email_cliente']
    valor = request.json['valor_produto']

    cursor.execute(
        f'''INSERT INTO crud_python.vendas_crm (nome_produto, nome_cliente, email_cliente, valor_produto) VALUES ('{produto}', '{cliente}', '{email}', {valor})''')
    mysql.connection.commit()
    cursor.close()
    return "Produto adicionado com sucesso!!"


# PUT
@app.route("/update/<string:table>", methods=['PUT'])
def update_data(table):

    cursor = mysql.connection.cursor()

    cursor.execute(
        "UPDATE crud_python.vendas_crm SET valor_produto = '300' WHERE idvendas_CRM = 15")
    mysql.connection.commit()
    cursor.close()
    return "Produto alterado com sucesso!!"


# DELETE
@app.route("/delete/<string:table>", methods=['DELETE'])
def delete_data(table):

    cursor = mysql.connection.cursor()

    id = request.json['idvendas_CRM']

    cursor.execute(
        f"DELETE FROM crud_python.vendas_crm WHERE idvendas_CRM = {id}")
    mysql.connection.commit()
    cursor.close()
    return "Produto deletado com sucesso!!"


if __name__ == "__main__":
    app.run(debug=True)


conexao.close()
