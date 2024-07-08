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
  
  
