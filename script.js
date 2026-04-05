async function getRoute() {
    let source = document.getElementById("source").value;
    let destination = document.getElementById("destination").value;

    let response = await fetch("http://127.0.0.1:5000/route", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ source, destination })
    });

    let data = await response.json();

    if (data.route) {
        document.getElementById("result").innerText =
            "Safe Route: " + data.route.join(" → ");
    } else {
        document.getElementById("result").innerText =
            "Error: " + data.error;
    }
}
