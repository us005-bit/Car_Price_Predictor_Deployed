# Car Price Prediction Model

This project builds a regression model to predict the selling price of a car based on various features like year, present price, fuel type, seller type, etc.

---

# Dataset
- Source: car_data.csv from Kaggle
- Features Used:
  - 'Year': Manufacturing year of the car
  - 'Present_Price': Current ex-showroom price
  - 'Kms_Driven': Distance driven in kilometers
  - 'Fuel_Type': Petrol/Diesel/CNG
  - 'Seller_Type': Dealer or Individual
  - 'Transmission': Manual or Automatic
  - 'Owner': Number of previous owners
- Target Variable: 'Selling_Price'

---

# Tech Stack
- Python
- Jupyter Notebook
- Libraries Used: 'Pandas', 'Numpy', 'Matplotlib', 'Seaborn', 'Scikit-learn'

---

# Workflow
1. Imported data using Pandas and used NumPy for numerical operations 

2. Data Exploration: 
   - Checked null values and data types (Missing values are handled before applying linear and polynomial regression, as these models cannot process NaN values and may produce errors or inaccurate results.)   

3. Feature Selection and Engineering:
(Feature engineering and selection are crucial to improve model accuracy by creating meaningful inputs and removing irrelevant or redundant features that could mislead the model.) 
   - Converted year to car age
   - Dropped some unwanted columns

4. Encoding: 
   - Applied one-hot encoding to categorical variables because regression models require numerical inputs. This allows the model to interpret categorical features correctly.

5. EDA(Exploratory Data Analysis):
   - Using Seaborn created a heatmap to understand relationship between features

6. Modeling
(Trained data using various models)
   - Used Linear Regression
   - Polynomial Regression

7. Regularization Techniques
(Regularization adds a penalty term to the loss function of a regression model to shrink model coefficients, preventing them from becoming too large in order to prevent overfitting, deal with multicollinearity and improve model generalization on unseen data)
(>Note: Applying regularization may reduce R² on training data, which is expected as it improves score of test data.)

   - Ridge Regularization on Linear Regression
   - Lasso Regularization on Linear Regression
   - ElasticNet Regularization on Linear Regression
   - Ridge Regularization on Polynomial Regression
   - Lasso Regularization on Polynomial Regression
   - ElasticNet Regularization on Polynomial Regression
 
8. Evaluation
   - Evaluated using R² score,Mean Absolute Error,Mean Squared Error and Root Mean Squared Error for each model

---

## Results
- Achieved highest R² score of 0.96 from Polynomial Regression without any regularization
The model explains ~96% of the variance in car selling prices

- Achieved an R² score of approximately 0.855 from rest of the models 
- Most other models explained approximately 85% of the variance

---

## How to Run
1. Clone this repository or download the files
2. Open `Project1.ipynb` in Jupyter Notebook
3. Run all cells sequentially to train and test the model

---

## Future Improvements
- Try Ensemble Techniques like Random Forest or XGBoost for better performance
- Deploy using Streamlit for an interactive web app

---

## Built by
Uddipt Shankar
## Contact me
shankar.uddipt02@gmail.com
