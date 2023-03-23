# TRANZACT-Tech-Interview

This project is designed to test the CountryLayer API and https://demo.evershop.io/ web site 
using Behave and Python. The project contains feature files and step files that define 
various scenarios for validating the API's functionality and web elements behavior .

## Project Structure
- features/: This folder contains the Gherkin feature files defining the test scenarios.
- features/steps/: This folder contains the Python step files implementing the step definitions for the test scenarios.
- main.py: This is the main entry point for running the test scenarios.
requirements.txt: This file lists the required Python packages for the project.
- api_key_example: You can find the field for the API key empty at the task2.feature file, corresponding for the API testing part.

To run this project, you need to have the following software installed on your system:

- Python 3.6 or later
- Git (optional, for cloning the repository)

## Installation
Follow these steps to set up the project on your local machine:

### Windows, macOS, and Linux

1. Clone the repository or download the project files:
> git clone https://github.com/yourusername/tranzact-technical-challenge.git
2. If you don't have Git installed, download the project files as a ZIP archive and extract them to a folder on your local machine.
3. Open a terminal (Command Prompt on Windows) and navigate to the project folder:
> cd tranzact-technical-challenge
4. Create a virtual environment:\
> python -m venv venv
5. Activate the virtual environment:
   - On Windows:
    > .\venv\Scripts\activate
   - On macOS and Linux:
    > source venv/bin/activate
6. Install the required packages:
> pip install -r requirements.txt

## Configuration
Before running the tests, you need to set up the API key for the CountryLayer API:

Replace the placeholder text <your_api_key> with your actual API key from the CountryLayer API.

## Running the Tests
To run the tests, execute the following command in the terminal:
> python main.py

The script will run all the scenarios defined in the feature files and display the results in the terminal.

## Troubleshooting
If you encounter any issues during the installation or test execution, ensure that you have installed the correct versions of Python and the required packages. Additionally, double-check your API key and endpoint URLs in the configuration files.

## License
This project is released under the MIT License. See the LICENSE file for more information.

## Contributing
To contribute to the project, please open an issue or submit a pull request on the project's GitHub repository.