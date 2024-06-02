const display_input = document.getElementById("inputValue")
const operators = ["-", "+", "%", "*", "/", "(", ")"]
let operations = []
let current_value = ""
// Handle Interactions
function HandleInteraction(value) {
    if (operators.includes(value)) {
        HandleOperatorInput(value)
    }
    else {
        HandleNumericInput(value)
    }
    UpdateUI()
}
function HandleNumericInput(value) {
    if (value === "." && current_value.includes(".")) {
        return
    }
    current_value += value
}
function HandleOperatorInput(value) {
    if (!current_value) {
        return
    }
    operations.push(current_value)
    operations.push(value)
    current_value = ""
}
function HandleReset() {
    current_value = ""
    operations = []
    UpdateUI()
}
function UpdateUI() {
    const display_string = operations.join(" ") + " " + current_value
    display_input.innerText = display_string.trim() ? display_string : "0"
}
function HandleEvaluate() {
    if (operations.length === 0) {
        return}
    let final_amount = operations[0]
    let prev_operator = null
    if (!current_value) {
        operations.pop()
    }
    else {
        operations.push(current_value)
        current_value = ''
    for ( let i = 1; i < operations.length; i++) {
        if (i % 2 === 0) {
            // Number
            final_amount = eval(`${final_amount} ${prev_operator} ${operations[i]}`)
        }
        else {
            // Operator
            prev_operator = operations[i]
        }
    }
    }
    operations = []
    current_value = final_amount
    UpdateUI()
}