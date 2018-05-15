This is the contents of this project. 
You can find here what the files are for
and how to use them:

* `collection.py` does the vote collection. 
It receives a form including the vote from `voting.py`
and inserts it to the database.

* `config.py` defines the maximum number of candidates 
to give _yes_ in a single vote. The same file must also be put 
to the `local` directory

* `functions.py` includes some functions used 
to display the list of candidates

* `index.py` code for the main page

* `server.py` server used for testing. Does not implement _Cosign_ 
authentication module

* `voting.py` displays the voting form and sends the encrypted vote
 
 These are the directories with other parts of the program. Almost every 
 directory has its own `README.md` and `CONTENTS.md`. They provide you 
 with the information about stuff you can doo with them and 
 files and directories they contain
 
* `administration` consists of code used by the election commission
used to administer paper voting

* `cosign` some _Cosign_ config files and scripts. Such files need to be
 used during configuration of the used _Apache 2_ server 
 before the real election
 
* `db` database files for database of persons and database of votes

* `key_management` code for Shamir's secret-sharing sheme 
and possible key generation

* `local` code that is run after the voting period to provide transfer
and counting of the votes

* `static` _JavaScript_ files for processing the vote 
and providing the election certificate, and _PKI.js_ library files 
(some of had to be edited for the purposes of our implementation)

* `test` this is the test implementation of the system
without _S/MIME_ encryption and _Cosign_ authentication.
We met a problem while decrypting the votes 
because we got `bad decrypt` error. We are still working
on its solution. Please, use the test version of the program
to test its other features.
