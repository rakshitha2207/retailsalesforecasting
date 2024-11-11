import pandas as pd
import streamlit as st
import logging

# @st.cache
class Datasets:
    def __init__(self):
        def ensure_monthly_freq(df):
            # Drop duplicate index values, if any
            df = df.loc[~df.index.duplicated(keep='first')]

            try:
                # Check if frequency can be inferred
                inferred_freq = pd.infer_freq(df.index)

                if inferred_freq is not None and inferred_freq != 'MS':
                    # Reindex to ensure monthly frequency, filling missing dates with NaN
                    full_index = pd.date_range(start=df.index.min(), end=df.index.max(), freq='MS')
                    df = df.reindex(full_index)
                    df.index.freq = 'MS'  # Ensure index frequency is set to 'MS'
                    logging.info(f"Reindexed {df.shape[0]} rows to monthly frequency.")

            except Exception as e:
                logging.error(f"Error ensuring monthly frequency: {e}")

            return df

        # Load datasets and ensure frequency
        self.train = pd.read_csv('datasets/train.csv', index_col=0, parse_dates=True).squeeze()
        self.train = ensure_monthly_freq(self.train)

        self.test = pd.read_csv('artifacts/test.csv', index_col=0, parse_dates=True).squeeze()
        self.test = ensure_monthly_freq(self.test)

        self.entire_data = pd.read_csv('datasets/entire_data.csv', index_col=0, parse_dates=True).squeeze()
        self.entire_data = ensure_monthly_freq(self.entire_data)

        self.cma = pd.read_csv('datasets/cma.csv', index_col=0, parse_dates=True).squeeze()
        self.cma = ensure_monthly_freq(self.cma)

        self.seasonal_indices_series = pd.read_csv('datasets/seasonal_indices_series.csv', index_col=0, parse_dates=True).squeeze()
        self.seasonal_indices_series = ensure_monthly_freq(self.seasonal_indices_series)

        self.residuals = pd.read_csv('datasets/residuals.csv', index_col=0, parse_dates=True).squeeze()
        self.residuals = ensure_monthly_freq(self.residuals)

        self.seasonal_indices_df = pd.read_csv('datasets/seasonal_indices.csv', index_col=0, parse_dates=True).squeeze()
        self.seasonal_indices_df = ensure_monthly_freq(self.seasonal_indices_df)

        self.hw_forecast_dev = pd.read_csv('datasets/hw_forecast_dev.csv', index_col=0, parse_dates=True).squeeze()
        self.hw_forecast_dev = ensure_monthly_freq(self.hw_forecast_dev)
        self.hw_forecast_dev_mean = self.hw_forecast_dev.iloc[:, 0]
        self.hw_forecast_dev_lower = self.hw_forecast_dev.iloc[:, 2]
        self.hw_forecast_dev_upper = self.hw_forecast_dev.iloc[:, 3]

        self.hw_forecast = pd.read_csv('datasets/hw_forecast.csv', index_col=0, parse_dates=True).squeeze()
        self.hw_forecast = ensure_monthly_freq(self.hw_forecast)
        self.hw_forecast_mean = self.hw_forecast.iloc[:, 0]
        self.hw_forecast_lower = self.hw_forecast.iloc[:, 2]
        self.hw_forecast_upper = self.hw_forecast.iloc[:, 3]

    # Function to return the relevant time series
    def get_datasets(self):
        return (self.train, self.test, self.entire_data, self.cma, self.seasonal_indices_series, self.residuals,
                 self.seasonal_indices_df, self.hw_forecast_dev_mean,
                 self.hw_forecast_dev_lower, self.hw_forecast_dev_upper, self.hw_forecast_mean,
                 self.hw_forecast_lower, self.hw_forecast_upper, self.hw_forecast)