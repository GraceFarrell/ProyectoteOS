<h1> Operating System Project: Taqueria Simulation </h1>
<p> This repository presents the documentation of our Operating Systems Final Project, which consists in simulate the way  "Tacos Franc" manage the orders of its customers.</p>		
<h2> Table of Contents </h2>
<UL type = disk> 
  <LI> <a href = "#1"> 1. Pre-Requisites </a></LI>
  <LI> <a href = "#2"> 2. Installation </a></LI>
  <LI> <a href = "#3"> 3. Algorithm </a></LI>
  <LI> <a href = "#4"> 4. Contribuitors </a></LI>
</UL>
<h2 id = "1"> 1. Pre-Requisites </h2>
<p> This project was developed to be run in Linux. To be able to run the project it is required to download the files of this repository. Likewise, it is important to have Python in your computer and some python modules. </p>
<h2 id = "2"> 2. Installation </h2>
<p> List of elements required to be installed to run the code </p>
<UL type = disk> 
  <LI> <h4> Python 3.6 or newest version </h4> </LI>
  <p> To install python click on the next <a href = "https://www.python.org/downloads/"> link </a></p>
  <LI> <h4> boto3 </h4></LI>
  <p> This module is used to read the queues of Amazon SQS Service. To install using the terminal, try: </p>
  <pre> sudo apt-get install pip-boto3</pre>
  <p> or </p>
  <pre> sudo pip3 install boto3 </pre>
  <p> When boto3 is installed, it is required to create the next files and folder: </p>
   <UL type = square> 
     <LI> Create a hidden folder in the home directory, called:</LI>
     <pre> .aws </pre>
     <p> Inside the folder create two files called credentials and config. </p>
     <LI> credentials</LI>
     <pre> [default]
 aws_access_key_id = YOUR_ACCESS_KEY
 aws_secret_access_key = YOUR_SECRET_KEY </pre>
     <LI> config </LI>
     <pre> [default]
 region=us-east-1 </pre>
    </UL>
  <LI> <h4> Matplotlib </h4></LI>
  <p> To install using the terminal, try: </p>
  <pre> sudo apt-get install python3-matplotlib</pre>
  <p> or </p>
  <pre> sudo pip3 matplotlib </pre>
  <LI> numpy </LI>
</UL>
<h2 id = "3"> 3. Algorithm </h2>
<h2 id = "4"> 4. Contribuitors </h2>
<UL type = disk> 
  <LI> <a href = "https://github.com/Kohina-Arisato"> Ariana Inzunza </a> </LI>
  <LI> <a href = "https://github.com/MiguelFrias97"> Miguel Frias </a> </LI>
  <LI> <a href = "https://github.com/GraceFarrell"> Natalia Cornejo </a> </LI>
</UL>
