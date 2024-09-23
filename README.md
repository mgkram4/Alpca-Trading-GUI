# Alpaca Trading GUI

## Overview
This project is a web-based graphical user interface for interacting with the Alpaca trading platform. It provides real-time market data, account information, and order management capabilities using the Alpaca API.

## Features
- Real-time stock and cryptocurrency price updates
- Account information display (buying power, cash balance, portfolio value)
- Order management (submit and cancel orders)
- Position tracking
- User-friendly web interface

## Technologies Used
- Python
- Flask (Web Framework)
- Alpaca API (Trading Platform)
- HTML/CSS/JavaScript (Frontend)

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/mgkram4/Alpca-Trading-GUI.git
   cd Alpca-Trading-GUI
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Alpaca API keys:
   - Create a `.env` file in the project root
   - Add your Alpaca API key and secret:
     ```
     ALPACA_API_KEY=your_api_key_here
     ALPACA_SECRET_KEY=your_secret_key_here
     ```

## Usage
1. Run the Flask application:
   ```
   python gui.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Use the interface to view market data, submit orders, and manage your Alpaca trading account.

## Contributing
Contributions to improve the Alpaca Trading GUI are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## Disclaimer
This project is for educational purposes only. Always understand the risks involved with algorithmic trading and use this tool responsibly. The creators of this project are not responsible for any financial losses incurred through its use.

## License
[MIT License](LICENSE)

## Contact
For any queries or support, please open an issue in the GitHub repository.
