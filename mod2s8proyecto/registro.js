const API_URL = "https://api.restful-api.dev/objects"; 

if (localStorage.getItem("usuario")) {
  window.location.href = "perfil.html";
}

document.getElementById("registroForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const nombre = document.getElementById("nombre").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: nombre,
        data: { email, password }
      })
    });

    if (!res.ok) throw new Error("Error al crear usuario");

const data = await res.json();


alert(`Usuario creado correctamente! Tu id es ${data.id}`);

const usuario = {
  id: data.id,
  nombre: data.name,
  email: data.data.email,
  password: data.data.password
};

localStorage.setItem("usuario", JSON.stringify(usuario));

window.location.href = "perfil.html";

  } catch (error) {
    alert("Hubo un error en el registro");
    console.error(error);
  }
});