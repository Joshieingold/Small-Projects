// Getting inputs
let your_score = 0;
let their_score = 0;
let percent_complete = "";
let new_estimation = "";
let estimate_x = 1.1

// Get Information from HTML
function HTMLGet() {
    your_score = (document.getElementById("your_score_find"));
    their_score = document.getElementById("their_score_find");
    your_score = Number(your_score.value);
    their_score = Number(their_score.value);
}
// Calculate Data
function Calculate() {
    your_score = Number(your_score);
    their_score = Number(their_score);
    percent_complete = "You are " + Math.round(your_score / their_score * 100) + "% Complete";
    new_estimation = "You need to solve " + Math.round((their_score - your_score) / estimate_x) + " more " + (estimate_x).toFixed(1) + " rated problems to achieve your goal.";


}
// Update UI
function UpdateUI() {
    if (their_score === 0 || your_score === 0) {
        return
    }
    else {
        estimation.innerText = new_estimation;
        percent_complete_html.innerText = percent_complete;
    }
}
// Cycle Estimations
function CycleUp() {
    estimate_x += 0.1;
    Calculate()
    UpdateUI()
}
// Cycle Estimations
function CycleDown() {
    estimate_x -= 0.1;
    Calculate()
    UpdateUI()
}

// Run Program
function Run() {
    HTMLGet();
    Calculate();
    UpdateUI();
}