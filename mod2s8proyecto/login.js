const API_URL = "https://api.restful-api.dev/objects"; 

if (localStorage.getItem("usuario")) {
  window.location.href = "perfil.html";
}

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("userId").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${API_URL}/${id}`);
    if (!res.ok) throw new Error("Usuario no encontrado");

    const data = await res.json();

    if (data.data?.password !== password) {
      alert("Contraseña incorrecta");
      return;
    }

    localStorage.setItem("usuario", JSON.stringify(data));
    window.location.href = "perfil.html";

  } catch (error) {
    alert("El usuario no existe");
    console.error(error);
  }
});