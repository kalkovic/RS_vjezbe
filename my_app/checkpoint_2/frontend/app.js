fetch("http://localhost:8001/news")
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("news-list");
        data.forEach(n => {
            const li = document.createElement("li");
            li.textContent = `${n.title} (${n.category})`;
            list.appendChild(li);
        });
    })
    .catch(err => console.error(err));
