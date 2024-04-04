document.addEventListener("DOMContentLoaded", function() {
    // Initialize variables and get questions data
    let currentQuestionIndex = 0;
    const questions = JSON.parse(document.getElementById('content').getAttribute('data-questions'));
    const content = document.getElementById('content');
    const btn = document.getElementById('revealBtn');

    // Function to display question and answer
    function displayQuestion() {
        if (currentQuestionIndex < questions.length) {
            // Get question and answer from questions array
            const question = questions[currentQuestionIndex].fields.question_text;
            const answer = questions[currentQuestionIndex].fields.answer_text;
            // Display question and hide answer initially
            content.innerHTML = `<div class='question'>Question: ${question}</div><div class='answer' style='display: none;'>Answer: ${answer}</div>`;
            btn.textContent = "Reveal Answer";
        } else {
            // Display message when no more questions left
            content.innerHTML = "No more questions.";
            btn.style.display = "none";
        }
    }

    // Display first question initially
    displayQuestion();

    // Event listener for reveal button click
    btn.addEventListener("click", function() {
        const answerElement = content.querySelector('.answer');
        if (btn.textContent === "Reveal Answer") {
            // Display answer on reveal button click
            answerElement.style.display = "block";
            btn.textContent = "Next Question";
        } else {
            // Move to next question on next button click
            currentQuestionIndex++;
            displayQuestion();
        }
    });
});

