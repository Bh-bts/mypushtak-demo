# MYPUSTAK Automation

This Repository contains the Automation testcases for Pustak.

----

### Local Setup
- Python 3.11
- Clone this project repository to your local machine.
- Open a terminal and navigate to the project directory.

### Environment variables:

#### Windows
Run the below commands to set the Mypustak username and password
```
set MYPUSTAK_EMAIL=your_mypustak_email
set MYPUSTAK_PASSWORD=your_mypustak_password
```
### Macos/Linux
Run the below commands to set the Mypustak username and password
```
export MYPUSTAK_EMAIL=your_mypustak_email
export MYPUSTAK_PASSWORD=your_mypustak_password
```
## Run Mypustak Test Locally

### Installation
- Run this command in project folder: `pip install -r requirements.txt`

### Running Test
- This command run the test in normal mode `pytest`
- This command run the test in parallel mode `pytest -n 2`

### Capture Screenshots on Test Failures
Screenshots are automatically captured when a test fails and stored in the `screenshots` directory.

## Run Pustak Test using GitHub Actions

### Test Execution
Configure your GitHub repository to use GitHub Actions for automated test execution.

### Set GitHub Secrets
Ensure you add the necessary secrets (MYPUSTAK_EMAIL and MYPUSTAK_PASSWORD) in the GitHub repository settings under Secrets.

### Manually Trigger Tests on GitHub Actions
To manually trigger a test run using GitHub Actions:

1. Go to the Actions tab in your GitHub repository.
2. Select the workflow you want to run.
3. Click on the Run workflow button.
4. Fill in any required parameters(Browser name and Headless mode) if prompted.
5. Click the Run workflow button again to start the process.
