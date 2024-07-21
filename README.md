<a name="readme-top"></a>

<div align="center">
  <h1><b>SEPSIS PREDICTION</b></h1>
</div>


 TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Sepsis Prediction ](#sepsis-prediction-api-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)
## Project Description
<!-- PROJECT DESCRIPTION -->

# Sepsis Prediction<a name="about-project"></a>

**Sepsis Prediction** This project aims to develop a machine learning-based solution to predict whether a patient will develop sepsis. Sepsis is a life-threatening condition caused by the body's response to an infection, which can lead to tissue damage, organ failure, and death. Early detection and treatment are crucial for improving patient outcomes.
The project involves training several machine learning models to predict the likelihood of a patient developing sepsis based on various input features. These models are then deployed via an API, and a user-friendly interface is created using Streamlit to allow healthcare professionals to input patient data and receive predictions.


### Feature

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|                                                                                  
| M11     | Attribute 6    |  Body mass index (weight in kg/(height in m)^2|
| BD2             | Attribute 7     |   Blood Work Result-4 (mu U/ml)|
| Age              | Attribute 8      |    patients age  (years)|
| Insurance | N/A     | If a patient holds a valid insurance card|
| Sepssis                 | Target           | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
  <ul>
    <li><a href="">Docker</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Features -->

## Key Features <a name="key-features"></a>

- **Business understanding: Understanding the project and formualating the hypotheis to test together with business questions to answer that will help in the analysis**
- **Data collection : Gathered comprehensive data on patients being tested for sepsis disease**
-**Exploratory Data Analysis(EDA): Examining and understanding the structure, patterns, and relationships within the dataset. This involved summary statistic, univariate analysis , bivariate analysis, outlier detection and handling missing values**
 **Data Cleaning: preparing the unified data ready for analysis**
 - **Visualizations: Using matplotlib and seaborn to create visually appealing charts, graphs and heatmaps to help answer the business questions**
 - **Answering Business questions: Using visualizations to answer business questions that help in analysing the dataset**
- **Hypothesis Testing: Testing formulated Hypothesis about whether Sepsis disease is common in elderly patients(40 years and above). Performing statistical analysis to test this hypothesis using Z-Test**
- **Data preparation : Transforming the dataset into a format suitable for training and evaluating ML models. Encompassing a range of tasks to improve the quality, consistency, and relevance of the data, ultimately leading to better model performance and insights. It involes checking if the data is balanced, feature engineering, data transformation, data splitting , constructing pipelines.**
- **Modelling : Creating mathematical representations (models) that learn patterns and relationships from the dataset in order to make predictions on whether a customer will churn or not.Data is trained both when balanced and unbalanced. The models trained include;Gradient_Boosting, Random_Forest, Stochastic_Gradient, SVC_Pipeline**
- **Hyperparameter Tuning : Hyperparameters are parameters whose values are set before the learning process begins. They control aspects such as the complexity of the model and its capacity to learn.Hyperparameter tuning helps improve model performance by finding the optimal settings.It prevents overfitting or underfitting of the model by adjusting hyperparameters.Proper tuning can lead to better generalization on unseen data.The steps include Use cross-validation to evaluate the performance of different hyperparameter settings.Consider the computational cost when choosing a tuning technique.Start with a coarse search space and refine it based on initial results.Monitor the performance metrics closely to avoid overfitting to the validation set.**

- **Feature Importance: Feature importance refers to a technique used to determine which features have the most significant impact on the target variable in a machine learning model.gher feature importance values indicate stronger influence on the model's predictions.Negative importance values suggest that the feature has a negative impact on the target variable.**
- **Model Evaluation : Model evaluation is the process of assessing the performance of a machine learning model on unseen data. It helps determine how well the model generalizes to new data and whether it meets the desired objectives. Classification Models:Accuracy: Measures the proportion of correctly classified instances.Precision: Measures the proportion of true positive predictions among all positive predictions.Recall (Sensitivity): Measures the proportion of true positive predictions among all actual positive instances.F1-Score: Harmonic mean of precision and recall, providing a balance between the two.**
- **saving the models: After training a machine learning model, it's important to save it for future use or deployment. Saving the model allows you to reuse it without the need to retrain from scratch.Joblib: Use libraries like Joblib or Pickle to serialize Python objects, including trained models, to disk.**
- **API Implementation: The API is built using FastAPI and serves machine learning models to provide predictions.The necessary machine learning models and the label encoder are loaded at the start of the API. These include: Support Vector, Classifier (SVC) model, Gradient Boosting model, Label Encoder for decoding predictions. The models are loaded using the joblib library.**
**A Pydantic model, DfFeatures, is defined to validate and structure the input data for the API. This model includes the following features:**

PRG (Plasma glucose)
PL (Blood Work Result-1)
PR (Blood Pressure)
SK (Blood Work Result-2)
TS (Blood Work Result-3)
M11 (Body mass index)
BD2 (Blood Work Result-4)
Age
Insurance

- **API Endpoints:**
- **Status Check Endpoint**
**The root endpoint (/) provides a status check for the API. It returns a JSON object containing the API name, a brief description, status message, and information on the loaded models.**
- **Sepsis Prediction Endpoint:**
**The /predict_sepsis endpoint accepts POST requests with patient data and an optional query parameter to select the model (SVC or gradient_boost). The endpoint processes the input data, selects the specified model, and returns the prediction along with the probability of the prediction.**
- **Streamlit Implementation**
- **Overview**
**The Sepsis Prediction application is a user-friendly interface built using Streamlit. It allows users to input patient data and predict the likelihood of sepsis. The application integrates with a backend API to perform the predictions using trained machine learning models.**

- **Page Configuration**
**The Streamlit page is configured with a title, icon, and wide layout for better user experience. The configuration is set using st.set_page_config().**

- **A title and introduction are provided to explain the purpose of the application. The markdown section gives users an overview of sepsis, the importance of early detection, and instructions on how to use the application.**

- **Input Form**
**The show_form function creates a form for users to input patient data. The form is divided into three columns to organize the input fields neatly. The features include:**

PRG (Plasma glucose)
PL (Blood Work Result-1)
PR (Blood Pressure)
SK (Blood Work Result-2)
TS (Blood Work Result-3)
M11 (Body mass index)
BD2 (Blood Work Result-4)
Age
Insurance


**The form is submitted using a button, which triggers the prediction process.**
- **Making Predictions**
**Upon form submission, the input data is sent to the backend API for prediction. The application handles the response, displaying the prediction result or an error message if the request fails.**

- **Dockerfile for API**
**Overview**
**The Dockerfile is used to create a Docker image for the Sepsis Prediction API. This image encapsulates all dependencies and configurations needed to run the API, ensuring a consistent environment across different deployments.**

- **Base Image**
**The base image used is python:3.10.11. This image includes Python 3.10.11 and provides a clean environment to set up the application.**

- **Copying Requirements File**
 **The requirements file, which lists all the dependencies for the project, is copied into the /tmp directory in the Docker image.**

- **Setting the Working Directory**
 **The working directory is set to /app, where the application code has been copied. This ensures that all subsequent commands are run in the context of this directory.**

- **Exposing the API Port**
 **The Docker container exposes port 8000, which is the port on which the API will be accessible. This allows external access to the API when the container is running.**

- **Running the Application**
 **The command to start the API is specified. uvicorn is used as the ASGI server to run the FastAPI application. The API will be accessible at host 0.0.0.0 on port 8000.**

- **Dockerfile for Streamlit Application**
- **Overview**
**The Dockerfile is used to create a Docker image for the Sepsis Prediction Streamlit application. This image encapsulates all dependencies and configurations needed to run the Streamlit app, ensuring a consistent environment across different deployments.**

- **Base Image**
**The base image used is python:3.10.11. This image includes Python 3.10.11 and provides a clean environment to set up the application.**
FROM python:3.10.11


- **Copying Requirements File**
**The requirements file, which lists all the dependencies for the project, is copied into the /tmp directory in the Docker image.**
COPY requirement.txt /tmp/requirement.txt


- **Installing Dependencies**
**The dependencies specified in the requirement.txt file are installed using pip.**
RUN python -m pip install -r /tmp/requirement.txt


- **Copying Application Code**
**The application code is copied into the /app directory in the Docker image. This includes all necessary files for the Streamlit application to function correctly.**
COPY . /app


- **Setting the Working Directory**
**The working directory is set to /app, where the application code has been copied. This ensures that all subsequent commands are run in the context of this directory.**
WORKDIR /app


- **Exposing the Application Port**
**The Docker container exposes port 8501, which is the default port for Streamlit applications. This allows external access to the Streamlit app when the container is running.**
EXPOSE 8501


- **Running the Application**
**The command to start the Streamlit application is specified. The home_page.py file is the entry point for the Streamlit app, and the app will be accessible at port 8501.**
CMD ["streamlit","run","home_page.py","--server.port=8501"]

- **Docker Compose Configuration**
**Overview**
**The docker-compose.yml file is used to define and manage multi-container Docker applications. In this project, Docker Compose is used to set up two services: the API and the Streamlit client. This setup ensures that both services can communicate with each other seamlessly within a shared network.**

- **Version**
**The version of Docker Compose being used is specified as 3.**
version: '3'

 **API Service**
**The API service is defined to handle the backend processing and predictions for the Sepsis Prediction application.**


- **Build Context: The build context is set to the ./api directory, which contains the Dockerfile and application code for the API.**
- **Ports: The API service exposes port 8000, allowing it to be accessed externally on the same port.**
- **Networks: The API service is connected to a custom network named mynetwork.**
- **Client Service**
**The client service is defined to handle the frontend interface using Streamlit, where users can interact with the application.**

services:
  api:
    build:
      context: ./api
    ports:
      - '8000:8000'
    networks:
      - mynetwork


- **Build Context: The build context is set to the ./frontend directory, which contains the Dockerfile and application code for the Streamlit app.**
- **Ports: The client service exposes port 8501, allowing it to be accessed externally on the same port.**
- **Networks: The client service is connected to the same custom network named mynetwork.**

  client:
    build:
      context: ./frontend
    ports:
      - '8501:8501'
    networks:
      - mynetwork


- **Networks**
**A custom network named mynetwork is defined using the bridge driver. This network allows the API and client services to communicate with each other.**

**Building and Deploying the Docker Containers**
**Step-by-Step Process**
1. **Building the Docker Containers**
First, I built the Docker images for both the API and the Streamlit client using the following commands:
This command reads the docker-compose.yml file and builds the Docker images based on the specified build contexts (./api for the API and ./frontend for the client).

2. **Starting the Services with Docker Compose**
After successfully building the Docker images, I started both the API and the Streamlit client services using Docker Compose:
This command creates and starts the containers for both services, ensuring they are up and running. Docker Compose handles the network setup, so both services can communicate over the defined mynetwork.

3. **Accessing the Streamlit Application**
Once the services were up, I accessed the Streamlit application via the provided link:
This link opens the Streamlit interface in a web browser, allowing users to interact with the Sepsis Prediction application. The application presents a user-friendly form where patient data can be entered to predict the likelihood of sepsis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python
- Jupyter lab
- Desktop Docker
-  Data on Patients developing Sepsis


### Setup

Create a new repository on github and copy the URL
Open Visual Studio Code and clone the repository by pasting the URL and selecting the repository destinatination

Create a virtual environment

```sh

python -m venv myvenvv

```

Activate the virtual environment

```sh
    myvenv/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```
## Usage
To run the project, execute the following command:
```sh
    jupyter notebook ML_APIs.ipynb
    docker build
    docker-compose up

```
- jupyter notebook will open the specified notebook
- users can explore the code, execute cells, and interact with the project's analysis and visualization

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Felix Kwemoi Motonyi**

- GitHub: [GitHub Profile](https://github.com/Felo10coder/Machine-Learning-API-s)
- Twitter: [Twitter Handle](https://x.com/Felo109?t=QQ7Gv-Lj-t6EyLIxYaJFGg&s=09)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/felo10)
- Medium: [Medium Profile]()
- Email: [email](felixkwemoi7@gmail.com)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcomed!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>
I would like to thank my team members for their efforts and support in this project. Starting with my team leader Dennis Gitobu, Joy Koech , Loyce Zawadi, Davis Kazungu and Evalyne Nyawira.
I would like to also thank all the free available resource made available online

<p align="right">(<a href="#readme-top">back to top</a>)</p>





