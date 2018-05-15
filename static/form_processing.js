/**
 * Created by Adam on 09/04/2018.
 */

//vote encryption, sending login without giving the user possibility to manipulate with it
function countRadios(radios) {
    var num = 0;
   for (i = 0; i < radios.length; i++) {
       if ((radios[i].value == "1") && (radios[i].checked)) {
           num++;
       }
   }
   return num;
}

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

async function processForm(max) {
    var x = document.forms["voting"];

    if (!validateForm(x, max)) {
        return false;
    }
    var login = x["login"].value;
    wipeOut(x); //erases form data
    x["submit"].type = "submit";
    x["submit"].value = "Pošli hlas";
    await smimeEncrypt(createVote(x));
    return true;
}
