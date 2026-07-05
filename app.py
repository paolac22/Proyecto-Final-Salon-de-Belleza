from flask import Flask, render_template
from data.salons import salons
from data.services import services

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home.html",
        salons=salons
    )

@app.route("/login")
def login():
    return render_template("login.html")

#=====================================================
# DETALLE DEL SALÓN
#=====================================================
@app.route("/salon/<int:id>")
def salon_detail(id):
    salon = next(
        (
            s
            for s in salons
            if s["id"]==id
        ),
        None
    )
    
    salon_services = services.get(id)

    return render_template(
        "salon_detail.html",
        salon=salon,
        services=salon_services
    )

#=====================================================
# SELECCIONAR FECHA Y HORA
#=====================================================

@app.route("/booking/<int:id>")
def booking(id):

    salon = next(
        (
            s for s in salons
            if s["id"] == id
        ),
        None
    )

    return render_template(
        "booking.html",
        salon=salon
    )

if __name__ == "__main__":
    app.run(debug=True)