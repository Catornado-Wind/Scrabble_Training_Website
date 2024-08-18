let numCorrect = 0;
let totalWords = answers.length;

function initQuiz(answers) {
    // Function to check the player's guess
    function checkGuess() {
        let guessInput = document.getElementById('guessInput');
        let guess = guessInput.value.trim().toUpperCase();
        let message = document.getElementById('message');

        let submitBtn = document.getElementById('submitBtn');
        let revealAnswers = document.getElementById('revealAnswers');
        
        guessInput.disabled = false;
        submitBtn.disabled = false
        
        let correctGuess = false;
        
        // Check if the guess matches any answers
        answers.forEach(answerObj => {
            if (answerObj["answer"][0].toUpperCase() === guess && !answerObj["revealed"]) {
                answerObj["revealed"] = true;
                answerObj["correct"] = true;
                correctGuess = true;
                numCorrect += 1;
            }
        });
        
        // Update the message
        if (correctGuess && numCorrect === totalWords) {
            message.textContent = "All possible words found";
            updateAnswersList();
        } else if (correctGuess && numCorrect != totalWords) {
            message.textContent = "Correct!";
            updateAnswersList();
        } else {
            message.textContent = "Try again!";
        }
        
        // Clear the input field
        guessInput.value = '';
    }

    // Function to update the answers list
    function updateAnswersList(revealAll = false) {
        const answersTable = document.getElementById('answersTable');
        answersTable.innerHTML = ''; // Clear the table

        let row;
        answers.forEach((answerObj, index) => {
            if (index % 10 === 0) {
                // Create a new row every 5 answers
                row = answersTable.insertRow();
            }

            const cell = row.insertCell();
            if (revealAll || answerObj.revealed) {
                cell.textContent = answerObj.answer;
                if (answerObj.correct) {
                    cell.style.backgroundColor = 'green'; // Green background for correct guesses
                } else if (revealAll) {
                    cell.style.backgroundColor = 'red'; // Red background for unrevealed answers
                }
            } else {
                cell.textContent = "";
            }
        });
    }

    function revealAllAnswers() {
        updateAnswersList(true);
        document.getElementById('message').textContent = "All answers revealed!";
        guessInput.disabled = true;
        submitBtn.disabled = true;
    }

    // Initialize the answers list when the page loads
    updateAnswersList();

    // Add event listener to submit on Enter key press
    document.getElementById('guessInput').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            checkGuess();
        }
    });

    // Add event listener to the buttons
    document.getElementById('submitBtn').addEventListener('click', checkGuess);
    document.getElementById('revealAnswers').addEventListener('click', revealAllAnswers);
}