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
