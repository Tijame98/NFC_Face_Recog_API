# Automatisation du Relevé de Présence des Étudiants

## Data Base

This folder contains SQL scripts and Python code to set up and manage the PostgreSQL database on your Raspberry Pi. The database stores student details, course information, and attendance records, etc...

create_tables.py: Python script to create the necessary tables in the database.
Insert_into_DB.py: Python scripts to insert and manage data within the database. It includes functions to connect to the database, insert new records, and query attendance data.

## Face Recognition

This directory includes scripts for setting up and running facial recognition to verify the identity of students during the attendance process.

featuredetector.py: Python script that integrates facial recognition technology using OpenCV with the latest feature called BFMatcher() . It compares the captured images against stored student images to verify identities and features compatibility.

## Flask API

Here, you'll find the Flask application that serves as the backend and frontend of the web interface for attendance tracking.

app.py: The main Flask application file. It initializes the app and ties together the API routes.
templates/: Contains HTML files that serve as templates for the web interface, which display attendance records and allow administrative actions.
static/: Holds CSS files and dependencies files for styling and interactive functionality on the web frontend.

## RC522

Scripts related to the operation of the RC522 NFC reader are stored here. They handle the reading of NFC tags and the initial authentication of student IDs.

det_ID.py: This script is responsible for interfacing with the RC522 NFC reader, capturing the UID of NFC cards presented by students.
extract_ID.py: checking captured UID of NFC cards against the database.

## Cloud Data Base hosted on Render

Hostname : dpg-cocsnu63e1ms739lgb80-a

Port : 5432

Database : nfc_r0a3

Username : raspi

Password : mkIWGPH0eGtRMApDnwV5Pu1frBGfgq1U

Internal Database URL : postgres://raspi:mkIWGPH0eGtRMApDnwV5Pu1frBGfgq1U@dpg-cocsnu63e1ms739lgb80-a/nfc_r0a3

External Database URL : postgres://raspi:mkIWGPH0eGtRMApDnwV5Pu1frBGfgq1U@dpg-cocsnu63e1ms739lgb80-a.frankfurt-postgres.render.com/nfc_r0a3

PSQL Command : PGPASSWORD=mkIWGPH0eGtRMApDnwV5Pu1frBGfgq1U psql -h dpg-cocsnu63e1ms739lgb80-a.frankfurt-postgres.render.com -U raspi nfc_r0a3
