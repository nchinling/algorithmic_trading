# Algorithmic Trading Project

## Overview

This project implements algorithmic trading strategies using Python. It leverages finance data obtained from Yahoo Finance, and MetaTrader 5 is employed for automating the trading process. The codebase is organised into separate folders for distinct functionalities, including broker API integration, performance indicators, backtesting strategies, and technical indicators.

## Project Structure

The project is organised into the following folders:

- **broker_api:** Contains code related to the integration with MetaTrader 5.

- **performance_indicators:** Implements performance indicators for evaluating the success of trading strategies. (cagr.py, max_dd_calmar.py, portfolio_rebalance.py, sharpe_sortino.py, volatility.py)

- **backtesting_strategies:** Encompasses various strategies for backtesting, enabling evaluation of trading algorithms. (portfolio_rebalance.py, renko_macd.py, renko_obv.py, resistance_breakout.py)

- **technical_indicators:** Houses code for calculating and utilizing technical indicators for decision-making in trading. (adx.py, atr.py, bollinger.py, indicator_macd.py, renko.py, rsi.py)

## Technologies Used

- **Python:** The primary programming language for algorithmic trading logic.

- **MetaTrader 5:** Used for automated trading and interfacing with financial markets.

- **Spyder:** The integrated development environment (IDE) for coding and testing.

## Getting Started

### Prerequisites

1. Install Python: [https://www.python.org/](https://www.python.org/)

2. Set up MetaTrader 5: [https://www.metatrader5.com/](https://www.metatrader5.com/)

3. Install Spyder: [https://www.spyder-ide.org/](https://www.spyder-ide.org/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nchinling/algorithmic_trading.git
    ```

2. Navigate to the project directory:

    ```bash
    cd "Algorithmic trading"
    ```

3. Explore individual folders for specific functionalities:

    ```bash
    cd broker_api
    # ...navigate through other folders as needed
    ```

## Usage

1. Review and customize the algorithmic trading strategies in the respective folders.

2. Execute the scripts using Spyder or any preferred Python IDE.

3. Monitor trading activities in MetaTrader 5.

## Acknowledgements

- The project makes use of finance data from Yahoo Finance.

- Special thanks to the MetaTrader 5 platform for enabling automated trading.


Feel free to use this corrected version in your README.md file. Let me know if you have any more questions or if there's anything else I can assist you with!
