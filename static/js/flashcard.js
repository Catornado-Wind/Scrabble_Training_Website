let index = 0;
let totalWords = words.length

let wordDisplay = document.getElementById("word-display");
let anagramDisplay = document.getElementById("anagram-display");
let progressDisplay = document.getElementById("progress-display");

wordDisplay.textContent = words[index][0];
anagramDisplay.textContent = words[index][1];
progressDisplay.innerHTML = "&nbsp;" + (index + 1) + " / " + (totalWords) + "&nbsp;";

function prev_word(){
  if (index > 0) {
    index = index - 1;
    wordDisplay.textContent = words[index][0];
    anagramDisplay.textContent = words[index][1];
    progressDisplay.innerHTML = "&nbsp;" + (index + 1) + " / " + (totalWords) + "&nbsp;";
  }
}

function next_word(){
  if (index < words.length - 1) {
    index = index + 1;
    wordDisplay.textContent = words[index][0];
    anagramDisplay.textContent = words[index][1];
    progressDisplay.innerHTML = "&nbsp;" + (index + 1) + " / " + (totalWords) + "&nbsp;";
  }
}

document.getElementById("prev-word").addEventListener("click", prev_word);
document.getElementById("next-word").addEventListener("click", next_word);