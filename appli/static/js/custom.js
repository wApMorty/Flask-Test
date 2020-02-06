var input = document.getElementById("passwordInput");
    
//Event listener pour cliquer sur le bouton quand on tape Enter
input.addEventListener("keyup", function(event){
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("connectBtn").click();
    }
})

// Fonction appelee au click sur le bouton Connect
function connect(){
    var password = document.getElementById("passwordInput");
    console.log("Mot de passe recu : " + password.value)
    if (password.value == "fromage") {
        console.log("Mot de passe accepté, passage a la page suivante")
        window.location = "menu&authorized=true";
    } else {
        console.log("Mot de passe refusé, refresh de la page")
        window.location="/";
    }
}

function analyse(){
    window.location = "../result"
}