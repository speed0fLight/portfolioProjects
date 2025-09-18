
# Note Buddy
#### Video Demo:  [Click Here!](https://youtu.be/sNIeox97S0U)
#### Description: A video showcasing a website for note taking at an easy simplified level.
Author: Justin N

## Hello, everyone!

This project was created over the course of 2 months, using all sorts of frameworks and skills ive learned from my time at cs50.
There were many challenges, learning bootstrap, learning flask, learning JS, each of which are remarkable in a website!

For choice, I opted for a note-taking website as it's a project that displays a great way to use SQL, Python, and JS!

## How to use the website

First, login. After doing so, you can go to the "notes" tab and start writing notes down. Alternatively, you can vist the "help" section; visible after you login.

## Breakdown:

This project uses flask, a website framework that loads html files as "templates", which accelerates the process of building a website.
How does it make development faster? You can reuse similar content such as a navigation bar at the top, or have your company logo on the left at all times.
This can be done using a layout, which is a exoskelton of your website with the correct places for your content to be inserted!

## Each core functionality

Loading notes uses the "fetch" function from JavaScript, which queries the database for a user's notes. This is where the majority of JavaScript was used!

Why use Java script? Why not load the page with everything by default?
The process of note management includes note creation, deletion, and editing. These features would not be practical to implement serversided only, instead the client
handles such actions, allowing for more seamless interaction with their data, without having to load excessive pages for actions, etc.

Loading HTML pages themselves heavily involves the use of Flask, which can load content into other pre-made templates to quickly make pages for websites instead of
having to create each html boilerplate from scratch, such as the footers, headers, etc. Only the content is inserted, nothing else!

Databases: The database system used is SQL, it was used because it's implementation was simple and practical in this situation, and it's compatability with
the projects interests also led me to use it as a tool within this project.

## My challenges, and learning experience from this.

I have learned a framework (Bootstrap HTML) which allowed me to compress and style webpages faster, and I have also solidified my knowledge of SQL, and Flask.
Bootstrap was vital as it allowed much better formatting and decoration for webpages which also appeals to users in the case of this being a note-taking app.
Bootstrap, Flask, Python, and SQL are a perfect combination for tackling projects such as this one.

The most important thing I learned is how to build a website from scratch, which can help me and others in future projects and other use cases.

## Deeper analysis of each tool used

The database is accessed from the server side, there are two types of tables, the users table (username, password) AND the user_notes table (user_id, note, etc)
How a query begins: First the save note function is called from the html page using javascript. This sends out a POST request, sending the new entry, the note's name
and the note's new name if that is changed as well. All three of the save, delete, and load note functions query the server which then acts on that information.

## Security

All notes cannot be accessed unless the user's session is valid and their user id belongs to the note they are accessing. The passwords are encrypted along with a
hashing system to ensure leaks cannot prove themselves harmful. Nevertheless, security is a minor concern in a simplistic application such as this.

## Ending

This project was a great conclusion to my learning career at cs50, from the python to C libraries to the entire system of webpages, this course is amazing for students who
want to get into programming, and overall I would say it's needed if anyone wants to learn about general programs.

Also, I have lots of things to say about the courses--They share a wonderful balance between difficulty and learning experience. Each week gives you easy and hard assignments depending
on your capability to do certain things, such as algorithms or programs that are complex than most.

## What's next?

After completing the final project, the course itself concludes, and the skills here are always transferrable anywhere that's needed.
Personal thanks to this course and those who have taught in it.
- Justin
