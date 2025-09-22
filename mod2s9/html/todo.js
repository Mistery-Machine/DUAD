document.addEventListener("DOMContentLoaded", function () {
  const usuarioActivo = JSON.parse(localStorage.getItem("usuarioActivo"));
  if (!usuarioActivo) {
    alert("Debes iniciar sesión para acceder");
    window.location.href = "login.html";
    return;
  }

  document.querySelector(".username").textContent = usuarioActivo.username;

  let tareas = [];
  let filtroActual = "todas";

  const showFormBtn = document.getElementById("showFormBtn");
  const formContainer = document.getElementById("formContainer");
  const taskForm = document.getElementById("taskForm");
  const taskInput = document.getElementById("taskInput");
  const taskList = document.getElementById("taskList");
  const cancelBtn = document.getElementById("cancelBtn");

  const filtroTodas = document.getElementById("filtroTodas");
  const filtroCompletas = document.getElementById("filtroCompletas");
  const filtroIncompletas = document.getElementById("filtroIncompletas");
  const logoutBtn = document.querySelector(".logout-btn");

  logoutBtn.addEventListener("click", () => {
    localStorage.removeItem("usuarioActivo");
    window.location.href = "login.html";
  });

  showFormBtn.addEventListener("click", () => {
    formContainer.classList.toggle("hidden");
    taskInput.focus();
  });

  cancelBtn.addEventListener("click", () => {
    formContainer.classList.add("hidden");
    taskInput.value = "";
  });

  const API_URL = "https://api.restful-api.dev/objects";

  async function cargarTareas() {
    try {
      const resp = await axios.get(`${API_URL}?id=${usuarioActivo.id}`);
      if (resp.data && resp.data[0] && resp.data[0].data) {
        tareas = resp.data[0].data.tareas || [];
      } else {
        tareas = [];
      }
      renderTareas();
    } catch (err) {
      console.error("Error cargando tareas:", err);
    }
  }

  async function guardarTareas() {
    try {
      const body = {
        name: `tareas_${usuarioActivo.username}`,
        data: { tareas },
      };

      if (!usuarioActivo.objId) {
        const resp = await axios.post(API_URL, body);
        usuarioActivo.objId = resp.data.id;
        localStorage.setItem("usuarioActivo", JSON.stringify(usuarioActivo));
      } else {
        await axios.put(`${API_URL}/${usuarioActivo.objId}`, body);
      }
    } catch (err) {
      console.error("Error guardando tareas:", err);
    }
  }

  taskForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const texto = taskInput.value.trim();
    if (texto === "") return;

    const nuevaTarea = {
      id: Date.now(),
      texto,
      completada: false,
    };

    tareas.push(nuevaTarea);
    guardarTareas();
    taskInput.value = "";
    formContainer.classList.add("hidden");
    renderTareas();
  });

  function renderTareas() {
    taskList.innerHTML = "";

    let tareasFiltradas = tareas;
    if (filtroActual === "completas") {
      tareasFiltradas = tareas.filter((t) => t.completada);
    } else if (filtroActual === "incompletas") {
      tareasFiltradas = tareas.filter((t) => !t.completada);
    }

    tareasFiltradas.forEach((tarea) => {
      const li = document.createElement("li");
      if (tarea.completada) li.classList.add("completed");

      const texto = document.createTextNode(tarea.texto);
      li.appendChild(texto);

      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.checked = tarea.completada;
      checkbox.addEventListener("change", () => {
        tarea.completada = checkbox.checked;
        guardarTareas();
        renderTareas();
      });

      const deletebtn = document.createElement("button");
      deletebtn.textContent = "╳";
      deletebtn.addEventListener("click", () => {
        tareas = tareas.filter((t) => t.id !== tarea.id);
        guardarTareas();
        renderTareas();
      });

      li.prepend(checkbox);
      li.appendChild(deletebtn);
      taskList.appendChild(li);
    });
  }

  filtroTodas.addEventListener("click", () => {
    filtroActual = "todas";
    renderTareas();
  });

  filtroCompletas.addEventListener("click", () => {
    filtroActual = "completas";
    renderTareas();
  });

  filtroIncompletas.addEventListener("click", () => {
    filtroActual = "incompletas";
    renderTareas();
  });

  cargarTareas();
});
