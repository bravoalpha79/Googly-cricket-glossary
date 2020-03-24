//Materialize navbar, modal and "toast" initialization
$(document).ready(function(){
     $(".button-collapse").sideNav();
     $('.modal').modal();
     let message = $(".message").text();
     Materialize.toast(message, 3000);
});



//Custom function to insert additional meaning field into addword/editword templates
function addMeaning() {
    let meaningList = document.getElementsByClassName("meaning");
    let newMeaningNum = meaningList.length + 1;

    let newMeaningRow = document.createElement("div");
    let newMeaningWrapper = document.createElement("div");
    let newMeaningTextarea = document.createElement("textarea");
    let newMeaningLabel = document.createElement("label")
    
    newMeaningRow.setAttribute("class", "row");

    newMeaningWrapper.setAttribute("class", "input-field col s8")

    newMeaningTextarea.id = `meaning${newMeaningNum}`;
    newMeaningTextarea.setAttribute("class", "meaning materialize-textarea");
    newMeaningTextarea.setAttribute("name", `meaning${newMeaningNum}`);

    newMeaningLabel.setAttribute("for", `meaning${newMeaningNum}`)
    newMeaningLabel.innerHTML = `meaning${newMeaningNum}`;
    
    newMeaningWrapper.appendChild(newMeaningTextarea);
    newMeaningWrapper.appendChild(newMeaningLabel);
    newMeaningRow.appendChild(newMeaningWrapper);

    document.getElementById("meanings").appendChild(newMeaningRow);
}