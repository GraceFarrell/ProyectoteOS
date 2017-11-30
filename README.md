<h1> Operating Systems Project: Taco Shop "Tacos Franc" Simulation </h1>
<p> This repository presents the documentation of our Operating Systems Final Project, which consists in simulating a taco shop's,   "Tacos Franc", order management.</p>		
<h2> Table of Contents </h2>
<UL type = disk> 
  <LI> <a href = "#1"> Pre-Requisites </a></LI>
  <LI> <a href = "#2"> Installation </a></LI>
  <LI> <a href = "#3"> Algorithms </a></LI>
  <LI> <a href = "#4"> Contribuitors </a></LI>
</UL>
<h2 id = "1"> 1. Pre-Requisites </h2>
<p> This project was developed to run in Linux. To be able to run the project it is required to download the files of this repository. Likewise, it is important to have Python 3.6 or the newest version in your computer, as well as some python modules. </p>
<h2 id = "2"> 2. Installation </h2>
<p> List of elements required to be installed to run the code </p>
<UL type = disk> 
  <LI> <h4> Python 3.6 or newest version </h4> </LI>
  <p> To install python click on the next <a href = "https://www.python.org/downloads/"> link. </a></p>
  <LI> <h4> boto3 </h4></LI>
  <p> This module is used to read the queues of Amazon SQS Service. To install using the terminal, try: </p>
  <pre> sudo apt-get install pip-boto3</pre>
  <p> or </p>
  <pre> sudo pip3 install boto3 </pre>
  <p> Once boto3 is installed, it is necessary to create the following: </p>
   <UL type = square> 
     <LI> Create a hidden folder in the home directory, called:</LI>
     <pre> .aws </pre>
     <p> Inside the folder create two files called credentials and config respectively. </p>
     <LI> credentials</LI>
     <pre> [default]
 aws_access_key_id=YOUR_ACCESS_KEY
 aws_secret_access_key=YOUR_SECRET_KEY </pre>
     <LI> config </LI>
     <pre> [default]
 region=us-east-1 </pre>
    </UL>
  <LI> <h4> Matplotlib </h4></LI>
  <p> To install using the terminal, try: </p>
  <pre> sudo apt-get install python3-matplotlib </pre>
  <p> or </p>
  <pre> sudo pip3 matplotlib </pre>
  <LI> <h4> numpy </h4> </LI>
  <p> To install numpy using the terminal, try: </p>
  <pre> sudo pip3 install numpy </pre>
</UL>
<h2 id = "3"> 3. Algorithm </h2>
<UL type = disk>
<LI> <h4> Cocinar() Function Flowchart </h4></LI>
<img src = "https://user-images.githubusercontent.com/18355966/33364892-33229d5e-d49b-11e7-88fe-0e76b9235fb8.png">
<LI> <h4> Cocinar() Pseudocode </h4></LI>
<pre> Get suborder from queue
Set time of preparation by type of suborder
toPrepare = number of tacos/quesadillas/etc… left to prepare
how_many = number of tacos/quesadillas/etc… that can be prepared in given time slice
If how_many < toPrepare:
	Check for meat
	if not enough meat:
		pause suborder
		prepare meat
		continue
	for each ingredient needed, decrement inventory by how_many*10
	Decrement tortillas by how_many
Prepare how_many from suborder
Decrement toPrepare by how_many
Change suborder priority
else:
	Check for meat
	if not enough meat:
		pause suborder
		prepare meat
		continue
	for each ingredient needed, decrement inventory by toPrepare*10
	Decrement tortillas by toPrepare
	Complete suborder
</pre>
<LI> <h4> Queue_Algorithm() Function Flowchart </h4></LI>
<img src = https://user-images.githubusercontent.com/18355966/33364893-3337094c-d49b-11e7-9d28-d63f5e5d33a2.png>
<LI> <h4> Queue_Algorithm() Pseudocode </h4></LI>
<pre>while true:
for the first three orders in maximum priority queue:
		if the queue is not empty:
			work on each order for 0.2 seconds
for the first two orders in medium priority queue:
		if the queue is not empty:
			work on each order for 0.4 seconds
if the low priority queue is not empty:
		work on the first  order in queue for 0.8 seconds
if the waiting queue is not empty or the min priority queue is not empty:
		if the waiting queue is not empty:
			work on the first order in the queue for as long as it takes to finish
			complete suborder
	else if min priority queue is not empty:
			work on the first order in queue for 1.6 seconds
</pre>
</UL>
<h2 id = "4"> 4. Contribuitors </h2>
<UL type = disk> 
  <LI> <a href = "https://github.com/Kohina-Arisato"> Ariana Inzunza </a> </LI>
  <LI> <a href = "https://github.com/MiguelFrias97"> Miguel Frias </a> </LI>
  <LI> <a href = "https://github.com/GraceFarrell"> Natalia Cornejo </a> </LI>
</UL>
