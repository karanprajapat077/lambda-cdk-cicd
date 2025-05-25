# Hourglass Code Challenge

This project is designed to solve the Hourglass problem as presented in the HackerRank coding challenge. The goal is to find the maximum hourglass sum in a 2D array.

## Overview

An hourglass in a 2D array is defined as a subset of values with indices falling in this pattern:

```
a b c
  d
e f g
```

For example, given the following 2D array:

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 1 2 4 0
```

The hourglass sums would be calculated as follows:

```
1 1 1
  1
1 1 1
```

The maximum hourglass sum in this case is 7.

## Installation

To run this project, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hourglass-code-challenge
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To execute the hourglass function, you can run the following command in your terminal:

```
python src/hourglass.py
```

## Running Tests

To ensure that the implementation works as expected, you can run the test cases provided in the `tests` directory. Make sure you have the testing framework installed, then run:

```
pytest tests/test_hourglass.py
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.