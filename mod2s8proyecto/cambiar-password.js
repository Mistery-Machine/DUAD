const API_URL = "https://api.restful-api.dev/objects"; 

document.getElementById("passwordForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("userId").value;
  const oldPassword = document.getElementById("oldPassword").value;
  const newPassword = document.getElementById("newPassword").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  try {
    const res = await fetch(`${API_URL}/${id}`);
    if (!res.ok) throw new Error("Usuario no encontrado");

    const data = await res.json();

    if (data.data?.password !== oldPassword) {
      alert("La contraseña anterior es incorrecta");
      return;
    }

    if (newPassword !== confirmPassword) {
      alert("Las contraseñas nuevas no coinciden");
      return;
    }

    const updateRes = await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: data.name,
        data: { ...data.data, password: newPassword }
      })
    });

    if (!updateRes.ok) throw new Error("Error al actualizar contraseña");

    alert("Contraseña actualizada correctamente");

  } catch (error) {
    alert("Error: " + error.message);
    console.error(error);
  }
});