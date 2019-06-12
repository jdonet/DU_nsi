//metho permettant de récupérer les varibvales GET
//src : https://www.creativejuiz.fr/blog/javascript/recuperer-parametres-get-url-javascript
function $_GET(param) {
	var vars = {};
	window.location.href.replace( location.hash, '' ).replace( 
		/[?&]+([^=&]+)=?([^&]*)?/gi, // regexp
		function( m, key, value ) { // callback
			vars[key] = value !== undefined ? value : '';
		}
	);

	if ( param ) {
		return vars[param] ? vars[param] : null;	
	}
	return vars;
}

function showQuestions(){
  //récupération de la variable GET en js
  var fichier = $_GET('fichierQuestions')
  readJSON(fichier)
}

//https://www.quora.com/In-JavaScript-how-do-I-read-a-local-JSON-file
function readJSON(path) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', path, true);
    xhr.responseType = 'blob';
    xhr.onload = function(e) { 
      if (this.status == 200) {
          var file = new File([this.response], 'temp');
          var fileReader = new FileReader();
          fileReader.addEventListener('load', function(){
            fillForm(fileReader.result);
          });
          fileReader.readAsText(file);
      } 
    }
    xhr.send();
}

function fillForm(res){
  //on vide la zone
  document.getElementById("form").innerHTML="";

  //parse du fichier
  var res = JSON.parse(res);
  //recupération des questions
  var questions = res.questions;
  var i=1;
  var titre = document.createElement("h1");
  var newContent = document.createTextNode(res.name);
  // ajoute le nœud texte au nouveau titre
  titre.appendChild(newContent);
  //ajout du titre du quizz
  document.getElementById("form").appendChild(titre);


  //parcours des questions
  questions.forEach(function(question) {
      
      // crée un nouvel élément div
    var newDiv = document.createElement("div");
    var title = document.createElement("h3");
    // et lui donne un peu de contenu
    var newContent = document.createTextNode(i+"- "+question.questiontext);
    // ajoute le nœud texte au nouveau titre
    title.appendChild(newContent);
    // ajoute l'élément titre au nouveau div créé
    newDiv.appendChild(title);
    
    //ajout des éléments avec appendChild https://www.grafikart.fr/tutoriels/dom-774
    var answers  = addAnswers(question,i);
    //ajout de ma div réponses à ma div question
    newDiv.appendChild(answers);
    // ajoute l'élément titre au nouveau div créé
    document.getElementById("form").appendChild(newDiv);
    i++;
  });
}

function addAnswers(question,nb){
  //recupération des réponses
  var answers = question.answers;
  var i=1;
  // crée un nouvel élément div
  var div = document.createElement("div");
  //si on a une réponse unique
  console.log(answers.length)
  if(answers.length<=2){
    var input = document.createElement("input");
      input.type = "text";
      input.name=nb;
      input.value = answers[0].text
      div.appendChild(input);
       

  }else{
    //si on a une réponse choix multiple
    //parcours des questions
    answers.forEach(function(answer) {
      //Création des boutons radio pour les réponses
      var input = document.createElement("input");
      input.type = "radio";
      input.name=nb;
      div.appendChild(input);
      //ajout du texte de la radio button
      var txt = document.createTextNode(i+"- "+answer.text);
      div.appendChild(txt);
      //ajout du saut de ligne
      var br = document.createElement("br");
      div.appendChild(br);
      i++
    });
  }
  return div
}