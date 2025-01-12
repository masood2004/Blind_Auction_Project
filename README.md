# Blind Auction Project

This repository contains a Python-based implementation of a **Blind Auction** system, where participants place confidential bids, and the highest bidder wins. The program ensures privacy by keeping bids hidden until all participants have submitted their offers.

## Features

- **Confidential Bidding**: Keeps all bids private until the auction ends.
- **Automated Winner Selection**: Determines the highest bidder automatically.
- **Interactive Interface**: Provides an easy-to-follow command-line interface.
- **Replay Option**: Allows users to conduct multiple rounds of auctions without restarting the program.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/masood2004/Blind_Auction_Project.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Blind_Auction_Project
   ```

3. **Ensure Python is installed**:

   - This project requires Python 3.x. You can download it from the [official Python website](https://www.python.org/downloads/).

## Usage

1. **Run the program**:
   ```bash
   python main.py
   ```

2. **Follow the prompts**:
   - Enter the names and bids of all participants as prompted.
   - The program will keep the bids confidential until all are submitted.

3. **View the Winner**:
   - Once all bids are collected, the program will display the highest bid and the corresponding bidder.

4. **Restart or Exit**:
   - After each auction, you can choose to start a new auction or exit the program.

## Example

Here’s an example interaction:

```
Welcome to the Blind Auction!
Enter your name: Alice
Enter your bid: 100
Is there another bidder? (yes/no): yes
Enter your name: Bob
Enter your bid: 150
Is there another bidder? (yes/no): no
The winner is Bob with a bid of $150.
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/masood2004/Blind_Auction_Project/blob/main/LICENSE) file for details.

## Acknowledgments

This project serves as an educational exercise for learning Python, particularly focusing on implementing loops, dictionaries, and user interaction.

Get ready to experience the thrill of a blind auction! 🎉💰
