document.addEventListener("DOMContentLoaded", () => {
  const usuarioActivo = JSON.parse(localStorage.getItem("usuarioActivo"));

  if (usuarioActivo) {
    if (
      window.location.pathname.includes("login.html") ||
      window.location.pathname.includes("signup.html") ||
      window.location.pathname.includes("index.html")
    ) {
      window.location.href = "todo.html";
    }
  }
});
