# Synthetic Health Data Generator

## Overview

The project is organized in different folders:
* _jupiter_ : It contains different Jupiter notebooks. Please refer to every single one for details.
* _web-ui_: It contains the application used to generate and evaluate synthetic data.

### Web-ui
* The application should be launched by [Docker](https://www.docker.com/). Here below some steps to run a Docker image:
  * Inside the root of the project directory run these commands:
    1) `docker build -t streamlit .`
    2) `docker run -p 8501:8501 streamlit`
  * After running the docker commands depicted abow, the application should be browsed at this address: `http://0.0.0.0:8501 `


* For developers, here below the main libraries used to develop the application:
  * [Streamlit](https://streamlit.io/) used for ui development
  * [SDV](https://sdv.dev/) used for synthetic data generation
  <br> (For details please refer to the documentation libraries)
