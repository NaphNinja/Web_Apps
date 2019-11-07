# BaverIQ Chat Application

This is a test chat application developed to demonstrate functionality including real time chat and file transfer using an intuitive UI. Please follow the instructions below to install and run the chat yourself. To broadcast, simply share the chat with other users and have them do the same. To test locally, open the application in multiple windows and login as a new user.

### Installation

You need node.js,npm and bower installed globally as a pre-requisite. Once these have been installed, run the following commands after entering your app directory:

-> $ sudo npm install

-> cd <your_app_directory/public/> and run $ bower install

-> Before performing the upcoming step, take a note of your local machine's IP address by opening a new terminal and typing $ ifconfig

-> cd into <your_app_directory/public/app/js/> and edit "app.js" and set $rootScope.baseUrl to <http://your_ip_address:7474>. Once that's done set socketProvider.setConnectionUrl('http://your_ip_address:7474')

-> Once the above step is completed, cd back into the root folder and run the application by typing: $ node app.js

-> View the application in the browser by navigating to <http://your_ip_address:7474>

> File shared among users will be stored in /public/app/upload and in the respective doc, music and image directory.
> The files in upload directory are stored with some expiry time (8 hours) and the files will be deleted after expiry time.
> The routine_cleanup function deletes files after every one hour.

### Version
0.0.1

### Tech

BaverIQ Messenger Test Application uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps
* [Bootstrap] - great UI boilerplate for modern web apps
* [AdminLTE] - great UI based on bootstrap
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework
* [jQuery] - javascript library
* [lightbox] - javascript plugin for image pop-ups 


License
----

MIT

### Contact
- Naphish Lashba Raj (naphish@baveriq.com)
