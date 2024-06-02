const empty_board = [["", "", ""], ["", "", ""], ["", "", ""]];
let game_board = JSON.parse(JSON.stringify(empty_board));  
let x_or_o = 1;
let winner = null;

let upper_text = document.getElementById("upper_text");
function DatabaseUpdate(value) {
    const [row, col] = value.split('');
    const rowIndex = row.charCodeAt(0) - 'a'.charCodeAt(0);
    const colIndex = parseInt(col) - 1;

    if (game_board[rowIndex][colIndex] === "") {
        game_board[rowIndex][colIndex] = WhichPiece();
    } else {
        return;
    }
    WinCheck();
    UpdateUI();
}
function WinCheck() {
    const lines = [
        // Rows
        [game_board[0][0], game_board[0][1], game_board[0][2]],
        [game_board[1][0], game_board[1][1], game_board[1][2]],
        [game_board[2][0], game_board[2][1], game_board[2][2]],
        // Columns
        [game_board[0][0], game_board[1][0], game_board[2][0]],
        [game_board[0][1], game_board[1][1], game_board[2][1]],
        [game_board[0][2], game_board[1][2], game_board[2][2]],
        // Diagonals
        [game_board[0][0], game_board[1][1], game_board[2][2]],
        [game_board[0][2], game_board[1][1], game_board[2][0]],
    ];

    for (const line of lines) {
        if (line[0] && line[0] === line[1] && line[0] === line[2]) {
            winner = line[0];
            return;
        }
    }
    winner = null;
}
function UpdateUI() {
    if (winner !== null) {
        upper_text.textContent = winner + " Wins!";
    } else {
        upper_text.textContent = "Play Tic Tac Toe!";
    }
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cellId = String.fromCharCode('a'.charCodeAt(0) + i) + (j + 1);
            const textElement = document.getElementById(cellId + "_text");
            if (textElement) {
                textElement.textContent = game_board[i][j];
            }
        }
    }
}
function WhichPiece() {
    if (x_or_o % 2 === 1) {
        x_or_o += 1;
        return "X";
    } else {
        x_or_o += 1;
        return "O";
    }
}
