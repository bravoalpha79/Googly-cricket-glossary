//Materialize navbar, modal and "toast" initialisation
$(document).ready(function(){
     $(".button-collapse").sideNav();
     $('.modal').modal();
     let message = $(".message").text();
     Materialize.toast(message, 3000);
});

//dotenv initialisation
require('dotenv').config()

/**
 * AutoComplete search form.
 * Application code obtained from https://tarekraafat.github.io/autoComplete.js/#/
 * and adapted to project needs.  
 */
new autoComplete({
    data: {                              // Data src [Array, Function, Async] | (REQUIRED)
      src: async () => {
        // API key token
        const token = process.env.MONGO_URI;
        // User search query
        const query = document.querySelector("#autoComplete").value;
        // Fetch External Data Source
        const source = await fetch(`https://cloud.mongodb.com/api/atlas/v1.0/search?key=${token}&q=${query}`);
        // Format data into JSON
        const data = await source.json();
        // Return Fetched data
        return data.entries;
      },
      key: ["form"],
      cache: false
    },
    sort: (a, b) => {                    // Sort rendered results ascendingly | (Optional)
        if (a.match < b.match) return -1;
        if (a.match > b.match) return 1;
        return 0;
    },
    placeHolder: "Enter word...",     // Place Holder text                 | (Optional)
    selector: "#autoComplete",           // Input field selector              | (Optional)
    threshold: 3,                        // Min. Chars length to start Engine | (Optional)
    debounce: 300,                       // Post duration for engine to start | (Optional)
    searchEngine: "strict",              // Search Engine type/mode           | (Optional)
    resultsList: {                       // Rendered results list object      | (Optional)
        render: true,
        container: source => {
            source.setAttribute("id", "word_list");
        },
        destination: document.querySelector("#autoComplete"),
        position: "afterend",
        element: "ul"
    },
    maxResults: 7,                         // Max. number of rendered results | (Optional)
    highlight: true,                       // Highlight matching results      | (Optional)
    resultItem: {                          // Rendered result item            | (Optional)
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li"
    },
    noResults: () => {                     // Action script on noResults      | (Optional)
        const result = document.createElement("li");
        result.setAttribute("class", "no_result");
        result.setAttribute("tabindex", "1");
        result.innerHTML = "No Results";
        document.querySelector("#autoComplete_list").appendChild(result);
    },
    onSelection: feedback => {             // Action script onSelection event | (Optional)
        console.log(feedback.selection.value.image_url);
    }
});



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