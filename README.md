# VertiSystem-Tasks
VertiSystem-Tasks

This repository contains the implementation of two tasks as per the requirements provided:

Task-1: Generate flight data, analyze and clean it.
Task-2: Model pipeline, containerization, and CI/CD for U.S. Electricity Prices dataset.

Task-1
Description
This task involves:

Generating 5000 JSON files containing random flight data for cities.
Analyzing and cleaning the generated flight data.
Producing a report with the following:
Total number of records processed.
Number of dirty records (records with NULL fields).
Average (AVG) and 95th percentile (P95) flight duration for the top 25 destination cities.
Two cities with the maximum passengers arrived and departed.
Steps to Run
Clone this repository:

git clone <repository_url>
cd VertiSystem-Tasks
Navigate to the Task-1 folder:

cd Task-1
Install required dependencies:

pip install -r requirements.txt
Run the Task-1.py script:

python Task-1.py
The results will be displayed in the terminal, including:

Total records processed.
Dirty records count.
Flight duration metrics (AVG and P95).
Cities with maximum passenger arrivals and departures.

Task-2
Description
This task involves:

Downloading and analyzing the U.S. Electricity Prices dataset.
Building a Random Forest model pipeline for predicting electricity prices.
Containerizing the pipeline using Docker.
Setting up a basic CI/CD pipeline using YAML.
Steps to Run
Prerequisites:
Install Docker on your local system: Docker Installation Guide.
Install Python 3.12+.
Install Kaggle CLI for downloading the dataset.
Step 1: Download the Dataset
Visit the Kaggle link: U.S. Electricity Prices Dataset.
Download the dataset and save it as clean_data.csv inside the Task-2/data/ directory.
Step 2: Install Dependencies
Navigate to the Task-2 folder:

cd Task-2
Install the required dependencies:

pip install -r requirements.txt
Step 3: Run the Analysis and Model Pipeline
Run the provided notebook Electricity_Prices_Analysis.ipynb to:

Analyze the dataset.
Train a Random Forest model using GridSearchCV.
Evaluate the model with Mean Squared Error (MSE).
You can run the notebook in Jupyter or Visual Studio Code.

Step 4: Containerize the Pipeline
Build the Docker image:

docker build -t electricity-prices-pipeline .
Run the container:

docker run -p 5000:5000 electricity-prices-pipeline
Access the service at http://localhost:5000.

Step 5: CI/CD Pipeline Setup
Copy the ci-cd-pipeline.yml file to your CI/CD tool (e.g., GitHub Actions, Jenkins, etc.).
The pipeline will:
Pull the latest code.
Build and test the container.
Deploy the container.
YAML Explanation
The YAML file automates the CI/CD pipeline. Key components:

Build Stage: Builds the Docker container for the pipeline.
Test Stage: Tests the containerized application.
Deploy Stage: Deploys the container to a local or cloud-based environment.
YAML is essential in CI/CD because it provides:

A declarative way to define build, test, and deployment workflows.
A standard structure that's portable across different CI/CD tools.
Automation to ensure continuous integration and deployment with minimal manual intervention.