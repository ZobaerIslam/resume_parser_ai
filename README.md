# Resume Parser AI

This project is a resume parser that uses AI to categorize resumes into different job categories. It provides a web interface built with Streamlit to upload and analyze resumes.

## Features

- Parses resumes in PDF and DOCX format.
- Predicts the job category of the resume using a pre-trained KMeans model.
- Provides a user-friendly web interface to upload and analyze resumes.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

There are two ways to use this project:

### Web Application

To run the web application, use the following command:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your browser. You can then upload a resume file and see the predicted job category.

### Command-Line Tool

To use the command-line tool, run the following command:

```bash
python main.py <path_to_resume>
```

Replace `<path_to_resume>` with the path to the resume file you want to analyze. The predicted job category will be printed to the console.

## File Descriptions

- `app.py`: The main file for the Streamlit web application.
- `main.py`: The main file for the command-line tool.
- `train.py`: A script to train the model with a custom dataset.
- `engine.py`: Contains the core logic for parsing resumes and making predictions.
- `utils.py`: Contains utility functions for cleaning text and handling files.
- `kmeans_model.joblib`: The pre-trained KMeans model.
- `vectorizer.joblib`: The pre-trained TF-IDF vectorizer.
- `requirements.txt`: A list of the Python packages required to run the project.
- `dummy_resume_data.csv`: A CSV file containing dummy resume data.
- `data/UpdatedResumeDataSet.csv`: The dataset used to train the model.

## Rebuilding the Model

To rebuild the model with your own dataset, you can use the `train.py` script.

Your dataset must be a CSV file containing a 'Resume' column with the resume text.

To train the model, run the following command:

```bash
python train.py <path_to_your_dataset.csv> --num_clusters <number_of_categories>
```

-   `<path_to_your_dataset.csv>`: The path to your CSV dataset.
-   `<number_of_categories>` (optional): The number of job categories you want to create. The default is 5.

This will create two new files: `kmeans_model.joblib` and `vectorizer.joblib`. These new files will replace the old model and vectorizer.
