// https://docs.djangoproject.com/en/3.2/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


async function getAllTodos(url) {
  try {
    const response = await fetch(url, {
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";

    data.context.forEach(todo => {
      const todoHTMLElement = `
        <li>
          <p>Task: ${todo.task}</p>
          <p>Completed?: ${todo.completed}</p>
        </li>`;
      todoList.innerHTML += todoHTMLElement;
    });
  } catch (error) {
    console.error("Error al obtener TODOs:", error);
    alert("Error al cargar los TODOs");
  }
}



const operationGetAllTodos = async (url) => {
       r = await fetch(url, {
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        }
      })

      dt = await  r.json();

    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";

    (dt.context).forEach(todo => {
      const todoHTMLElement = `
        <li>
          <p>Task: ${todo.task}</p>
          <p>Completed?: ${todo.completed}</p>
        </li>`
        todoList.innerHTML += todoHTMLElement;
    });


};


async function addTodo(url, payload) {
  try {
    const response = await fetch(url, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({payload: payload})
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("TODO creado exitosamente", data);
    return data;
  } catch (error) {
    console.error("Error al agregar TODO", error);
    alert("Error al crear el TODO");
    throw error;
  }
}


async function updateTodo(url, payload) {
  try {
    const response = await fetch(url, {
      method: "PUT",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      body: JSON.stringify({payload: payload})
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("TODO actualizado exitosamente:", data);
    return data;
  } catch (error) {
    console.error("Error al actualizar TODO", error);
    alert("Error al actualizar el TODO");
    throw error;
  }
}


function deleteTodo(url) {
  fetch(url, {
    method: "DELETE",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
}
