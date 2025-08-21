const API_URL = "https://api.restful-api.dev/objects"; 
const usuario = JSON.parse(localStorage.getItem("usuario"));

if (!usuario) {
  window.location.href = "login.html";
}

async function cargarPerfil() {
  try {
    const res = await fetch(`${API_URL}/${usuario.id}`);
    const data = await res.json();

    document.getElementById("perfil").innerHTML = `
      <div class="card">
        <h2>${data.name}</h2>
        <p><strong>ID:</strong> ${data.id}</p>
        <p><strong>Email:</strong> ${data.data?.email || "No registrado"}</p>
      </div>
    `;
  } catch (error) {
    console.error("Error cargando perfil:", error);
  }
}

document.getElementById("logout").addEventListener("click", () => {
  localStorage.removeItem("usuario");
  window.location.href = "login.html";
});

cargarPerfil();