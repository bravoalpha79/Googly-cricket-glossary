# Googly - The glossary of Cricket

Googly is a web-based glossary of the game of Cricket, open to contributions by owner-authorised users.

## UX

The site is intended for experts, players or fans of the game of Cricket or any other users interested in the terminology of the game.  
Visitors have the option of searching for a specific term, or browsing the index of words by letter.   
Owner-authorised users ("contributors") have the additional options of adding new entries, editing/updating existing entries and deleting entries.
 
### User stories
Given the intended purpose of the glossary, the following user stories have been identified:

1. As a user I want to have a search box so I can quickly find the desired word (or set of words beginning with the input character(s)).
2. As a user, I want to have a letter index so I can browse through the glossary entries by letter.
3. As a user, I want to be able to display the selected word and its meaning(s).
4. As a user, I want to have a message form so I can contact the site owner.
5. As a user-contributor, I want to be able to add a new entry to the glossary. This includes adding a term and its meaning(s). 
6. As a user-contributor, I want to be able to edit/modify an existing entry. This includes modifying both the term and its meaning(s).
7. As a user-contributor, I want to be able to add meanings to an existing entry.
8. As a user-contributor, I want to be able to delete an existing entry.
9. As a user-contributor, I want to have a confirmation/warning before deleting an entry.
10. As a user-contributor, I want to have a check when entering/modifying a word so I do not accidentally create a duplicated entry.
11. As a user-contributor, I want to have a check when entering/modifying a word so I do not accidentally create an invalid/empty entry.
12. As site owner, I want to have the user messages (sent via the contact form) sent to my specified email address.
13. As site owner, I want the user messages to contain their name and email address so I can contact them back.
14. As site owner, I want to have a Contributor authorisation feature that prevents non-authorised users from modifying site content. 


### UI structure

The following UI elements were identified as essential for the implementation of the user stories:
- navigation bar/menu;
- word search box;
- letter index;
- new entry form;
- edit entry form;
- delete confirmation prompt;
- contact form;
- login form.

The initial design idea was to implement the navigation as a sidebar on desktop screens and as top navigation on screens of width 992px or less.
However, this presented problems with consistent placing and responsiveness of the search box and the letter index, as well as leaving too much of empty screen real estate on desktop resolutions.   

Thus the final design (in cooperation with the project mentor) was to implement: 
- a [Materialize](https://materializecss.com/) top navbar on all screen resolutions, responsive only with regards to its display mode;
- a custom bottom "searchbar" (just above the Footer) integrating the Search box and the Letter Index.

These two features would be a part of the "base" HTML template and would be displayed across all pages/templates, whereas all other content (search results, entries, forms) would be displayed in the screen real estate between the navbar and the searchbar.  

## Features
### Existing features 
#### Navbar

The top navbar was implemented using the Materialize Navbar component.  
On desktop screen sizes (992px and above), the navbar displays the "brand logo" and the navigation links. 
On screen sizes below 992px, the navbar displays the "brand logo", while a "burger icon" opens the navigation links in a side slide-in menu.
The navigation links contents change depending on whether the user is logged in as Contributor or not.

#### Searchbar

The searchbar contains a Materialize Search box, followed (below it) by a Letter Index with links to individual alphabet letters. 
Using the Search box returns all entries starting with the same input character(s).
Using a Letter Link displays all entries starting with the specified letter. 

#### Contributor authorisation
The Contributor authorisation feature was implemented for exercise purposes and to prevent a random visitor from modifying the contents of the glossary without contacting the site owner.   
Therefore no advanced security was implemented for this feature (as this is outside the scope of the project) - the authorisation merely consists of a check whether the entered credential can be found in the database, in a collection named "Contributors", as an existing passkey.
If the Contributor authorisation is successful, the UI displays additional options to the user.

#### Contact form
For non-registered users, a contact form is available which uses [emailJS](https://www.emailjs.com/) to send the user's message to the site owner. This is intended primarily as a means to obtain Contributor credentials from the site owner, but can also be used for general questions.  

_Note: with the implemented UI layout, the contact form is not available to users logged in as Contributor. It is assumed that, if a user is a Contributor, the "first contact" with the owner has already been made, and subsequent messaging will be performed through personal email directly._ 

#### Create-Read-Update-Delete (CRUD)

The Read function is implemented via a simple centred box displaying the word/term and its meanings. (For Contributors, this is complemented by an Edit button and a Delete button.)   
The Create function (Contributors only) uses a Materialize form. Initial fields (Term and Meaning 1) are mandatory, while the user has the option of dynamically adding multiple meanings through an additional "Add meaning" button.   
The Update function (Contributors only) also uses a Materialize form, with the same rules as for Create.   
The Delete function (Contributors only) is implemented via the Delete button below an existing entry. The user is prompted by a distinct warning (modal) to confirm or cancel the deletion. 

Implemented checks: 
- the first character of the entry's term (word) must be a letter;
- the entry's term (word) must not be empty;
- the first meaning of an entry must not be empty;
- the Create function must not result in a duplicated entry (check on term only);
- the Edit function must not result in a duplicated entry (check on term only). 

### Features left to implement

1. Add additional fields/properties to the entry:
    - word type (noun, verb, adjective);
    - alternate forms of the same term;
    - example uses (like in a dictionary).

2. Add an autocomplete searchbox that would search the database and provide automatic word suggestions based on the input characters.

## Technologies Used

The languages, frameworks, libraries, and other tools used during this project: 

- HTML for page structure and content;
- CSS for content styling;
- JavaScript for HTML DOM manipulation and for emailJS service processing;
- Python3 for backend processing and application logic;
- [Flask](https://github.com/pallets/flask) framework, including [Jinja](https://github.com/pallets/jinja) templating language, for advanced template routing and manipulation;
- [Materialize](https://materializecss.com/) was used for responsive design, navigation bar, buttons, forms and modal implementation;    
- [jQuery](https://jquery.com/) to enable the use of the Materialize library;
- [MongoDB](https://www.mongodb.com/) for database provision;
- [emailJS](https://www.emailjs.com/) to forward application user messages to an email address;
- Fonts were obtained from [Google Fonts](https://fonts.google.com/);
- Icons were obtained from Materialize;
- [Favicon.io](https://favicon.io/) was used for favicon creation;
- [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML and CSS code;
- [JSHint](https://jshint.com/) was used to validate JavaScript code;
- [PEP8 online](http://pep8online.com/) to validate Python code;
- [W3schools.com Color Converter](https://www.w3schools.com/colors/colors_converter.asp) was used to convert colours between default, HEX and RGB for CSS coding purposes;
- [Autoprefixer CSS online](https://autoprefixer.github.io/) was used for correct vendor prefixing of CSS styles where required;
- [Convertio](https://convertio.co/eps-jpg/) was used for image conversion from SVG to JPEG;
- [Compress JPEG](https://compressjpeg.com/) for image file size reduction;
- Google Chrome Developer Tools were used for development and testing, debugging and as a styling aid;
- [Gitpod](https://www.gitpod.io/) was used as the IDE for development and Git version control;
- [GitHub](https://github.com/) was used for source code storage;
- [Heroku](https://www.heroku.com/) for application online deployment.


## Testing

1. Automatic testing was not conducted.

2. All code (HTML, CSS, JavaScript, Python) was validated using online validators:

- [W3C Markup Validation Service](https://validator.w3.org/) for HTML and CSS;
- [JSHint](https://jshint.com/) for JavaScript;
- [PEP8 online](http://pep8online.com/) for Python code.

No issues were identified except where related to the use of Jinja in HTML, which the W3C Validator raises as errors.

3. Extensive testing was performed during development - basically any significant feature addition was immediately tested. Several bugs were identified in the process and corrected:
- When a term's first letter was changed during an update, the entry still kept the "letter" property of the original term (before the update), causing the updated word to appear in the wrong letter index.   
This was fixed by adding the "letter" property to the list of properties to be amended by the update.
- Following a logout, if a refresh was clicked (accidentally or intentionally), a Werkzeug error was displayed.   
Fixed by adding a condition to simply render index.html if username is not in session and logout is invoked.

4. User stories have been tested individually. 
During the tests, the following issue has been identified:
- Message can be sent with an empty message text field.   
Fixed by adding the "required" attribute to the form textarea tag in the contribute.html template. 
HTML code revalidated OK.
Subsequent testing of the form tested OK.
- The toast message when an invalid character is entered is misleading - national characters are also letters, but they are not accepted.
Fixed by modifying the corresponding flash message text.


## Deployment

**The final version of the application has been deployed online at:**   
**https://googly-cricket-glossary.herokuapp.com/**

The following procedure was used for deployment on Heroku:

1. In Gitpod CLI, in the root directory of the project, run 

   `pip3 freeze --local > requirements txt`

   to create a `requirements.txt` file containing project dependencies.

2. In Gitpod project workspace root directory, create a new file called Procfile (capital "P" is important!).  
   Open the Procfile. Inside the file, enter:  

   `web: python3 app.py`

    Save the file.

3. **Make sure you do a Git commit after creating the requirements.txt and the Procfile.**

4. On [Heroku](https://www.heroku.com/), sign in using your username and password.

5. On Heroku Dashboard, press the "New" button, then select "Create new app".

6. Enter the app name (note: name must be unique!) and select your region.   
   Press "Create app".

7. On Heroku App Dashboard, select the Settings tab.

    Under "App information", copy the Heroku git URL.

8. In Gitpod workspace CLI, in the project's root directory, enter  

    `heroku login`   

    Follow the instructions to login.

    Enter 

    `git remote add heroku <Heroku Git URL>`

    where `<Heroku Git URL>` is the Heroku git URL copied from the Heroku App Dashboard in Settings (step 7 above).

    Finally, enter

    `git push heroku master`

    to push the contents of your local Git repository to the newly created Heroku remote repository.

9.  Still in the Gitpod workspace CLI, enter 

     `heroku ps:scale web=1`
        
     to start the Heroku web process.

10. Log into your [MongoDB Atlas](https://account.mongodb.com/account/login) account.   

    In the dashboard, select your database Cluster, then click the Connect button.

    In the pop-up, select the option "Connect your application". 

    Under the tab "Connection string only", copy the connection string.


11. On Heroku App Dashboard, in the Settings tab, click the button "Reveal Config vars".

    Using the Add button, add the following keys and their corresponding values:

    key: `IP`  
    value: `0.0.0.0`

    key: `PORT`   
    value: `5000`   
    
    key: `MONGO_URI`   
    value:   
    - paste the string copied from MongoDB,
    - inside the pasted string, replace `<password>` with your database access password (**NOT** your MongoDB login password), and
    - replace `test` with the name (case-sensitive!) of the database used for your project.

    key: `SECRET_KEY`   
    value: value of SECRET_KEY as entered in the project's env.py file, **without quotes** . 

12. In the top right corner of the Heroku App Dashboard, click on the More button.

    From the dropdown menu, select "Restart all dynos". Confirm Restart when prompted.


13. Click on Open app. The App is now deployed.

### Local development

If you want to run this project locally, you will need to follow these steps.

1. Clone or download this repository.

2. Upload the repository into your IDE of choice.  

I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE.

3. In your workspace CLI, run

   `pip3 install -r requirements.txt`

   to install the project-required dependencies.

4. In the root directory of your project, create an env.py file. 

   Don't forget to add the env.py file to your .gitignore file.

5. In MongoDB Atlas, create a new database for the project.

    The database needs to have the following attributes:

    - collection "contributors"
    - collection "entries"

    In collection "contributors":
    - document property: "passkey" -> String

    In collection entries:
    - document property: "term" -> String
    - document property: "letter" -> String
    - document property: "meanings" -> Array of Strings

6. Once you have created the database, go back to the Cluster View and click "Connect".
    In the resulting pop-up, click on "Connect your application".
    Under the tab "Connection String Only", copy the connection string.

7. Back in your IDE, open the env.py file.

   At the top of the file, add 

   `import os`

   Then, add 

   `os.environ["MONGO_URI"] = "<mongo_uri>"`
    
    where `<mongo_uri>` is the pasted MongoDB connection string copied in step 6 above.

   In the pasted `<mongo_uri>` string:
   - replace < password > with your database access password (**NOT** your MongoDB login password), and
   - replace "test" with the name (case-sensitive!) of your project database. 

   Finally, add

   `os.environ["SECRET_KEY"] = "<your_secret_key>"`

    where `<your_secret_key>` is a combination of letters, numbers and characters of your choice. This is used to enable the Flask flash messaging feature.

    Save the file.

8. Log into [emailJS](https://www.emailjs.com/) or create an account if you don't already have one.

   Add a mail service of your choice, but make sure that the "service ID" field is named "gmail" (case-sensitive!).

9. In emailJS, create a new email template, named "googly". Open the template to edit it.

   In the Subject field, enter a subject title of your choice.

   In the Content field, enter the following: 
 
   ```
   {{contributor_request}}
 

   {{from_name}} can be contacted at {{from_email}}
   ```

   Finally, in the right-hand details column, enter the following:

   "To email" field: email of your choice  
  
   "From name (optional)" field: `{{from_name}}`

   "From email (optional)" field: `{{from_email}}`

   Save the template.

10. In emailJS dashboard, click on Account. Select the "API keys" tab.

    Copy the User ID string **only**.


11. In your IDE, open the base.html file. Scroll down to the scripts.

    In the `emailjs.init` function, replace the string between the quotes with your ID User string copied from emailJS (keep the quotes!).

    Save the file.

12. Run the app.py file and open it in your browser.   
    The application is now running locally.


  


## Credits

### Code
#### HTML and CSS
- The home page heading animation code was copied and adapted from the CSS Fundamentals lessons by [Code Institute](https://courses.codeinstitute.net/);
- the ::placeholder targeting method and the code for Materialize toast positioning were obtained from [Stack Overflow](https://stackoverflow.com/);
#### JavaScript
- the emailJS sendMail function was copied and adapted from the Interactive FrontEnd Development lessons by Code Institute;
- the Page Reload method was obtained from Stack Overflow;

#### Python/Jinja
- the session.pop() method and the Jinja version of the Python len() command were obtained from Stack Overflow;
- the list comprehension code was obtained from [DataCamp](https://www.datacamp.com/);
- the key-value iteration code was obtained from [W3Schools](https://www.w3schools.com/);

### Media
- Pictures were obtained from the following sources:
    - Wallpaper for all pages except Contribute: [Pixabay](https://pixabay.com/);
    - Contribute page wallpaper: [Pexels](https://www.pexels.com/);
    - Favicon picture: [Free SVG](https://freesvg.org/);
    - Navigation bar "brand logo": [Wikipedia](https://www.wikipedia.org/);   
    
- The existing glossary terms and their definitions were obtained from [Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_cricket_terms).

### Acknowledgements



