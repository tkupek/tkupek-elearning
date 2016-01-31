function toggle_solution(id)
{
    element = document.getElementById("explanation_" + id);
    if (element.className == "show") {
        element.className = "hide";
    } else {
        element.className = "show";
    }
}