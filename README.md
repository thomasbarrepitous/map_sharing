# GeoPoints Sharing App


- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [License](#license)

## Overview

This project is a geographic points sharing application built using Python, Django Rest Framework (DRF), and Dash. The application allows users to save and organize locations, create collections of points, and share them with others. The primary focus of the project is to showcase proficiency in REST APIs, JWT authentication, caching, and other relevant skills.



## Features

- **User Authentication**: Secure user authentication using JWT tokens.

- **Geographic Points**: Save and manage geographic points with details such as name, coordinates, and description.

- **Collections**: Create collections of points for better organization.

- **Sharing**: Share collections of points with other users.

- **RESTful API**: Utilize Django Rest Framework to build a robust and scalable API.

- **JWT Authentication**: Implement JSON Web Token (JWT) authentication for secure user access.

- **Caching**: Optimize performance using caching mechanisms for frequently accessed data.

## Requirements

Make sure you have the following tools and credentials installed/configured before running the application:

- **Docker**: Install Docker from [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).

- **Docker Compose**: Install Docker Compose from [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).

- **Google Maps API Key**: Create a Google Maps API key on Google Cloud Platform (GCP) following the instructions below.

## Google Maps API Key

To use Google Maps services, you'll need to create an API key on GCP:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new project or select an existing one.

3. Navigate to the "APIs & Services" > "Credentials" page.

4. Click on "Create Credentials" and choose "API key".

5. Copy the generated API key.

6. In the project root, create a `.env` file and add your API key:

    ```dotenv
    GCP_KEY=your_gcp_key
    ```

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/thomasbarrepitous/map_sharing.git
    cd map_sharing
    ```

2. Create (or add to) an `.env` file in the project root and configure environment variables. Example:

    ```dotenv
    export GCP_KEY=your_gcp_key
    export AUTH_API_URL="http://api:8000/api/account/"
    export PLAYLIST_API_URL="http://api:8000/api/playlists/"
    export DJANGO_SECRET_KEY=your_django_secret_key
    export DEBUG="True"
    ```

3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Access the DRF backend at [http://localhost:8000](http://localhost:8000) and the Dash frontend at [http://localhost:8050](http://localhost:8050).


## Usage

1. Access the application at [http://localhost:8000](http://localhost:8000).

2. Create an account or log in if you already have one.

3. Explore the features to save and manage geographic points and collections.

4. Share your collections with other users.

## API Documentation

The API documentation is available at [http://localhost:8000/api/docs/](http://localhost:8000/api/swagger/). Explore the endpoints and test the API functionality.


## License

This project is licensed under the [MIT License](LICENSE).


---
