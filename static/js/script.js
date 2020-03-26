//Materialize navbar, modal and "toast" initialisation
$(document).ready(function(){
     $(".button-collapse").sideNav();
     $('.modal').modal();
     let message = $(".message").text();
     Materialize.toast(message, 3000);
});

//dotenv initialisation
require('dotenv').config()

//function for {sending the Contributor contact form via emailJS
function sendMail(contactForm) {
    const name = `${contactForm.firstname.value} ${contactForm.lastname.value}`;
    let message;
    emailjs.send("gmail", "googly", {
        "from_name": name,
        "from_email": contactForm.email.value,
        "contributor_request": contactForm.contributormessage.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            message = `Thank you, ${name}. Your message has been sent.`;
        }, 
        function(error) {
            console.log("FAILED", error);
            message = `Sorry, something went wrong. Message not sent.`;  
    })
    .then(
        function () {
            Materialize.toast(message, 4000);
            setTimeout(function() {
                window.location.href = "";
            }, 2000)
        })

    return false;
}

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