# Django-with-celery

In this project, I use celery for carrying out an intensive task while the users can normally use the application as they would.
This app takes an integer from the user and makes that many number of random users in the database in the background without having the user to stop and wait while the request task is completed.

## Demo app

This app uses celery to make a random number of users (between 50 and 500) and stores them in the database. The task is process intensive and time consuming so it's carried out in the background with the help of celery.

## Email_example app

This app is used to send emails in the background after waiting for 10 seconds. Since it's an intensive task and would take users' time, so it's carried out in background while the user continues using website.
