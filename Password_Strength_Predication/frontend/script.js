// ==============================
// Elements
// ==============================

const passwordInput = document.getElementById("password");
const toggleBtn = document.getElementById("toggleBtn");

const progressBar = document.getElementById("progressBar");

const strengthText = document.getElementById("strengthText");
const emoji = document.getElementById("emoji");

const suggestions = document.getElementById("suggestions");

const lengthItem = document.getElementById("length");
const upperItem = document.getElementById("upper");
const lowerItem = document.getElementById("lower");
const numberItem = document.getElementById("number");
const specialItem = document.getElementById("special");


toggleBtn.addEventListener("click", () => {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";
        toggleBtn.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';

    } else {

        passwordInput.type = "password";
        toggleBtn.innerHTML = '<i class="fa-solid fa-eye"></i>';

    }

});


// ==============================
// Live Prediction
// ==============================

passwordInput.addEventListener("keyup", () => {

    const password = passwordInput.value;

    checkRequirements(password);

    if (password.length === 0) {

        resetUI();
        return;

    }

    predictPassword(password);

});


// ==============================
// Call FastAPI
// ==============================

async function predictPassword(password) {

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                password: password
            })

        });

        const data = await response.json();

        updateStrength(data);

    }

    catch (error) {

        console.log(error);

        strengthText.innerHTML = "Server Error";

        emoji.innerHTML = "⚠️";

    }

}


// ==============================
// Update Strength
// ==============================

function updateStrength(data) {

    strengthText.innerHTML = data.strength;

    emoji.innerHTML = data.emoji;

    progressBar.style.width = data.score + "%";

    progressBar.style.background = getColor(data.score);

    strengthText.className = "";

    if (data.score <= 35)
        strengthText.classList.add("weak");

    else if (data.score <= 70)
        strengthText.classList.add("medium");

    else
        strengthText.classList.add("strong");


    updateSuggestions(data.score);

}


// ==============================
// Password Checklist
// ==============================

function checkRequirements(password) {

    updateItem(lengthItem, password.length >= 12, "At least 12 characters");

    updateItem(upperItem, /[A-Z]/.test(password), "Uppercase letter");

    updateItem(lowerItem, /[a-z]/.test(password), "Lowercase letter");

    updateItem(numberItem, /\d/.test(password), "Number");

    updateItem(specialItem, /[^A-Za-z0-9]/.test(password), "Special character");

}

function updateItem(element, valid, text) {

    if (valid) {

        element.innerHTML = "✅ " + text;

        element.classList.remove("invalid");

        element.classList.add("valid");

    }

    else {

        element.innerHTML = "❌ " + text;

        element.classList.remove("valid");

        element.classList.add("invalid");

    }

}


// ==============================
// Suggestions
// ==============================

function updateSuggestions(score) {

    if (score <= 35) {

        suggestions.innerHTML = `
        • Use at least 12 characters.<br>
        • Add uppercase letters.<br>
        • Include numbers.<br>
        • Include special symbols like @ # $ %.
        `;

    }

    else if (score <= 70) {

        suggestions.innerHTML = `
        • Password is decent.<br>
        • Increase its length.<br>
        • Mix more symbols and numbers.<br>
        • Avoid common words.
        `;

    }

    else {

        suggestions.innerHTML = `
        🎉 Excellent password!<br>
        Keep using unique passwords for every account.
        `;

    }

}


// ==============================
// Progress Bar Colour
// ==============================

function getColor(score) {

    if (score <= 35)
        return "#ef4444";

    if (score <= 70)
        return "#f59e0b";

    return "#22c55e";

}


// ==============================
// Reset UI
// ==============================

function resetUI() {

    progressBar.style.width = "0%";

    strengthText.innerHTML = "Waiting...";

    strengthText.className = "";

    emoji.innerHTML = "⚪";

    suggestions.innerHTML = "Start typing your password...";

    checkRequirements("");

}