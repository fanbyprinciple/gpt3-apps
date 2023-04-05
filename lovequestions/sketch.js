let questions = []; // Array to hold the questions
let currentQuestion = 0; // Variable to keep track of the current question
let inputField; // Variable to hold the user's answer input field

function preload() {
  // Load the text file with questions
  questions = loadStrings("questions.txt");
}

function setup() {
  createCanvas(800, 400);
  
  
  
  // Display the first question
  displayQuestion();
}

function displayQuestion() {
  // Clear the canvas
  background(220);
  
  // Display the current question
  textAlign(CENTER);
  textSize(12);
  text(questions[currentQuestion], width/2, height/2);
}
