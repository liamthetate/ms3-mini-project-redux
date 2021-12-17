![title](static/images/rm-logo.png)

Live site: http://flask-task-manager-experiment.herokuapp.com/start

<br/>
<br/>

# ABOUT

A (somewhat) gamified CRUD experience. I would recommend 'playing' it before reading any further, as the information contained in this document might deflect from the first-time experience...

<br/>
<br/>

# PRODUCT SHOT
![product](static/images/rm-product-shot.png)
<br/>
<br/>

# UX

## User Stories

First Time Visitor Goals

>I want to play a game.

>I want to understand what my task is.

>I want to navigate the app/site, effortlessly.

<br/>

Returning Visitor Goals

>I want to show a friend this dull but disturbing thing I found.

>I want to see what happens when I 'save' the bees.

>I want a quick way to get in contact with the creator.


<br/>

Frequent User Goals

> I enjoy creating ficitional bees and adding them to lists.

<br/>
<br/>

## Design

Colour Scheme
* White predominates (Apple/Tech vibes) with Yellow and Black used on buttons and the main menu. As ever Red is used to call attention to important information.
<br/>

Typography
* The main font is 'IBM Plex Serif' with Serif as the fallback.
<br/>

Wireframes
* [Title Screen](static/images/rm-wf1.png)
* [Story](static/images/rm-wf2.png)
* [Signup](static/images/rm-wf3.png)
* [Create](static/images/rm-wf4.png)
* [Read](static/images/rm-wf5a.png)
* [Update](static/images/rm-wf5b.png)
* [Delete](static/images/rm-wf5c.png)
* [Congrats](static/images/rm-wf6.png)
* [IBM](static/images/rm-wf7.png) 
* [Game Over](static/images/rm-wf8.png) 
<br/>
<br/>

# LIBRARIES, FRAMEWORKS & PROGRAMS USED

1. Materialize:
    * Materialize was used throughout for layout, buttons etc.
  <br/>
2. Google Fonts:
    * Google fonts was used for 'IBM Plex Serif'.
    <br/>
3. Font Awesome:
    * Font Awesome was for the top icon and the social media link.
    <br/>
4. Gitpod
    * Gitpod was used for all code creation and pushing to GitHub.
    <br/>
5. GitHub:
    * GitHub was used to store the projects code after being pushed from Gitpod.
    <br/>
6. Photoshop:
    * Photoshop was used to create a fake 'handwritten' picture of a bee's data.
    <br/>
7. Balsamiq:
    * Balsamiq was used to create the wireframes during the design process.
<br/>
8. Full Page JS:
    * The javascript library Full Page JS was used for the start and end pages.
    <br/>
9. [Web Formater](https://webformatter.com/):
    * To format my html, css code and Javascript.
<br/>
10. Heroku:
    * For hosting the app/site, synced to GitHub.
<br/>
11. MongoDB:
    * For database hosting and backend CRUD functionalitity.
<br/>
12. Jinja:
    * Template engine 
<br/>
13. Flask:
    * Framework used to write the web application.
<br/>
14. Python:
    * For all the game logic and CRUD operations.
<br/>
<br/>

# FEATURES 

## Landing page

![landing page](static/images/rm-landing-page.png)
<br/>
A visual pun. Simple and straightfoward design with a genocidial cleanliness.

## Top HUD

![top hud](src/images/top-hud.png)
<br/>
The 1600 is a reference to real targets that 'cleaners' have for iPhones. 
A better display would have been Hour / Minutes / Seconds but I couldn't figure it out!

## Player HUD

![player hud](src/images/player-hud.png)
<br/>
Oversized and overbearing, permenatly displayed above your head, a signifier of your value lol.

## Spray

![player hud](src/images/spray.png)
<br/>
A toxic chemical that makes the phones nice and shiny.

## Fail!

![player hud](src/images/fail.png)
<br/>
If you don't do your one job properly, the machine will shake!

## Chat!

![player hud](src/images/worker-chat.png)
<br/>
The only thing worth doing XD
<br/>
<br/>

# Testing User Stories from User Experience (UX) Section

## First Time Visitor Goals:

>I want to play a game.

Well, it's not going to be fun.

<br/>

>I want to understand what my task is.

The opening story, menu instructions and flashing red icons should communicate what needs doing.

<br/>

>I want to navigate the app/site, effortlessly.

As a one-shot experience there is a flow to the UX and simple UI

<br/>

## Returning Visitor Goals:

>I want to show a friend this dull but disturbing thing I found.

Your exisiting username probably doesn't exist anymore!

<br/>

>I want to see what happens when I 'save' the bees.

Nothing new on-screen, but you're a good person. 

<br/>

>I want a quick way to get in contact with the creator.

It's right at the bottom of the start page.

<br/>

## Frequent User Goals:

> I enjoy creating ficitional bees and adding them to lists.

I like your style.
<br/>
<br/>

# FUTURE EXPANSION

There are numerous ways to improve this experience, from small to large.

SMALL: 

* Only display list information that pertains to the current task i.e. if the UI says find the diseased, the list below only lists disease and not honey productivity. At the moment it's more intuitive to 'skip ahead' and start reporting bees that aren't yet a focus of attention.

LARGE:

* More involved tasks! For example: Finding the Admin or Head of BR (Bee Resources) log-in details on the list, then logging-in as them and reporting them as diseased / poor productivity, lol!

<br/>
<br/>



# TESTING

## Devices & Browsers

The site was tested on the following devices:

Device | OS | Browser
-------|----|---------
iPhone 8 | iOS 14 | Safari, Ghostery, Firefox 
Macbook Pro | Big Sur | Safari, Firefox, Chrome, Brave
<br/>

iPhone 8 couldn't fit the whole game on the screen and was missing vital controls. But it's a desktop experience so...

The fixed width nature of the game means that testing in browsers has been relatively straight forward, the main issue for desktop was keeping the game centered on the page. This was achieved with this css magic formula:

    display: flex;
    justify-content: center;
    align-items: center;

KaboomJS has worked flawlessly across all the browsers I tested it on however the AudioContent issue addressed in 'Known Bugs' remains a problem to solve.


## Validator testing

HTML: A few errors detected on the W3C validator but I'm outta time! :/

CSS: No errors were found when passing through the Jigsaw W3C validator.

JS: KaboomJS trips 'Jshint' up on almost every line so difficult to know :/
<br/>
<br/>

## Lighthouse results

Desktop [View](src/images/lighthouse.png)
<br/>
<br/>

## Known bugs

1. Safari is a big one. Because of the AudioContent API, no sound will play at all! Chrome won't play the title music for the same reason but does work after that.
<br/>
<br/>

# DEPLOYMENT

To get this code to work on your machine I used this dev template:

* [Phaser 3 Template](https://github.com/ourcade/phaser3-parcel-template.git)

Then in Visual Studio Code, open a zsh terminal and type:

    npm install kaboom

    npm run start // RUN YOUR OWN SERVER

    npm run build // TO MAKE A VERSION FOR THE WEB (Production files will be placed in the dist folder. Then upload those files to a web server.)

I have deployed the game to my own ftp/website [here](http://liamtate.co.uk/efws/index.html) using Filezilla to transfer files. I am happy to supply a username & password so you can check the time and date stamp. (I'm hesitant to deploy it to github pages because I'd have to restructure my development folders then push to this repository and I'm concerned it'll break something this close to the deadline. All the deployed files can be found in the /dist folder).

However, if I was going to deploy to GitHub pages this is how I would do it:

* GitHub repository > 'Settings' tab > 'Pages' menu
* Source drop-down menu > Select Master Branch > Click Save
<br/>

To clone a repository via HTTPS you could just read [this handy guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository), or following along below:

* Dropdown menu 'Code' > Choose either HTTPS, SSH or CLI
* Click clipboard icon
* Open Terminal > Type: 

        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

* Press Enter:

        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
        > Cloning into `Spoon-Knife`...
        > remote: Counting objects: 10, done.
        > remote: Compressing objects: 100% (8/8), done.
        > remove: Total 10 (delta 1), reused 10 (delta 1)
        > Unpacking objects: 100% (10/10), done.

<br/>

To clone a repository to GitHub Desktop:

* Dropdown menu 'Code' > Open with GitHub Desktop
* Follow the prompts!
<br/>
<br/>

# CREDITS

## Code: 

The 'game' owes an obvious debt to the Task Manager mini-project and further code used is detailed below.

<br />



# SPOILERS

If you Edit > Select All on the webpage you'll find a message.
On the webpage Right-click > 'Inspect / Inspect Element' > Console. You will find a further message.
Got it yet? Hit the + and - keys for fun times!

The idea, at least for me, is to free the workers by breaking or crashing the actual game by overwhelming the machine(s) #Luddite :D
