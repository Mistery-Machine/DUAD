const loginForm = document.getElementById("login");

loginForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];

  const user = usuarios.find(
    (u) =>
      (u.username === username || u.email === username) &&
      u.password === password
  );

  if (user) {
    alert("Login exitoso");
    localStorage.setItem("usuarioActivo", JSON.stringify(user));
    window.location.href = "todo.html";
  } else {
    alert("Usuario o contraseña incorrectos");
  }
});
