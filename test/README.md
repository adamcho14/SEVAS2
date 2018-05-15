# SEVAS
**SEVAS** (**S**ystem of **E**lectronic **V**oting for **A**cademic **S**enate) 
is an open-source project of a complex electronic election system developed 
for Academic Senate in Faculty of Physics, Mathematics and Informatics,
Comenius University in Bratislava (FMPH).

The system provides a handy user interface run in an Internet browser. 
It enables students to cast their votes in elections to the Student Senate 
just using their PCs or smartphones. When voting has ended, the votes are counted 
and the final results are published.

The system ought to be minimal, yet reliable, so that it can run 
in any available Internet browser.

# What technologies are used

* _Python_ as the primary back-end programming language
* _JavaScript_, _HTML_ and _CSS_ for the front end
* _S/MIME_ protocol
* _Cosign_ to provide logging in
* _Shamir's Secret-Sharing Scheme_
* _Apache_ server
* _SQLite_ database management system (might be changed to _PostgreSQL_ or _MySQL_)

# What is done or partially done
* form used by voters to cast their votes
* form validation and vote formation
* vote collection
* vote counting
* user interface for the election commission
* form encryption using _S/MIME_ protocol for E-mail communication
* final database model
* logging in using _Cosign_

# What is to be done
* configuration of _Apache 2_ server for logging in via `Cosign`
* deployment in the structures of FMPH
* features I can't remember while writing this

You can find the structure of this project in `CONTENTS.md`.
