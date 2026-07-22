/*=====================================================
=            VARIABLES
=====================================================*/

const buttons=document.querySelectorAll(".add-service");
const reservation=document.getElementById("reservationList");
const totalPrice=document.getElementById("totalPrice");
const totalTime=document.getElementById("totalTime");
const serviceCount=document.getElementById("serviceCount");
let services=[];

/*=====================================================
=            RENDER RESERVA
=====================================================*/

function renderReservation(){
    if(services.length===0){
        reservation.innerHTML=`
            <div class="empty-reservation">

                <i class="bi bi-calendar-check"></i>

                <p>No has agregado servicios.</p>

            </div>
        `;

        totalPrice.innerHTML="$0";
        totalTime.innerHTML="0 min";
        serviceCount.innerHTML="0";
        return;
    }

    reservation.innerHTML="";

    let total=0;

    let minutes=0;

    services.forEach((service,index)=>{

        total+=service.price;
        minutes+=service.minutes;
        reservation.innerHTML+=`

            <div class="reservation-item">
                <div>
                    <strong>${service.name}</strong>
                    <br>
                    <small>${service.time}</small>
                </div>

                <div>
                    <span>$${service.price}</span>
                    <button
                    class="delete-service"
                    onclick="removeService(${index})">
                    <i class="bi bi-trash"></i>
                    </button>
                </div>

            </div>
        `;
    });

    totalPrice.innerHTML=`$${total}`;
    totalTime.innerHTML=`${minutes} min`;
    serviceCount.innerHTML=services.length;

}

/*=====================================================
=            AGREGAR SERVICIO
=====================================================*/

buttons.forEach(button=>{
    button.addEventListener("click",()=>{
        const exists=services.find(item=>item.name===button.dataset.name);
        if(exists){
            return;
        }

        let minutes=parseInt(button.dataset.time);

        if(isNaN(minutes)){
            minutes=60;
        }

        services.push({
            name:button.dataset.name,
            price:parseFloat(button.dataset.price),
            time:button.dataset.time,
            minutes:minutes
        });

        renderReservation();

    });
});

/*=====================================================
=            ELIMINAR SERVICIO
=====================================================*/

function removeService(index){
    services.splice(index,1);
    renderReservation();

}