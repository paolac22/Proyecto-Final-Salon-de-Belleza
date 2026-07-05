/*=====================================================
=            SELECCIÓN DE DÍA
=====================================================*/
const days=document.querySelectorAll(".day-btn");

days.forEach(day=>{
    day.addEventListener("click",()=>{
        days.forEach(btn=>btn.classList.remove("active"));
        day.classList.add("active");
    });
});