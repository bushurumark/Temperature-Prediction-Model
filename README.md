### Solar Weather Data Analysis Overview

This project is focused on analyzing solar weather data to predict temperature variables using various regression models. It demonstrates the entire data science process from data preprocessing, exploratory data analysis (EDA), model building, hyperparameter tuning, to model evaluation. The project employs several machine learning algorithms, including Decision Tree, Random Forest, AdaBoost, Gradient Boosting, XGBoost, and a Stacking Ensemble model to ensure the highest prediction accuracy. 

**Data Preprocessing:** Includes handling of missing values, outliers, and normalization of column names.

**Exploratory Data Analysis (EDA):** Utilizes histograms, boxplots, and heatmaps to understand the data distribution and feature correlations.

**Model Building and Evaluation:** Implements various regression models and evaluates them based on RMSE, MAE, R-squared, and Adjusted R-squared metrics.

**Hyperparameter Tuning:** Applies GridSearchCV for tuning models to improve performance.

**Feature Importance Visualization:** Offers insights into the most significant features for each model.

**Stacking Ensemble Model:** Combines predictions from multiple models to enhance the predictive power.

### Data Description:

The dataset includes various attributes related to solar weather analysis. Below is the detailed data dictionary:
Inputs

1.	### Energy delta[Wh]
•	**Description:** The change in energy consumption or production measured in watt-hours.

•	**Type:** Float

2.	### GHI
•	**Description:** Global Horizontal Irradiance, which is the total amount of shortwave radiation received from above by a surface horizontal to the ground.

•	**Type:** Float

3.	### Pressure
•	**Description:** Atmospheric pressure measured in hectopascals (hPa).

•	**Type:** Float

•	**Default Value:** 1013.25 (standard atmospheric pressure at sea level)

4.	### Humidity
•	**Description:** The amount of water vapor in the air, expressed as a percentage.

•	**Type:** Float

5.  ### Wind Speed
•	**Description:** The speed of the wind measured in meters per second (m/s).

•	**Type:** Float

6.	### Rain_1h
•	**Description:** The amount of rainfall in the last hour, measured in millimeters (mm).

•	**Type:** Float

7.	### Snow_1h
•	**Description:** The amount of snowfall in the last hour, measured in millimeters (mm).

•	**Type:** Float

8.	### Clouds_all
•	**Description:** The percentage of the sky covered by clouds.

•	**Type:** Float

9.	### IsSun
•	**Description:** A binary indicator of whether it is sunny (1) or not (0).

•	**Type:** Integer (0 or 1)

10.	### SunlightTime
•	**Description:** The amount of time the sun has been shining, measured in hours.

•	**Type:** Float

11. ### DayLength
•	**Description:** The total length of the day from sunrise to sunset, measured in hours.

•	**Type:** Float

12. ### SunlightTime/DayLength
•	**Description:** The ratio of sunlight time to the total length of the day.

•	**Type:** Float

13. ### Weather_type
•	**Description:** Categorical representation of weather conditions.

•	**Type:** Integer (1 to 5)

	1: Clear
 
	2: Clouds
 
        3: Rain
  
	4: Snow
 
	5: Other

14.	### Hour
•	**Description:** The hour of the day (24-hour format).

•	**Type:** Integer (0 to 23)

15.	### Month
•	**Description:** The month of the year.

•	**Type:** Integer (1 to 12)

### Output
1.	### Temp
•	**Description:** The predicted temperature, measured in degrees Celsius (°C).

•	**Type:** Float

### Dependencies:
• Python 3.7+

• pandas

• numpy

• scikit-learn

• matplotlib

• seaborn

### Contact Information:
For further information or queries regarding this project, please contact:
• Data Scientist: Levi Bushuru

• Email: bushurumark@gmail.com

• Phone: +254704084567 or +254704135291

