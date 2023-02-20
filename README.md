# Patient-Data
Ability of a prescriber to work with patient data.
The main aim of this project is to build an application where the prescriber should be able to create a patient table, update the details of existing patient, delete existing patient, add new patient.
Requsites
      1. Since the problem description looks like a CRUD operation, we use sqlalchemy for database operations.
      2. We have to build an application, so we use http methods for client-server communication.
      3. To make the application easier we use flask framework.
      4. After building the application we may have trust issue with the quality of our application to test that we use 2 methods
          1. testing using postman
          2. Testing using python script
      5. Overall We us python as a coding language.
      6. By the end we will be building a rest api Using Flask without any external libraries.
      
Files
./settings.py – In this file all the required libraries are imported.
./main.py –  In this file the basic application  trigger is happening.
./patient.py – In this file the all the sql operations are done.  
./api.py – In this file the rest endpoints are created and each end points are mapped to their functions.
./testing.py – In this file the script for testing the created application is written

the basic flow of the application
![basic patient table](https://user-images.githubusercontent.com/43267530/220086958-22e69b17-4bef-486b-8c49-c54539e5b5de.png)
