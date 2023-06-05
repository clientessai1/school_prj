
function ouvrePage(lien)
{
 var xhr = getXhr2();
	console.log(xhr);
 // On défini ce qu'on va faire quand on aura la réponse
 xhr.onreadystatechange = function(){
  // On ne fait quelque chose que si on a tout reçu et que le serveur est ok
  if(xhr.readyState == 4 && xhr.status == 200){
	document.getElementById('form_login').innerHTML = xhr.responseText;
  }
	
 }

 //xhr.open("GET","/api_logged_user_pages/page1",true);
 xhr.open("GET",lien,true);

// if (true)
	{

	 // Only send the token to relative URLs i.e. locally.
	 xhr.setRequestHeader("X-CSRFToken", getCookie2('csrftoken'));
	 xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
   }

 /*var formate_to_json = {"username":username , "password":password};
	xhr.send(JSON.stringify(formate_to_json));*/
  xhr.send();
  //alert("Click sur LienPage "+lien);
}


function ouvrePage1(event)
{
  event.preventDefault();
  ouvrePage("/api_logged_user_pages/page1");
}


function ouvrePage2(event)
{
  event.preventDefault();
  ouvrePage("/api_logged_user_pages/page2");
}



alert('api_logged_user_pages');


