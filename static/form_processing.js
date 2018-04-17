/**
 * Created by Adam on 09/04/2018.
 */


function countRadios(radios) {
    var num = 0;
   for (i = 0; i < radios.length; i++) {
       if ((radios[i].value == "1") && (radios[i].checked)) {
           num++;
       }
   }
   return num;
}

// TODO: Serious issue! In voting form, a voter can change their login by editing the source code. It enables them to vote as somebody else!!!
function validateForm(form, max) {
    if (countRadios(form) > max) {
        alert('Zvolili ste veľa kandidátov. Môžete najviac ' + max + '.');
        return false;
    }
    return true;
}


function createVote(radios) {
    var vote = "";
    for (i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            vote += "<";
            vote += radios[i].name.toString();
            vote += "#";
            vote += radios[i].value.toString();
            vote += ">";
        }
    }
    return vote;
}

function wipeOut(radios) {
    for (i = 0; i < radios.length; i++) {
        radios[i].value = "";
    }
}

function encryptVote(vote) {
    return vote;
}

function processForm(max) {
    var x = document.forms["voting"];

    if (!validateForm(x, max)) {
        return false;
    }
    var login = x["login"].value;
    var vote = encryptVote(createVote(x));
    wipeOut(x);
    x["submit"].value = "Submit";
    x["login"].value = login;
    x["vote"].value = vote;
    return true;
}
