#=====================================================
# SERVICIOS BASE
#=====================================================

hair_services=[
    {"name":"Lavado","price":10,"time":"30 min"},
    {"name":"Blower","price":15,"time":"45 min"},
    {"name":"Plancha","price":12,"time":"30 min"},
    {"name":"Corte","price":18,"time":"45 min"},
    {"name":"Tintura","price":40,"time":"120 min"}
]

nail_services=[
    {"name":"Manicure","price":15,"time":"40 min"},
    {"name":"Pedicure","price":18,"time":"50 min"},
    {"name":"Gel","price":20,"time":"60 min"},
    {"name":"Acrílicas","price":35,"time":"90 min"}
]

spa_services=[
    {"name":"Masaje Relajante","price":35,"time":"60 min"},
    {"name":"Limpieza Facial","price":28,"time":"50 min"},
    {"name":"Exfoliación","price":22,"time":"45 min"}
]

barber_services=[
    {"name":"Corte Clásico","price":12,"time":"30 min"},
    {"name":"Barba","price":8,"time":"20 min"},
    {"name":"Corte + Barba","price":18,"time":"50 min"}
]

#=====================================================
# SERVICIOS POR SALÓN
#=====================================================

services={

1:{
    "Cabello":hair_services,
    "Uñas":nail_services
},

2:{
    "Cabello":hair_services
},

3:{
    "Uñas":nail_services
},

4:{
    "Cabello":hair_services,
    "Spa":spa_services
},

5:{
    "Cabello":hair_services
},

6:{
    "Uñas":nail_services
},

7:{
    "Cabello":hair_services,
    "Uñas":nail_services
},

8:{
    "Spa":spa_services
},

9:{
    "Cabello":hair_services
},

10:{
    "Cabello":hair_services
},

11:{
    "Uñas":nail_services
},

12:{
    "Cabello":hair_services,
    "Spa":spa_services
},

13:{
    "Cabello":hair_services
},

14:{
    "Spa":spa_services
},

15:{
    "Cabello":hair_services,
    "Uñas":nail_services
},

16:{
    "Cabello":hair_services,
    "Barbería":barber_services
}

}