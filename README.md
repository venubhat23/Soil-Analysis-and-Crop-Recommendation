# SOIL ANALYSIS AND CROP RECOMMENDATION

Tech Stack: Python, Flask, HTML, CSS, JavaScript, Machine Learning, MySQL
Developed an advanced system that integrates machine learning and deep learning techniques to enhance crop yield through precise cultivation recommendations. Leveraged the Random Forest algorithm to analyze comprehensive soil datasets, including pH, moisture content, and nutrient levels, etc. Employed the MobileNetv2 deep learning framework to classify soil types based on visual data from soil images. This innovative approach provided farmers with data-driven insights for optimal crop selection and resource optimization, effectively combining precision farming with sophisticated machine learning models for informed decision-making.

## Installation

### 1. Extract and Locate the Project

- Download the project zip file and extract its contents to a suitable location (e.g., D:\projectcode).
  
### 2. Install Anaconda Navigator and MySQL Administrator/Query Browser

- Download and install [Anaconda Navigator](https://www.anaconda.com/products/distribution#download-section).
- Install MySQL Administrator and MySQL Query Browser from the `MYSQL` folder.

### 3. Setup the Database

- Open your SQL query browser (e.g., MySQL Query Browser).
- Locate the `Database.sql` file in the `db` folder of your project directory.
- Execute the SQL script to set up the database.

### 4. Open Anaconda Command Prompt

- Open Anaconda Navigator.
- Launch the Anaconda Command Prompt from the Navigator.

### 5. Prepare Environment for the Project

- Open Anaconda Prompt and create a new environment with Python 3.8:
  ```sh
  conda create -n tf python=3.8
- Proceed with 'y' when prompted.
### 6. Activate the TensorFlow Environment

- Activate the newly created environment:
  ```sh
  activate tf
  
### 7. Install Necessary Packages

- In the Anaconda Command Prompt, enter the following command to install the required packages:
  ```sh
  pip install -r requirements.txt

 ### 8. Navigate to the Project Directory

- Change the directory to the location where you extracted the project (e.g., D: drive):
  ```sh
  D:
  cd path\to\project\folder
  
### 9. Run the Project

- In the Anaconda Command Prompt, enter the following command to run the project:

  ```sh
  python app.py

## Deployment

### Deployed on Render
The application is currently deployed and accessible at [https://soil-analysis-and-crop-recommendation-1.onrender.com](https://soil-analysis-and-crop-recommendation-1.onrender.com).

### Deployed on Free MySQL Hosting
The MySQL database for the application is hosted on [Free MySQL Hosting](https://www.freemysqlhosting.net/).

### Alternative Deployment Options

#### AWS EC2 and RDS
Alternatively, you can deploy this application using AWS services:

1. **AWS EC2**: Host your Flask application on an Amazon EC2 instance. EC2 provides scalable compute capacity in the cloud.
2. **AWS RDS**: Use Amazon RDS to host the MySQL database. RDS offers a managed relational database service that simplifies database administration tasks.

For detailed instructions on deploying to AWS EC2 and RDS, follow these steps:

1. **Setup EC2 Instance**:
   - Launch an EC2 instance with a suitable AMI (e.g., Ubuntu).
   - SSH into the instance and install the necessary software (e.g., Python, Flask, Gunicorn).
   - Deploy your Flask application code to the instance.

2. **Setup RDS**:
   - Create an RDS instance with MySQL as the database engine.
   - Configure security groups and network settings to allow your EC2 instance to connect to the RDS instance.
   - Update your Flask application’s database connection settings to point to the RDS instance.

### Notes
- Ensure that all environment variables and configurations are correctly set for both deployment environments.
- For more details on setting up and configuring AWS services, refer to the [AWS Documentation](https://docs.aws.amazon.com/).

--- 

Feel free to adjust the content to better fit your project's specific details!