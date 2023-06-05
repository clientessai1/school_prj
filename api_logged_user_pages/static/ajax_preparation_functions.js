
 function getCookie2(name) {
     var cookieValue = null;
	 //alert('getCookie2 - 1'+document.cookie );
     if (document.cookie && document.cookie !== '') {
	 //alert('getCookie2 - 2');
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             //var cookie = jQuery.trim(cookies[i]);
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


function getXhr2(){
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
  alert("Votre navigateur ne supporte pas les objets XMLHTTPRequest...2");
  xhr = false;
 }

 return xhr;
}
