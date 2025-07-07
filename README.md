# ThinkOn Mini Project – Web App Deployment Stack

This repository demonstrates a complete deployment stack using **HAProxy**, **Flask (Python)**, and **MySQL**, with secure base image automation.

The solution meets the following requirements:

-  A secure **base image**, updated weekly to address vulnerabilities
-  A **database server** (MySQL 8)
-  A sample **database** with initialization
-  A small web array of **3 Flask nodes**
-  A front-end **HAProxy load balancer**
-  Infrastructure-as-code for CI/CD using Docker and GitHub Actions


## Components

| Component     | Description                              |
|---------------|------------------------------------------|
| `secure-base` | Custom Docker image based on Ubuntu 20.04 with security patches and Python preinstalled |
| `db`          | MySQL 8 with a sample `thinkon` database |
| `web1/2/3`    | Flask applications served on port 5000   |
| `haproxy`     | Load balancer for routing web traffic    |


## Testing via GitHub Actions
Two workflows are defined:

Rebuild Secure Base Image
.github/workflows/patch-rebuild-secure-base.yml

Runs weekly (Monday, 2AM UTC)

Builds and pushes ghcr.io/swalia-proj/secure-base:latest

Test Full App Stack
.github/workflows/test-app-stack.yml

Spins up HAProxy, Flask, and MySQL services

Runs smoke tests to validate:

HAProxy responds (curl)

MySQL health is green


## Secure Base Image Build
The secure-base image is:

Based on ubuntu:20.04

Auto-patched weekly via GitHub Actions

Preinstalled with python3 and pip3

Pushed to GitHub Container Registry (GHCR)


Author
Sonia Walia
Email: soniawalia.sw@gmail.com
