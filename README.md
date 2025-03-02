# Gold Price Prediction

This project is a **Gold Price Prediction Model** trained using historical market data. The model predicts the adjusted closing price of Gold ETFs based on various financial indicators.

## 📌 Important Note
This model is trained on an **older dataset** and may not accurately reflect recent market trends and prices. The predicted values should be used for **educational and research purposes only**.

## 📊 Dataset Description
The dataset consists of multiple financial indicators that influence gold prices. Below are the key columns used in the dataset:

- **Date**: The date of the recorded values.
- **Open, High, Low, Close**: Daily price movements of different assets.
- **Adjusted Close**: Adjusted closing price considering factors like stock splits and dividends.
- **Volume**: The total number of shares or contracts traded.

### 🔹 Market Indices
- `SP_Ajclose`: Adjusted Close price of S&P 500 Index.
- `DJ_Ajclose`: Adjusted Close price of Dow Jones Index.
- `EG_Ajclose`: Adjusted Close price of Eldorado Gold Corporation (EGO).

### 🔹 Exchange Rate & Commodities
- `EU_Price`: EUR/USD Exchange rate.
- `OF_Price`: Brent Crude Oil Futures price.
- `OS_Price`: Crude Oil WTI USD price.
- `SF_Price`: Silver Futures price.
- `USB_Price`: US Bond Rate price.

### 🔹 Precious Metals
- `PLT_Price`: Platinum price.
- `PLD_Price`: Palladium price.
- `RHO_PRICE`: Rhodium price.

### 🔹 Other Financial Indicators
- `USDI_Price`: US Dollar Index Price.
- `GDX_Adj Close`: Adjusted Close price of Gold Miners ETF.
- `USO_Adj Close`: Adjusted Close price of Oil ETF USO.

## 🚀 How to Use
1. Clone the repository:
   ```sh
   git clone https://github.com/Devashish10112003/gold-price-prediction.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## 📈 Predictions
- The model takes the above financial values as input and predicts the **adjusted closing price** of Gold ETFs.
- Due to outdated training data, **predictions may not match current market values**.

## 📬 Contact
If you have any questions or suggestions, feel free to reach out!
