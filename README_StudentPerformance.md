Student Performance Predictor
1.Main Objective:

The main objective of this project is to build a classification model that can predict a student’s academic performance level(High,Medium or Low) based on various personal and academic features. This model can help educators and academic institutions identify students who may need early intervention, thereby improving educational outcomes.

2.Data Description

Dataset : Students Performance Dataset from Kaggle
Records : 1000
Target Variable : Performance(High/Medium/Low)
Key Features: 
Gender
Race/Ethnicity
Parental Level of Education
Lunch Type
Test Preparation Course
Math Score
Reading Score
Writing Score
Derived Featues:
Average Score=mean of math score,reading score and writing score
Performance = Derivied from average score

3.Tech Stack
Python
Jupyter Notebook
Libraries Used: Pandas,Numpy,Matplotlib,Seaborn,Scikit-Learn

WORKFLOW

Imported data using Pandas and Numpy for numerical Operations
4.Data Exploration
Handling Missing Data : No missing values found
Looked at Data types
Differentiate between categorical and numerical data columns

5.Feature Engineering
Created avg score column by taking mean of math,reading and writing score.
Categorized students into a new column performance(High>=70,Medium>=40,Low<40)

6.Encoding
Used Label Encoder for categorical variables and encoded performance as target variable
Performed encoding of target variable separately because it's used as labels for prediction, not input features, and needs to be mapped to numeric class IDs in a consistent, controlled way. Encoding it with the rest could mix up class mappings or overwrite labels.
 
7.Imbalance Handling
Applied SMOTE to balance classes in training data as students with low performance were very few(30 out of 1000).
We handle imbalanced data to prevent the model from being biased toward majority classes, which can lead to poor precision, recall, and F1-score for underrepresented classes. This ensures the model treats all classes fairly and performs well across the full distribution.

8.Data Visualization
Class Distribution of Target using Count Plot
This helped in identifying imbalanced data
Distribution of Average Scores using Histogram Plot
Helped identify that data is normally skewed. Value of skewness is -0.299
Average Score by Gender using Boxplot
Performance vs Parental Education using Count Plot
Correlation Heat Map 

9. Model Training
Train Test Split: 80% train,20% Test

Models Trained: 
Logistic Regression
Random Forest
XGBoost

10.Evaluation Metrics Used:
Accuracy
Precision
Recall
F1 Score
Confusion Matrix Display

11.Results
Both Random Forest and XGBoost achieved 1.0(100%) accuracy and F1scores
Logistic Regression performed slightly lower achieving 0.95(95%) accuracy and precision

12.Model Recommendation
The Random Forest Classifier is recommended as the final model. It showed excellent performance across all metrics and provided interpret-able feature importance, which are valuable for educational decision making. Since our goal was interpret-ability XGBoost was not considered even though it produced similar results due to its complexity which makes it’s interpret-ability low.

13.Key Findings and Insights
Top Predictive Features:
Test preparation course
Parental Level of education
Gender
Race/Ethnicity

Insights
Students who completed test preparation tended to perform better
Higher parental education levels were associated with higher student performance
Gender differences in performance were observed and should be explored further
  

14.Future Improvements
Inculde more data like attendance etc.
Deploy model as a school dashboard tool
Compare with more models

15.How to Run
Clone this repository or download all the files
Open StudentPerformance.ipynb in Jupyter Notebook
Run all cells sequentially

16.Built By 
Uddipt Shankar
17.Contact Details
shankar.uddipt02@gmail.com



