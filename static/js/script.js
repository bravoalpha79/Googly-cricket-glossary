//Materialize modal initializtion
$(document).ready(function(){
    $('.modal').modal();
});

//Function to insert additional meaning field into addword/editword templates
function addMeaning() {
    let meaningList = document.getElementsByClassName("meaning");
    let newMeaningNum = meaningList.length + 1;
    let newMeaning = document.createElement("textarea");
        
    newMeaning.id = `meaning${newMeaningNum}`;
    newMeaning.setAttribute("class", "meaning");
    newMeaning.setAttribute("name", `meaning${newMeaningNum}`);
    newMeaning.setAttribute("placeholder", `meaning ${newMeaningNum}`);
    newMeaning.setAttribute("cols", "40");

    document.getElementById("meanings").appendChild(newMeaning);
}