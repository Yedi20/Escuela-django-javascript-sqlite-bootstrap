   (function () {
   
   const  btnEliminacion = document.querySelectorAll(".btnEliminacion");
        btnEliminacion.forEach(btn => {
            btn.addEventListener('click', (e) =>{
                const confirmacion = confirm('Enserio, ¿Lo vas borrar?');
                if (!confirmacion) {
                    e.preventDefault();
                    
                }
            });
            
        });
})();