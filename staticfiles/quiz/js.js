

const data = JSON.parse(document.getElementById('js_1').textContent);
wrong_answers = data['wrong_answers'];
right_answers = data['right_answers'];
wrong_answers.forEach(checkWrong);
right_answers.forEach(checkRight);
function checkWrong(id){
document.getElementById(id).style.backgroundColor = "red";
}

function checkRight(id){
document.getElementById(id).style.backgroundColor = "green";
}