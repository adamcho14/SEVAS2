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

/*async function encryptVote(vote) {
    //var openpgp = require('openpgp');
    //openpgp.initWorker({ path:'openpgp.worker.js' });
    //openpgp.config.aead_protect = true;
    var options, encrypted;
    var pubkey = '-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5YfZnqDq6CyPsn+vtHhZOw32Fs4Y7uun5BgxGV3TvMLYOspXiSnPY8Pv7dOgI08kSw5HbpD5vYv2vfTCMqJAwRSQlrXe95L4zqufKnU4V69ScC+79mafX36H19amC4tfNdRzW0YkALziVWiQf1Q5oOVvLTqchAKSxkCZ3HRhEkQIDAQAB-----END PUBLIC KEY-----';
    var privkey = "-----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQC5YfZnqDq6CyPsn+vtHhZOw32Fs4Y7uun5BgxGV3TvMLYOspXiSnPY8Pv7dOgI08kSw5HbpD5vYv2vfTCMqJAwRSQlrXe95L4zqufKnU4V69ScC+79mafX36H19amC4tfNdRzW0YkALziVWiQf1Q5oOVvLTqchAKSxkCZ3HRhEkQIDAQABAoGAUWdM9hOPRiaiLcPDq6msjgWV1uIQLaZUG3+mYDUDKg0vxKBy5J1g5YBchfy97zJgdxbds58Zs3u6fhbw/LMALREePG/3RCIFbzNR9rCdo0zwKwQi9M2St87CONxQEMK3fL5bhJFRcegKz2A6tit6Ulpu/zh8GL4WluGhI8zO1oECQQD4GcZazAT7M2fzrf8uihhyxDk/qr1AII0+1nS+OOKPH4q8mSgd7NhYnnbTnMk6CKDPbMCoANLUXcn/8ThgbRRpAkEAv0j78ET1X6m0z7/sd1IAZ0JzhONMP1gGfefip7aJbC5B/iEy7/naE6fXcJLGTE8m7c8lDteKe+rFr8UKPDEJ6QJBAMTOFWWjH3Rw883+QUWWsAwiEdOqShObfs/Q6KyYjUfBWpl+2K7cWUX69gGpBortmzrPZwgeFx/1Ai7wF6uN+7kCQBo1Eqd5mzCvHKG2BtzWNE3xcchMJ/8pvUH0yj32KV/T+qCpxcPRNIqq3T6ELXz4/zlnvwkIiOWvZcRON7fFdDkCQQCh2ACI1aGfvoQF3Ot6zY9H/W5vULnOw0xO3NBDuFxhvUkk9veiqk234mFbRCdHuD0rE5pZ157LfKiK78u80avw-----END RSA PRIVATE KEY-----";
    var passphrase = 'passphrase';

    var privKeyObj = openpgp.key.readArmored(privkey).keys[0];
    await privKeyObj.decrypt(passphrase);

    options = {
        data: vote,
        publicKeys: openpgp.key.readArmored(pubkey).keys
    };

    return await openpgp.encrypt(options);*/

    /*return openpgp.encrypt(options).then(function (ciphertext) {
        encrypted = ciphertext.data;
    });*/



    //return smimeEncrypt(vote);
    //return vote;
    //return btoa(encrypted);
//}

async function processForm(max) {
    var x = document.forms["voting"];

    if (!validateForm(x, max)) {
        return false;
    }
    var login = x["login"].value;
    //var vote = smimeEncrypt(createVote(x));
    wipeOut(x);
    x["submit"].value = "Pošli hlas";
    x["login"].value = login;
    //x["vote"].value = vote;
    await smimeEncrypt(createVote(x));
    return true;
}

/*async function processForm(max) {
    var x = document.forms["voting"];
    if (!validateForm(x, max)) {
        return false;
    }
    var login = x["login"].value;
    var vote;
    encryptVote(createVote(x)).then(function (ciphertext) {
        vote = ciphertext.data;
        console.log(vote);
        wipeOut(x);
        x["submit"].value = "Submit";
        x["login"].value = login;
        x["vote"].value = vote;
        x.submit();
    }, console.log("chyba"));

    return false;
}*/
