# Python Calculator 🐍

A simple command-line calculator written in Python.

This is my first Python project, created as part of my journey into programming, software development, and engineering.

The project is continuously improved to explore fundamental programming concepts, version control with Git, and collaborative development workflows using GitHub.

## Features

**Current version: v1.5**

### Arithmetic Operations

- Addition (`+` or `plus`)
- Subtraction (`-` or `minus`)
- Multiplication (`*` or `mal`)
- Division (`/` or `dividiert`)
- Exponentiation (`**` or `hoch`)

### Mathematical Constants

- Pi (`pi` or `p`)
- Euler's number (`euler` or `e`)
- Constants can be used as either the first or second number
- Mathematical constants are provided by Python's built-in `math` module

### Input Handling

- Support for integers and decimal numbers
- Case-insensitive commands using `.lower()`
- Automatic removal of surrounding whitespace using `.strip()`
- Input validation using `try` and `except`
- Automatic retry after invalid numeric input
- Division-by-zero protection for standard division
- Detection of unsupported arithmetic operators
- Separate input loops for numbers and arithmetic operations

### User Interface

- Welcome screen displaying the program version and available commands
- Interactive help using `a` or `anleitung`
- Exit functionality using `s` at any input stage
- Automatic return to the current input prompt after displaying help
- Continuous calculations using a main program loop
- Goodbye message when exiting the calculator

### Modular Program Structure

Version 1.5 introduces four reusable functions:

- `begruessung()` – Displays the welcome screen
- `anleitung()` – Displays available commands and instructions
- `eingabe()` – Handles numeric input, mathematical constants, validation and special commands
- `berechnen()` – Handles arithmetic operations, help requests and calculation output

The main program now coordinates these functions instead of handling all operations directly.

## Getting Started

### Requirements

- Python 3
- No external libraries required

### Installation and Usage

1. Clone or download this repository.
2. Open `calculator.py` in a Python IDE such as Thonny.
3. Run the program.
4. Enter two numbers or mathematical constants.
5. Select an arithmetic operation.
6. The calculator displays the result and starts a new calculation.
7. Enter `a` for help or `s` to exit.

**Notes:**

- Decimal numbers must use a period (`3.14` instead of `3,14`).
- Commands are case-insensitive.
- Surrounding spaces are ignored.
- Help can be accessed during both number and operator input.
- Results are currently displayed directly and are not stored for subsequent calculations.

## Development Roadmap

- [x] **v1.0** – Basic calculator with four arithmetic operations
- [x] **v1.1** – Support for decimal numbers
- [x] **v1.2** – Input validation and error handling
- [x] **v1.3** – Exit functionality and improved user interface
- [x] **v1.4** – Mathematical constants, exponentiation and flexible commands
- [x] **v1.5** – Code refactoring, reusable functions and interactive help
- [ ] **v1.6** – Previous-result memory and chained calculations
- [ ] **v2.0** – Advanced mathematical operations

## Changelog

### v1.5 – Code Refactoring & Interactive Help

- Refactored the calculator into four reusable functions
- Introduced function parameters and return values
- Centralized numeric input handling
- Added dedicated input validation loops
- Improved error recovery without restarting the entire calculation
- Added interactive help using `a` and `anleitung`
- Added whitespace normalization using `.strip()`
- Reduced duplicated code
- Simplified the main program loop
- Improved code organization and maintainability

### v1.4 – Mathematical Expansion

- Added mathematical constants pi and Euler's number
- Introduced exponentiation using `**` and `hoch`
- Added alternative text commands for arithmetic operations
- Implemented case-insensitive commands using `.lower()`
- Updated the welcome screen with additional commands

### v1.3 – Exit Functionality

- Added an exit option at all three input stages
- Added a welcome screen
- Added a goodbye message
- Improved user interaction

### v1.2 – Input Validation

- Added exception handling using `try` and `except`
- Prevented crashes caused by invalid numeric inputs
- Added automatic retry after invalid input
- Preserved existing calculator functionality

### v1.1 – Decimal Number Support

- Replaced integer input conversion with floating-point conversion
- Added support for calculations involving decimal numbers
- Preserved existing arithmetic operations and division-by-zero protection

### v1.0 – Initial Version

- Implemented four basic arithmetic operations
- Added a continuous calculation loop
- Added protection against division by zero
- Added handling for unsupported operators

## Development Workflow

This project uses Git and GitHub for version control.

New features are developed in separate feature branches, tested and integrated into the main branch through pull requests.

Stable development milestones are marked using Git tags.

## Project Purpose

The primary goal of this repository is to document my progress in learning Python and software development.

Future improvements will focus on writing more reliable, maintainable, testable and structured code.

**Status:** Active learning project.
