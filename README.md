# AgriMarketWatch

**AgriMarketWatch** is a comprehensive project aimed at gathering, analyzing, and presenting data from various sources related to agriculture. This project integrates multiple layers, including a Python-based machine learning component, a Node.js/Express.js API backend, and a Vite-React frontend. The project is containerized using Docker, ensuring a consistent development and production environment.

## Project Purpose

The goal of AgriMarketWatch is to provide a centralized platform for monitoring and analyzing agricultural data, including:

- **Commodities Markets**: Tracking and analyzing trends in commodity prices.
- **Weather Data**: Gathering and processing data from various weather stations.
- **Climate Data**: Monitoring long-term climate changes affecting agriculture.
- **World Market and Supplies Data**: Analyzing global market trends and their impact on local agriculture.
- **Geopolitical Data**: Understanding the impact of global political changes on agriculture.

The project also aims to integrate with the **AgriBiz** project, which focuses on helping local farmers increase crop yields sustainably by providing insights based on soil analysis, fertilizer use, and cultivation information.

## Project Layers

### 1. **Frontend Layer (Vite-React)**

- **Purpose**: This layer provides a user-friendly interface for interacting with the data. It includes a dashboard for visualizing the data and a blog section for written analyses.
- **Tools**:
  - **React**: Used for building the UI components.
  - **Vite**: A build tool that serves as a faster alternative to Webpack.
- **Technologies**: TypeScript, Tailwind CSS, React Router, and more.

### 2. **Backend Layer (Node.js/Express.js)**

- **Purpose**: The backend API layer handles requests from the frontend and interacts with the database. It processes data from external APIs, such as weather data providers, and serves this data to the frontend.
- **Tools**:
  - **Node.js**: A JavaScript runtime for building the server-side application.
  - **Express.js**: A minimal and flexible Node.js web application framework.
  - **PostgreSQL**: The database used to store and query the collected data.

### 3. **Machine Learning & Data Processing Layer (Python)**

- **Purpose**: This layer handles all machine learning and data processing tasks, including predictive analysis on market trends and other agricultural data.
- **Tools**:
  - **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
  - **scikit-learn**: A library for machine learning in Python.
  - **Pandas**: A library providing data structures and data analysis tools for Python.

### 4. **Infrastructure Layer (Docker)**

- **Purpose**: Docker is used to containerize all components of the project, ensuring consistent environments across development, testing, and production.
- **Tools**:
  - **Docker Compose**: Manages multi-container Docker applications.
  - **Dockerfiles**: Each layer (React, Node, Python) has its own Dockerfile for containerization.

### 5. **CI/CD and Code Quality**

- **Husky**: Used for setting up Git hooks, such as enforcing commit message conventions with commitlint.
- **Linting**: ESLint for JavaScript/TypeScript, and Flake8 for Python are configured to maintain code quality.
- **Testing**: Jest for unit tests in the frontend, Pytest for Python, and Mocha/Chai for Node.js backend.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your system.
- **Node.js**: Required for running the backend and frontend locally without Docker.
- **Python 3.12**: Required for running the machine learning layer locally without Docker.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/agrimarketwatch.git
   cd agrimarketwatch
   ```

2. **Set Up Docker**:

   ```bash
   docker-compose up --build
   ```

3. **Running Locally Without Docker**:
   - **Frontend**:

     ```bash
     cd react
     yarn install
     yarn dev
     ```

   - **Backend**:

     ```bash
     cd node
     yarn install
     yarn dev
     ```

   - **Python ML Layer**:

     ```bash
     cd python
     source venv/bin/activate
     pip install -r requirements.txt
     uvicorn app.main:app --reload
     ```

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
