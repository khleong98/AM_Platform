Welcome to AM Platform!

This README provides an overview of the components, setup instructions, and how to launch the web app.

============================== Components ==============================

1. User Referral
   URL         : localhost:8080/referral
   Description : Allows users to check the referral tree of any user by email.

2. User Detail
   URL         : localhost:8080/detail
   Description : Enables users to retrieve information about any user by email.

3. User Detail API
   URL         : localhost:5000/api/detail
   Description : Provides similar functionalities as User Detail, but accessible via API.

=========================== Environment Setup ===========================

Before launching the web app, ensure to set up the environment using Conda. Follow these steps:

1. Navigate to the root directory of the project.

2. Run the following Conda command to create the environment:
   conda env create -f environment.yml

========================= Launching the Web App =========================

Flask with Conda:

1. Navigate to the backend directory:
   cd backend

2. Activate the Conda environment:
   conda activate am_platform

3. Run the Flask app:
   python app.py

Vue with npm:

1. Navigate to the frontend directory:
   cd frontend

2. Run the Vue development server:
   npm run serve