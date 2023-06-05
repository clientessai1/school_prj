alert("A VOTRE AVIS !!111111!!");
  function salut2()
  {
	  alert("Bonjour 2");
	}
  salut2();
  alert('GOOD');

 function getCookie_APILogin(name) {
     var cookieValue = null;

     if (document.cookie && document.cookie !== '') {

         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             var cookie = cookies[i].trim();

             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
             }
         }
     }
     return cookieValue;
  }

function getXhr_APILogin(){
 var xhr = null;
 if(window.XMLHttpRequest) // Firefox et autres
	{
  xhr = new XMLHttpRequest();
	  }
 else if(window.ActiveXObject){ // Internet Explorer
  try {
   xhr = new ActiveXObject("Msxml2.XMLHTTP");
  } catch (e) {
   xhr = new ActiveXObject("Microsoft.XMLHTTP");
  }
 }
 else { // XMLHttpRequest non supporté par le navigateur
  alert("Votre navigateur ne supporte pas les objets XMLHTTPRequest...");
  xhr = false;
 }

 return xhr;
}

/**
* Méthode qui sera appelée sur le click du bouton
*/

function verifLoginData(){
 var xhr = getXhr_APILogin();
	console.log(xhr);
 // On défini ce qu'on va faire quand on aura la réponse
 xhr.onreadystatechange = function(){
  // On ne fait quelque chose que si on a tout reçu et que le serveur est ok
  if(xhr.readyState == 4 && xhr.status == 200){
	  //document.getElementById('form_login').innerHTML = xhr.responseText;
	if(xhr.responseText == 'non')
	{
	  alert(xhr.responseText);
	}else 
	  //document.getElementById('form_login').innerHTML = "<h2>Connexion R&eacute;ussie !</h2>";
	  document.getElementById('form_login').innerHTML = xhr.responseText;
  }

	
 }

 xhr.open("POST","api_login/checkLoginData",true);

// if (true)
	{

	 // Only send the token to relative URLs i.e. locally.
	 xhr.setRequestHeader("X-CSRFToken", getCookie_APILogin('csrftoken'));
	 xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
	 xhr.setRequestHeader("Accept", "application/json");
	 xhr.setRequestHeader("Content-Type", "application/json");
   }

  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  //alert(username +' - '+password);
 //var formate_to_json = {"no1": val_input_no1 , "no2": val_input_no2};
 var formate_to_json = {"username":username, "password":password};
	xhr.send(JSON.stringify(formate_to_json));
	//xhr.send();
}

document.getElementById('form_login').addEventListener('submit', event=>{
  event.preventDefault();
  alert('submitting');
});
alert("A VOTRE AVIS !!222222!!");
