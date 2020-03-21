//Materialize modal initializtion
$(document).ready(function(){
    $('.modal').modal();
});

//Function to insert additional meaning field into addword/editword templates
function addMeaning() {
    let meaningList = document.getElementsByClassName("meaning");
    let newMeaningNum = meaningList.length + 1;

    let newMeaningRow = document.createElement("div");
    let newMeaningWrapper = document.createElement("div");
    let newMeaningTextarea = document.createElement("textarea");
    
    newMeaningRow.setAttribute("class", "row");

    newMeaningWrapper.setAttribute("class", "input-field col s8")

    newMeaningTextarea.id = `meaning${newMeaningNum}`;
    newMeaningTextarea.setAttribute("class", "meaning materialize-textarea");
    newMeaningTextarea.setAttribute("name", `meaning${newMeaningNum}`);
    newMeaningTextarea.setAttribute("placeholder", `meaning ${newMeaningNum}`);
    
    newMeaningWrapper.appendChild(newMeaningTextarea);
    newMeaningRow.appendChild(newMeaningWrapper);

    document.getElementById("meanings").appendChild(newMeaningRow);
}