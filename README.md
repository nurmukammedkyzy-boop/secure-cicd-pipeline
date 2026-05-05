# Secure CI/CD Pipeline Project

## Objective

This project demonstrates a complete secure CI/CD pipeline using GitHub Actions.

The pipeline includes:

- Build automation
- Automated testing
- Security scanning
- Artifact management
- Simulated deployment
- Logging and monitoring concepts

## Application Overview

The application is a simple Python Flask REST API.

It includes:

- Home endpoint
- Greeting endpoint with input validation
- Calculator endpoint
- Health check endpoint
- Secure information endpoint using environment variables
- Logging to a local log file

## Technology Stack

- Python
- Flask
- Pytest
- Flake8
- Bandit
- pip-audit
- GitHub Actions

## Pipeline Architecture Diagram

```text
Developer
   |
   v
Git Push / Pull Request
   |
   v
GitHub Actions CI/CD Pipeline
   |
   +--> Install Dependencies
   |
   +--> Lint Code
   |
   +--> Run Unit Tests
   |
   +--> Run SAST Security Scan
   |
   +--> Run Dependency Scan
   |
   +--> Generate Monitoring Output
   |
   +--> Package Application
   |
   +--> Upload Artifact
   |
   v
Deploy to Staging
   |
   v
Deploy to Production