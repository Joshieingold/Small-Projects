// Getting inputs
let your_score = 0;
let their_score = 0;
let percent_complete = "";
let one_four = "";
let one_five = "";
let one_six = "";

// Get Information from HTML
function HTMLGet() {
    your_score = (document.getElementById("your_score_find"));
    their_score = document.getElementById("their_score_find");
    your_score = Number(your_score.value)
    their_score = Number(their_score.value)
}
// Calculate Data
function Calculate() {
    your_score = Number(your_score);
    their_score = Number(their_score);
    percent_complete = "You are " + Math.round(your_score / their_score * 100) + "% Complete";
    one_four = "You need to solve " + Math.round((their_score - your_score) / 1.4) + " more 1.4 rated problems to achieve your goal.";
    one_five = "You need to solve " + Math.round((their_score - your_score) / 1.5) + " more 1.5 rated problems to achieve your goal.";
    one_six = "You need to solve " + Math.round((their_score - your_score) / 1.6) + " more 1.6 rated problems to achieve your goal.";

}
// Update UI
function UpdateUI() {
    onefour_html.innerText = one_four;
    onefive_html.innerText = one_five;
    onesix_html.innerText = one_six;
    percent_complete_html.innerText = percent_complete;
}

// Run Program
function Run() {
    HTMLGet();
    Calculate();
    UpdateUI();
}