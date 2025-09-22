const signUpForm = document.getElementById("register");

signUpForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const email = document.getElementById("email").value.trim();
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];

  const existe = usuarios.some(
    (u) => u.username === username || u.email === email
  );
  if (existe) {
    alert("El usuario o email ya están registrados");
    return;
  }

  const nuevoUsuario = {
    id: Date.now(),
    username,
    email,
    password,
  };

  usuarios.push(nuevoUsuario);

  localStorage.setItem("usuarios", JSON.stringify(usuarios));

  alert("Registro exitoso, ahora inicia sesión");
  window.location.href = "login.html";
});
