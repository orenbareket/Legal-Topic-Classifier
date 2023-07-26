function predictTopic() {
    const inputText = document.getElementById("inputText").value;
    const data = { "text": inputText };
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json; charset=utf-8' },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(result => {
        console.log("Prediction result:", result); // Debugging statement

        if (result.topic === "No legal topic found.") {
            document.getElementById("outputTopic").innerText = "No legal topic found.";
        } else {
            document.getElementById("outputTopic").innerText = "Predicted Legal Topic: " + result.topic;
        }
    })
    .catch(error => {
        console.error("Error predicting topic:", error);
    });
}