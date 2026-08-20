const tasks = [
    "Learn Azure",
    "Build 3-tier architecture",
    "Deploy application"
];

function renderTasks() {
    const list = document.getElementById("taskList");

    list.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.textContent = task;
        list.appendChild(li);
    });
}

function addTask() {
    const input = document.getElementById("taskInput");

    if (input.value.trim() === "") {
        return;
    }

    tasks.push(input.value);

    input.value = "";

    renderTasks();
}

renderTasks();
