from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
import requests

from data.salons import salons
from data.services import services


app = Flask(__name__)
app.secret_key = "salon-belleza-clave-secreta"

API_URL = "http://127.0.0.1:8001"


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html",
        salons=salons,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        password = request.form.get("password", "")

        try:
            response = requests.post(
                f"{API_URL}/auth/login",
                json={
                    "correo": correo,
                    "password": password,
                },
                timeout=5,
            )

            if response.status_code == 200:
                resultado = response.json()
                usuario = resultado["usuario"]

                session["usuario_id"] = usuario["id"]
                session["usuario_nombre"] = usuario["nombre"]
                session["usuario_correo"] = usuario["correo"]

                flash("Inicio de sesión exitoso.", "success")
                return redirect(url_for("home"))

            flash(
                "Correo o contraseña incorrectos.",
                "danger",
            )

        except requests.RequestException:
            flash(
                "No se pudo conectar con el servidor.",
                "danger",
            )

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()

    flash(
        "Sesión cerrada correctamente.",
        "success",
    )

    return redirect(url_for("login"))


# =====================================================
# DETALLE DEL SALÓN
# =====================================================

@app.route("/salon/<int:id>")
def salon_detail(id):
    salon = next(
        (
            salon_item
            for salon_item in salons
            if salon_item["id"] == id
        ),
        None,
    )

    if salon is None:
        return "Salón no encontrado", 404

    salon_services = services.get(id, [])

    return render_template(
        "salon_detail.html",
        salon=salon,
        services=salon_services,
    )


# =====================================================
# SELECCIONAR FECHA Y HORA
# =====================================================

@app.route("/booking/<int:id>")
def booking(id):
    salon = next(
        (
            salon_item
            for salon_item in salons
            if salon_item["id"] == id
        ),
        None,
    )

    if salon is None:
        return "Salón no encontrado", 404

    return render_template(
        "booking.html",
        salon=salon,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
