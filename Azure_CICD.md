# CI/CD pipeline in Azure

## CI/CD Pipeline for Azure Web App with Docker

This guide explains how to set up a CI/CD pipeline in Azure for a web application that predicts outputs using a Docker image. We will use GitHub for version control, Azure Container Registry to store our Docker images, and Azure Web App to host our application.

### Overview of the Process
**Source Control:** Your project code is stored in a GitHub repository.
**Continuous Integration:** When you push changes to your GitHub repository, a CI pipeline automatically builds a Docker image of your application.
**Container Registry:** The built Docker image is pushed to Azure Container Registry, a private storage for your Docker images.
**Continuous Deployment:** Azure Web App pulls the Docker image from the Container Registry and deploys it, making your application available to users.

**Step-by-Step Guide**


**Step 1:** Set Up Your GitHub Repository
Ensure your project code, including the Dockerfile, is in a GitHub repository.
Make sure your code is working locally before pushing it to GitHub.


**Step 2:** Create Azure Container Registry


**Step 3:** Set Up Azure Web App


**Step 4:** Build and Push Docker Image Locally
Open your terminal and navigate to your project directory.
Build the Docker image using the following command:
- docker build -t testdockerkrish.azurecr.io/mltest:latest .
Log in to your Azure Container Registry:
- docker login testdockerkrish.azurecr.io
Push the Docker image to the Azure Container Registry:
- docker push testdockerkrish.azurecr.io/mltest:latest


**Step 5:** Configure GitHub Actions for CI/CD
In your GitHub repository, go to the "Actions" tab.
Click on "Set up a workflow yourself" or choose a template.
Create a new YAML file (e.g., ci-cd.yml) and add the following code:

-----------------------------------------------------------------------------------------------------------------------------------------------------
yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main  # Change this to your default branch

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Log in to Azure Container Registry
        uses: azure/docker-login@v1
        with:
          login-server: testdockerkrish.azurecr.io
          username: ${{ secrets.AZURE_USERNAME }}
          password: ${{ secrets.AZURE_PASSWORD }}

      - name: Build and push Docker image
        run: |
          docker build -t testdockerkrish.azurecr.io/mltest:latest .
          docker push testdockerkrish.azurecr.io/mltest:latest

      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v2
        with:
          app-name: <your-app-name>
          slot-name: 'production'
          images: 'testdockerkrish.azurecr.io/mltest:latest'
-------------------------------------------------------------------------------------------------------------------------------------

Replace <your-app-name> with your actual Azure Web App name.
Save the file. This will trigger the CI/CD pipeline every time you push changes to the main branch.


**Step 6:** Set Up Secrets in GitHub
Go to your GitHub repository settings.
Click on "Secrets" and then "Actions".
Add the following secrets:
AZURE_USERNAME: Your Azure Container Registry username.
AZURE_PASSWORD: Your Azure Container Registry password.


**Step 7:** Test Your CI/CD Pipeline
Make a change to your code and push it to the main branch.
Go to the "Actions" tab in your GitHub repository to see the pipeline running.
Once the pipeline completes, your application should be updated and running on Azure Web App.

**Step 8:** Access Your Application in Azure

**Find Your Web App URL:**

Go to the Azure Portal.
Click on "App Services" and select your web app.
Copy the URL shown (e.g., https://<your-app-name>.azurewebsites.net).

**Open Your Application:**

Paste the URL into a web browser and hit Enter.
This will take you to your app's home page.

**Use the App:**

Fill out any forms and submit to see predictions.

**Check Logs:**

If something goes wrong, check the logs in the Azure Portal under "Log stream" for real-time updates.

**Manage Your App:**

You can stop or restart your app from the Azure Portal.
