function presionarBoton(accionADesencadenar) {
  console.log("El boton ha sido presionado");

  if (accionADesencadenar === "function") {
    accionADesencadenar();
  }
  console.log("Fin de la accion al presionar el boton");
}

//Callbacks

function mostrarMensaje() {
  console.log("Se mostro un mensaje");
}

function reproducirSonido() {
  console.log("Sonido se ha reproducido");
}

//Prueba
console.log("--- Primer uso: Botón con mensaje ---");
presionarBoton(mostrarMensaje);

console.log("\n--- Segundo uso: Botón con sonido ---");
presionarBoton(reproducirSonido);
