document.getElementById("caloriesForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from refreshing the page
  
    // Collect input values
    const age = parseInt(document.getElementById("age").value);
    const gender = document.getElementById("gender").value;
    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value);
    const activityLevel = parseFloat(document.getElementById("activityLevel").value);
  
    // Mock calories prediction logic
    const baseCalories = (gender === "male") 
      ? 10 * weight + 6.25 * height - 5 * age + 5
      : 10 * weight + 6.25 * height - 5 * age - 161;
  
    const predictedCalories = Math.round(baseCalories * activityLevel);
  
    // Display result
    document.getElementById("result").innerText = `Predicted Calories Burned: ${predictedCalories} kcal/day`;
  });  
