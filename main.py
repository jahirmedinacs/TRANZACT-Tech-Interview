import os
import subprocess


def main():
    print("Running tests and generating Allure reports...")
    subprocess.run(["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "reports/", "features/"])

    print("Opening Allure report...")
    subprocess.run(["allure", "serve", "reports/"])


if __name__ == "__main__":
    main()
