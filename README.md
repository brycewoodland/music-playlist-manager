## Overview

**Project Title**: Music Playlist Manager

**Project Description**: A RESTful API which uses Firestore, Python, and Flask. It utilizes CRUD operations to manage playlists.

**Project Goals**: 
1. Create a database
2. Use CRUD operations to manage data
3. Implement Swagger Doc

## Instructions for Build and Use

Steps to build and/or run the software:

1. **Create a Firebase Account and Set Up Firestore**:
   - Go to the [Firebase Console](https://console.firebase.google.com/).
   - Create a new project or select an existing project.
   - In the project dashboard, click on "Firestore Database" and create a Firestore database.
   - Go to "Project Settings" and navigate to the "Service accounts" tab.
   - Click on "Generate new private key" to download the service account key file. Save it as `service-account-file.json` in the project root directory.

2. **Ensure Python is Installed**:
   - Make sure you have Python 3.8+ installed. You can download it from the [official Python website](https://www.python.org/downloads/).

3. **Project Dependencies**:
   ```python
     pip install firebase-admin

     pip install Flask
   
     pip install flasgger
   ``` 
     

Instructions for using the software:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/music-playlist-manager.git
   cd music-playlist-manager
2. **To Run**:
```Python
  python server.py
  ```

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Firestore
* Python
* Packages: firestore-admin, flask, & flasgger

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Firebase](https://firebase.google.com/docs/firestore)
* [What are Cloud Databases?](https://www.youtube.com/watch?v=RUa0GTgYrXc)
* [#3 @reach/router & Firestore — Let's build a Firebase & React app](https://www.youtube.com/watch?v=gWC8zjc8wPs)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Adding a user with authorization, this way when a user signs in they can access their playlists.
* [ ] I also want to implement authorization so that users can only add songs to playlists and can't create, update, or delete song info.
* [ ] Implement a frontend.
