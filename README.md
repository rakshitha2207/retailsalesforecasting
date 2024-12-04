# Retail Sales Forecasting and Monitoring
[![Made with Python](https://img.shields.io/badge/Made%20with-Python%203.9.0-blue.svg)](https://www.python.org/)

# Project Description
The  Retail Sales Forecasting and Monitoring project is designed to provide real-time analysis and forecasting for the Retail Sales. The dataset used here is related to the US market and offers valuable insights into the sales performance of the retail trade sector, which encompasses a wide range of businesses in the retail industry.

# Motivation to Monitor Sales and Build a Forecasting Model
 Retail sales here refers to the total sales value generated by retail establishments in the US. It covers various retail categories, including both durable and non-durable goods, providing a comprehensive overview of consumer spending behavior and the overall health of the retail industry.
* Monitoring sales in the retail trade sector is crucial for businesses to assess their performance, identify trends, and make data-driven decisions. By understanding sales patterns and fluctuations, businesses can adapt their strategies, optimize inventory management, and improve overall operational efficiency.

* The motivation behind building a forecasting model for Retail Sales is to provide stakeholders, such as retailers, manufacturers, and policymakers, with reliable insights into future sales trends. By forecasting future sales, businesses can proactively plan and make informed decisions about inventory management, resource allocation, and marketing strategies. 


# Data Collection and Model Development

The dataset used in this project was collected from the [Federal Reserve Economic Data (FRED) platform](https://fred.stlouisfed.org/series/RSXFSN). The data is spans from January 1992 to September 2024 and represents the Advance Retail Sales in the retail trade sector. 

The collected data is used training and evaluating the forecasting models. The forecast was then generated for a two-year period from November 2024 to September 2025. 

The dataset exhibits both trend and seasonality, requiring the use of appropriate forecasting models. Several models were considered, including:

1. **Linear Regression with Seasonal Dummies**: This model incorporates seasonal dummy variables in a linear regression framework to capture seasonal patterns and their impact on sales.

2. **Holt-Winters Model**: The Holt-Winters model is a popular method for forecasting time series data with trend and seasonality. It utilizes exponential smoothing techniques  and can capture level, trend and seasoanlity effectively.

3. **Decomposition Forecasting using Linear Regression & Seasonal Naïve**: This approach involves decomposing the time series into trend, seasonal, and residual components and then forecast each component separately. **Linear regression** was used to capture the trend and **Seasonal Naïve** was used for seasonality as this assumes that future sales will be the same as the sales from the corresponding season in the previous year. 

4. **SARIMA (Seasonal AutoRegressive Integrated Moving Average)** model was also explored to capture the underlying characteristics of the data. 

After thorough evaluation, the Holt-Winters model was selected as the optimal and efficient model for this project. The decision was based on important indicators such as high accuracy, adherence to statistical assumptions, interpretability for non-technical stakeholders, development efficiency, and the inclusion of confidence intervals.

Including confidence intervals in the forecasts is crucial as it provides an indication of the reliability and uncertainty associated with the predictions. This information is valuable for decision-making and allows businesses to account for potential variations and prepare accordingly.

The choice of the Holt-Winters model, along with the consideration of confidence intervals, ensures that the forecasting model provides reliable and actionable insights to support effective planning, resource allocation, and strategic decision-making.
![saless](https://github.com/rakshitha2207/retailsalesforecasting/blob/main/output.png)
## View Notebooks in Colab

| Notebook | Colab Link |
| -------- | ---------- |
| Data Collection | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashrafalaghbari/RetailSensei/blob/main/notebooks/data_collection.ipynb) |
| Decomposition Forecasting | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashrafalaghbari/RetailSensei/blob/main/notebooks/decomposition_forecasting.ipynb) |
| Holt-Winters Model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashrafalaghbari/RetailSensei/blob/main/notebooks/holt_winters_model.ipynb) |
| Linear Regression with Seasoanl Dummies | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashrafalaghbari/RetailSensei/blob/main/notebooks/lr_with_seasoanl_dummies.ipynb) |
| SARIMA| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashrafalaghbari/RetailSensei/blob/main/notebooks/sarimax.ipynb) |

# Worflow
![sales](workflow.png)


# Installation

Follow these steps to install and run the project locally:

Set up a virtual environment (optional but recommended):

```bash
python -m venv env
env\Scripts\activate.bat
```

```bash
git clone https://github.com/ashrafalaghbari/RetailSensei.git
cd <project-directory>
pip install -r requirements.txt
streamlit run app.py
```

Access the web application by opening the following URL in your web browser:

```bash
http://localhost:8501
```

<!-- If you prefer to use a Docker image, you can follow these additional steps:

Pull the Docker image from Docker Hub:
```bash
docker pull salesapp:0.1
```
Run the Docker container:
```bash
docker run -p 8501:8501 salesapp:0.1
```
Access the web application using the same URL as mentioned above. -->

# Usage

The interactive dashboard provides forecasted values for the next 24 months, from May 2023 to April 2025. It automatically retrieves new sales observations from FRED using the FRED API and displays them on the dashboard. The stars marker represents the actual values on the dashboard.

When a new sales observation is obtained, it is evaluated against the forecasted values to assess the performance of the model. The evaluation metrics used are MAPE (Mean Absolute Percentage Error), RMSE (Root Mean Squared Error), and MAE (Mean Absolute Error). These metrics provide insights into the model's performance and help identify outliers or the need for model retraining to adapt to changing market behavior.

The performance metrics are color-coded, with red indicating that the new observation has worsened the model's performance compared to the previous evaluation since the last observation date. The new sales observation is added to the testing set used during model evaluation and compared with the forecasted values generated during model development besides the new forecasted values dispayed on the dashboard. The two sets are evaluated using the three metrics, and the performance metrics are updated accordingly.

If the new sales observation negatively impacts the model's performance, the performance metrics will be flagged to indicate the deterioration. This serves as an alert to consider retraining the model to maintain its accuracy and adaptability to the ever-changing market dynamics.

By monitoring the performance metrics, users can track the model's reliability and identify potential issues when new observations are added.



# License

[MIT](https://github.com/ashrafalaghbari/RetailSensei/blob/main/LICENSE)


# Contact

If you have any questions or encounter any issues running this project, please feel free to [open an issue](https://github.com/ashrafalaghbari/RetailSensei/issues). I'll be happy to help!
