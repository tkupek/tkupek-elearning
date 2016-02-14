var QueryString = function () {
  // This function is anonymous, is executed immediately and
  // the return value is assigned to QueryString!
  var query_string = {};
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for (var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=");
        // If first entry with this name
    if (typeof query_string[pair[0]] === "undefined") {
      query_string[pair[0]] = decodeURIComponent(pair[1]);
        // If second entry with this name
    } else if (typeof query_string[pair[0]] === "string") {
      var arr = [ query_string[pair[0]],decodeURIComponent(pair[1]) ];
      query_string[pair[0]] = arr;
        // If third or later entry with this name
    } else {
      query_string[pair[0]].push(decodeURIComponent(pair[1]));
    }
  }
    return query_string;
}();

window.onload = init();

function init() {
    enable_disable_question();
}

function enable_disable_question() {
    var elements = document.querySelectorAll("p[id*='enable-']");

    for(var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var questionId = element.getAttribute("data-questionId");

        if(element.getAttribute("data-value") == "False") {
            element.className = element.className.replace("hide", "");
            //document.getElementById("showSolution_" + questionId).disabled = true;
            //get_answer(element.getAttribute("data-questionId"));
        } else {


        }
    }
}


function toggle_solution(id)
{
    var element = document.getElementById("explanation_" + id);
    if (element.className == "show") {
        element.className = "hide";
    } else {
        element.className = "show";
    }
}

function show_solution(id)
{
    var element = document.getElementById("explanation_" + id);
    if (element.className == "hide") {
        element.className = "show";
    }
}

function get_answer(id) {

    var showSolutionButton = document.getElementById("showSolution_" + id);
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

    var questionId=encodeURIComponent(id);
    var token=encodeURIComponent(QueryString.token);
    var answers=encodeURIComponent(JSON.stringify(getCheckboxAnswers(id)));

    answerRequest.open("GET", "/api?id="+questionId+"&token="+token+"&answers="+answers, true)
    answerRequest.send(null)
}

function getCheckboxAnswers(id) {

    var answers = [];

    var elements = document.getElementsByName("checkbox_" + id);
    for(var i = 0; i < elements.length; i++) {
        if(elements[i].checked) {
            answers.push(parseInt(elements[i].value));
        }
    }

    return answers;
}

function parseResponse(id, responseText) {

    var correctOptions = JSON.parse(responseText);

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

