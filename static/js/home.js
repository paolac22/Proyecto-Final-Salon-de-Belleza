/*=========================================
BUSCADOR
=========================================*/

const searchInput = document.querySelector("#searchInput");

if(searchInput){
    searchInput.addEventListener("keyup",function(){
        const value=this.value.toLowerCase();
        document.querySelectorAll(".salon-item").forEach(card=>{
            const title=card.querySelector("h5").innerText.toLowerCase();
            card.style.display=title.includes(value) ? "" : "none";
        });
    });

}