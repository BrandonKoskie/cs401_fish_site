# The Hawaii Seafood Guide

A web application designed to assist consumers with reliable information about sustainable seafood choices in Hawaii. This platform helps users make informed decisions about local fish species while promoting ocean conservation and food security.

## Project Overview

Hawaii's ocean is vital to the islands' culture, economy, and food systems, but it faces significant threats from overfishing, climate change, habitat destruction, and pollution. Many local residents, tourists, and seafood consumers lack accessible information about which Hawaii fish species are sustainably harvested versus those that are overfished or carry health risks.

This website provides clear ratings and details to help users understand:
- **Sustainability ratings** for local fish species
- **Health information** including mercury levels and ciguatera risks
- **Preparation tips** and cultural significance
- **Consumer guides** for different dietary needs and occasions

Inspired by the Monterey Bay Aquarium's Seafood Watch program, our platform tailors sustainable seafood guidance specifically to Hawaii's unique marine ecosystem and cultural staples.

## Group Members

- **Alpha Team**
  - Brandon Koskie
  - Tallen Vidal
  - Dae'onna Butler
  - Kamryn Lopez

## How to Run the Application

### Prerequisites

Ensure you have the following installed:
- **Python 3.9+**
- **pip** (Python package manager)
- **Docker** and **Docker Compose** (optional, for containerized deployment)

#### 1. Clone the Repository
```bash
git clone https://github.com/BrandonKoskie/cs401\_fish\_site.git
cd cs401\_fish\_site
```

#### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Flask Application
```bash
python -m api.app

The website will be available at http://localhost:5000/fish
```
## Containerizing the web app 

Make sure you have cloned the Github repository before attempting to access the service through containerization. Please note anywhere it says "username" in the command instructions, you should use your dockerhub username.
Please be sure to have docker desktop open and running in the background before you begin! If you have all of th prerequisites you may begin!
#### 1. Build the docker image
```bash
[terminal]$ docker build -t username/flask-hawaii_seafood_app:1.0 .
```

#### 2. Run the docker container
```bash
[terminal]$ docker run --name "flask-hawaii_seafood_ap" -d -p 5000:5000 username/flask-hawaii_seafood_app:1.0
```
#### 3. Check to be sure your container is running and that your image was successfully built
```bash
[terminal]$ docker ps -a
```

#### 4. Access the microservice, query the webpage data
```bash
# On Windows
[terminal]$ curl http://curl localhost:5000/
[terminal]$ curl http://curl localhost:5000/fish
# On macOS/Linux
[terminal]$ curl localhost:5000/
[terminal]$ curl localhost:5000/fish
```
#### 5. Clean up and shut down your container
```bash
# Use this command to identify the hash for your container and then copy and paste it into the command below 
[terminal]$ docker ps -a

[terminal]$ docker stop hashhere

[terminal]$ docker rm hashhere

```

## Using the docker compose file
Make sure the previous instructions were successful when trying to containerize the web app using the docker file
#### 1. Spinning up the container
```bash
[terminal]$ docker compose up
 ✔ Image cs401_fish_site-flask-app Built                                                                                                                                                             6.9s
 ✔ Network cs401_fish_site_default Created                                                                                                                                                           0.0s
 ✔ Container hawaii-seafood-app    Created                                                                                                                                                           0.1s
Attaching to hawaii-seafood-app
hawaii-seafood-app  |  * Serving Flask app 'app'
hawaii-seafood-app  |  * Debug mode: on
hawaii-seafood-app  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
hawaii-seafood-app  |  * Running on all addresses (0.0.0.0)
hawaii-seafood-app  |  * Running on http://127.0.0.1:5000
hawaii-seafood-app  |  * Running on http://172.19.0.2:5000
hawaii-seafood-app  | Press CTRL+C to quit
hawaii-seafood-app  |  * Restarting with stat
hawaii-seafood-app  |  * Debugger is active!
hawaii-seafood-app  |  * Debugger PIN: 730-230-684
```

#### 2. Checking commands with curl
```bash
[terminal]$ curl http://curl localhost:5000/
[terminal]$ curl http://curl localhost:5000/fish
# On macOS/Linux
[terminal]$ curl localhost:5000/
[terminal]$ curl localhost:5000/fish
```

#### 3. Cleaning up your compose work space
```bash
[terminal]$ docker compose down

#double check by runnning this command to see that your docker workspace is cleared
[terminal]$ docker ps -a

```

## Congratulations! You have successfully ran our web app service using Dockerfile and Docker Compose!