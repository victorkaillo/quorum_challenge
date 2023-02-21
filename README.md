# quorum_challenge
Quorum Coding Challenge
## Developer:
### Victor Kaillo


### Requirements:

* Python3;
* Docker (optional to enviromment);
* Pandas (framework to parser);


## Instructions:

1. Download project: 
	 - ```git clone https://github.com/victorkaillo/quorum_challenge.git```
	 

2. Set up enviromment, you can choose:
	- virtualenv;
		# To set up enviromment virtualenv:
		1. $apt-get install python3-pip **(LINUX)**
		1. $brew install python3 **(MacOs)**

		2. $pip3 install virtualenv
		3. $virtualenv venv
		4. $source /path/to/venv/bin/activate
		5. $pip install -r requirements.txt

	- docker;
		# To set up enviromment docker:
		1. $docker build -t quorumchallenge .
		2. $docker run -it --entrypoint /bin/bash quorumchallenge -s


	- or your local python and pip;
		## if you preffer your local enviromment:
		1. Installed Python and Pip
		2. $pip install -r requirements.txt

3. Run the application.
	- $python3 src/data_extract_service.py


* **Important:**  If you choose the **docker environment**, remember that the **files** will be created **inside the container**. And you will need to have the container **running** to access them


**Thank you!**
