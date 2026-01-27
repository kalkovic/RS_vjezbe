const output = document.getElementById("output");
const newsList = document.getElementById("news-list");

let token = null;

// LOGIN
function login() {
  fetch("http://localhost:8000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: "test",
      password: "test"
    })
  })
  .then(res => res.json())
  .then(data => {
    token = data.access_token;
    output.textContent = "Uspješna prijava ✔";
  })
  .catch(err => output.textContent = err);
}

// DOHVAT VIJESTI
function loadNews() {
  fetch("http://localhost:8001/news", {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  })
  .then(res => res.json())
  .then(data => {
    newsList.innerHTML = "";
    data.forEach(n => {
      const li = document.createElement("li");
      li.textContent = `${n.title} (${n.category})`;
      newsList.appendChild(li);
    });
  })
  .catch(err => output.textContent = err);
}
