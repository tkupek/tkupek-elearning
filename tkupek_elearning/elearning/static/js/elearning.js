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
window.onbeforeunload = function() {
        if(document.getElementById("progressbar").style.width != "100%") {
            var message = document.getElementById("popup-leave-message").innerHTML;
            return message;
        }
    }

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
    if (element.className.indexOf("hide") > -1) {
        element.className = element.className.replace("hide", "show");
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
       setButtonToNext(id);
      }
      else{
       alert("Sorry, sending your answer was not successful!");
      }
     }
    }

    var questionId=encodeURIComponent(id);
    var token=encodeURIComponent(QueryString.token);
    var answers=encodeURIComponent(JSON.stringify(getCheckboxAnswers(id)));

    answerRequest.open("GET", "/api?id="+questionId+"&token="+token+"&answers="+answers, true)
    answerRequest.send(null)
}

function setButtonToNext(id) {
    button = document.getElementById('showSolution_' + id);
    button.className = button.className.replace("show", "hide");

    if(getNextQuestion(id)) {
        button = document.getElementById('next_' + id);
        button.className = button.className.replace("hide", "show");
    }
}

function scrollToNextQuestion(id) {
    var nextQuestion = getNextQuestion(id);

    if(nextQuestion) {
        location.href = "#" + nextQuestion.id;
    }
}

function getNextQuestion(id) {
    var questions = document.getElementsByName("question");

    for(var i = 0; i < questions.length; i++) {
        if(questions[i].id == "question_" + id) {
            return questions[i+1];
        }
    }
    return null;
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

    var parse = JSON.parse(responseText);
    var correctOptions = parse.options_id;
    var progress = parse.progress;

    if(parse.show_completed) {
        $('#completed-modal').modal('show');
    }

    setCorrectOptions(correctOptions, id)
    setProgress(progress)
}

function setCorrectOptions(correctOptions, id) {
    var elements = document.getElementsByName("checkbox_" + id);
        var holders = document.getElementsByName("checkbox_div_" + id);

        for(var i = 0; i < elements.length; i++) {
            var element = elements[i];
            var holder = holders[i];

            var correct = isCorrectOption(element.value);
            if(correct) {
                holder.className = holder.className + " list-group-item-success";
            } else {
                if(element.checked) {
                    holder.className = holder.className + " list-group-item-danger";;
                }
            }
            element.disabled = true;
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

function setProgress(progress) {
    progressbar = document.getElementById("progressbar");
    progressbar.style.width = progress + "%";
    progressbar.innerHTML = progress + "%";
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
