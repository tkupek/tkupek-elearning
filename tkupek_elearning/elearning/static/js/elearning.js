function toggle_solution(id)
{
    element = document.getElementById("explanation_" + id);
    if (element.className == "show") {
        element.className = "hide";
    } else {
        element.className = "show";
    }
}

function show_solution(id)
{
    element = document.getElementById("explanation_" + id);
    if (element.className == "hide") {
        element.className = "show";
    }
}

function get_answer(id) {

    showSolutionButton = document.getElementById("showSolution_" + id);
    showSolutionButton.disabled = true;

    show_solution(id);

    var answerRequest=new ajaxRequest()
    answerRequest.onreadystatechange=function(){
     if (answerRequest.readyState==4){
      if (answerRequest.status==200 || window.location.href.indexOf("http")==-1){
       parseResponse(id, answerRequest.responseText);
      }
      else{
       alert("An error has occured making the request");
      }
     }
    }

    var questionId=encodeURIComponent(id)
    var token=encodeURIComponent("1ea6de64cf5a11e5ada41c6f6525891e")
    var answers=encodeURIComponent(getCheckboxAnswers(id))

    answerRequest.open("GET", "api?id="+questionId+"&token="+token+"&answers="+answers, true)
    answerRequest.send(null)
}

function getCheckboxAnswers(id) {

    var answers = "";

    var elements = document.getElementsByName("checkbox_" + id);
    for(var i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            answers += elements[i].value + "_";
        }
    }

    if(answers != "") {
        answers = answers.substring(0, answers.length - 1);
    }

    return answers;
}

function parseResponse(id, responseText) {

    var correctOptions = responseText.split("_");

    var elements = document.getElementsByName("checkbox_" + id);

    for(var i = 0; i < elements.length; i++) {
        var element = elements[i];
        element.className="";

        var correct = isCorrectOption(element.value);
        if(correct) {
            element.className="correct";
        } else {
            if(element.checked) {
                element.className="failed";
            }
        }
     }

    function isCorrectOption(option) {
        for(var i = 0; i < correctOptions.length; i++) {
            if(correctOptions[i] == option) {
                return true;
            }
        }
        return false;
    }
}


function ajaxRequest() {

 var activexmodes=["Msxml2.XMLHTTP", "Microsoft.XMLHTTP"] //activeX versions to check for in IE
 if (window.ActiveXObject){ //Test for support for ActiveXObject in IE first (as XMLHttpRequest in IE7 is broken)
  for (var i=0; i<activexmodes.length; i++){
   try{
    return new ActiveXObject(activexmodes[i])
   }
   catch(e){
    //suppress error
   }
  }
 }
 else if (window.XMLHttpRequest) // if Mozilla, Safari etc
  return new XMLHttpRequest()
 else
  return false
}