from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: Cálculo de compras
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_tarro = 9000

        # Cálculo del total y descuentos
        total_sin_descuento = cantidad * precio_tarro
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        # Crear el mensaje
        mensaje = (
            f"Nombre del cliente: {nombre}<br>"
            f"Total sin descuento: ${total_sin_descuento:.2f}<br>"
            f"El descuento es: ${descuento_aplicado:.2f}<br>"
            f"El total a pagar es de: ${total_con_descuento:.2f}"
        )

    return render_template('ejercicio1.html', mensaje=mensaje)

# Ejercicio 2: Login de usuarios
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # Usuarios predefinidos
    usuarios = {
        "juan": "admin",  # Usuario administrador
        "pepe": "user"    # Usuario regular
    }

    mensaje = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Validar credenciales
        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)


