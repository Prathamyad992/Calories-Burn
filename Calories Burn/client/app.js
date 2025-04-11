document.getElementById("calorieForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    // Get form input values
    const gender = document.getElementById("gender").value;
    const age = document.getElementById("age").value;
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;
    const duration = document.getElementById("duration").value;
    const heartRate = document.getElementById("heart_rate").value;
    const bodyTemp = document.getElementById("body_temp").value;

    // Create FormData object to send to the backend
    const formData = new FormData();
    formData.append("gender", gender);
    formData.append("age", age);
    formData.append("height", height);
    formData.append("weight", weight);
    formData.append("duration", duration);
    formData.append("heart_rate", heartRate);
    formData.append("body_temp", bodyTemp);

    try {
        const response = await fetch("http://127.0.0.1:5000/predict_calorie", {
            method: "POST",
            body: formData,
        });
        const result = await response.json();

        document.getElementById("result").textContent = `Estimated Calorie Burn: ${result.estimated_calorie.toFixed(2)} kcal`;
    } catch (error) {

        document.getElementById("result").textContent = "Error occurred while predicting calories.";
        console.error("Error:", error);
    }
});
