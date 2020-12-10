# CAC Contest Submssion - 1984 Facial Tracker

Adv. Java with Android Studio S1

10/1/2020

This is a submission for the Congressional App Contest. The program is supposed to utilize the OpenCV library and detect if faces are present during
a school session. The program is supposed to help teachers recognize who is actually at their computer while they are teaching. The program constantly checks
for faces and sends the data towards a database, where the teacher can see. The database utilizes SQL and is hosted on pythonanywhere.com. The teacher can log in and generate a classroom code, which then can be shared
amongst the students. Students can then enter the code and send their facial data to the teacher.

I worked on this project with my friend Timothy Wilks. I wrote the groundwork for the facial detection part and completed the database side. Timothy Wilks
worked on the facial detection portion. We faced some issues, mostly with version control, and learning how to use the libraries given. In the end, it did not
work as the database accesses was not up to date everytime the teacher recieved data, instead showed a constant list of students. Also the opencv data did not
change what was sent towards the database. We did not find a way to use both libraries at the same time.
