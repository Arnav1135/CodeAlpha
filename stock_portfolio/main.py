import pandas as pd
import matplotlib.pyplot as plt
class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Ticker', 'Shares', 'Purchase Price', 'Current Price', 'Value', 'Gain/Loss'])
        def add_stock(self, ticker, shares, purchase_price, current_price):
        value = shares * current_price
        gain_loss = (current_price - purchase_price) * shares
        new_stock = pd.DataFrame([[ticker, shares, purchase_price, current_price, value, gain_loss]],
                                 columns=self.portfolio.columns)
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
        print(f"Added {shares} shares of {ticker} at ${purchase_price} per share.")

   def remove_stock(self, ticker):
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
        print(f"Removed {ticker} from portfolio.")

  def update_stock_price(self, ticker, new_price):
        for i, row in self.portfolio.iterrows():
            if row['Ticker'] == ticker:
                self.portfolio.at[i, 'Current Price'] = new_price
                self.portfolio.at[i, 'Value'] = row['Shares'] * new_price
                self.portfolio.at[i, 'Gain/Loss'] = (new_price - row['Purchase Price']) * row['Shares']
        print(f"Updated price for {ticker} to ${new_price}")

 def display_portfolio(self):
        print("\nStock Portfolio:")
        print(self.portfolio)
        total_value = self.portfolio['Value'].sum()
        total_gain_loss = self.portfolio['Gain/Loss'].sum()
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        print(f"Total Gain/Loss: ${total_gain_loss:.2f}")
       def plot_performance(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.portfolio['Ticker'], self.portfolio['Gain/Loss'], color='skyblue')
        plt.title('Stock Portfolio Performance')
        plt.xlabel('Stock Ticker')
        plt.ylabel('Gain/Loss ($)')
        plt.show()
if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock('AAPL', 10, 150, 175)  
    portfolio.add_stock('MSFT', 5, 250, 300)  
    portfolio.update_stock_price('AAPL', 180)  
    portfolio.display_portfolio()
    portfolio.plot_performance()
    portfolio.remove_stock('MSFT')
    portfolio.display_portfolio()
