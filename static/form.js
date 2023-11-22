window.onload = miFuncion;

function miFuncion() {
    inputs.forEach(input => {
            if (input.value.trim() !== '') {
                input.classList.add("is-valid");
            } else {
                input.classList.remove("is-valid");
            } 
        
    });
}


    
    const inputs = document.querySelectorAll("input");


    
    
    inputs.forEach(input => {
        input.addEventListener("blur", (event) => {
            if (event.target.value.trim() !== '') {
                input.classList.add("is-valid");
            } else {
                input.classList.remove("is-valid");
            } 
        });
    });









