function attend(id) {
    var innerText = document.getElementById(id).innerHTML;

    if(innerText === "Go to This Event") {
        document.getElementById(id).innerHTML = "Going";
    }

    if(innerText === "Going") {
        document.getElementById(id).innerHTML = "Go to This Event";
    }
}