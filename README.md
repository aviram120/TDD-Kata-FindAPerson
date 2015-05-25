## TDD Kata - FindAPerson
A repository for HW4 of the JCE [Software Engineering Course](https://github.com/jce-il/se-class/wiki/Schedule)

### Intro
In this homework we are exercising [Test Driven Development](http://en.wikipedia.org/wiki/Test-driven_development).
In this software development method code is written through the following cycle: Test (Red) -> Code (Green) -> Refactor. See lecture slides for more details and resources.
We will also use git to document the process.

You can either follow the given problem or ask the course team for another problem, e.g., from the Kata page in the lecture slides.

### Background Story
This excecise was prepared in Honor of [Or A.][ref-or] R.I.P who died during the [2015 Nepal earthquake](http://en.wikipedia.org/wiki/April_2015_Nepal_earthquake).

Let's take a look at [Ushahidi](http://www.ushahidi.com/), which is a platform, services and tools for geographical crowd sourcing, e.g., for coordinating rescue eefforts following a natural crisis ([Nepal](http://www.ushahidi.com/2015/04/29/status-update-regarding-ushahidi-deployments-for-nepal/)).   The [Crowdmap - Basic Features](https://wiki.ushahidi.com/display/WIKI/Crowdmap+-+Basic+Features),  are:

* Create a post
* Create a Map
* Find Posts
* Find a Map
* Collaborate
* **Find a Person**: This feature will be added at a later date. Stay Tuned
* See all the latest Posts
* See all the latest photos
* Map view
* View a post by Location

![](https://wiki.ushahidi.com/download/attachments/8356261/View%20a%20post%20from%20a%20location.png?version=1&modificationDate=1367443180000&api=v2&effects=border-simple,blur-border,tape)

Since they state that there is a missing feature, we are going to "implement" it! For a start we do not assume dependecies on exising code rather we will discover and implement only the necessary dependecies.

### The Actual Problem, Add a Feature: Find a Person!
* Given a person name, return all posts (of a map) containing it’s name (in any of a post fields), example:
   - Input: "Or A."
   - Output: ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"]
* Given a name, check if the map includes a location information (place or geo. location), example:
   - Input: "Or A."
   - Output: True
* Check if there are map inconsistencies, e.g., the same name with different locations. Example:
   - Input: nepal map (with content as above)
   - Output: True (since the name appear in more than one location)

### Work Instructions
1. To start, [**fork** the exercise repository][forking] (For later updates: first add a [remote][config-remote] to the upstream repo and [sync][sync-remote] with a [pull][ref-pull]:  ```git pull upstream master```).
1. [**Clone**][ref-clone] the repository to your workstation.
1. Make sure you have a test runner setup working, e.g. by running: ```python test_find_person.py```
1. Modify/add files (in the repository directory) to complete your solution.
    * Each TDD phase needs to be [**commit**ted][ref-commit] separately with a suitable message that tell the TDD stage and achivement, e.g. “RED: Test for finding a name”.
    * You can also do it with pair programming, but you must switch roles between RED and GREEN, including commit author (see [here]( http://c2.com/cgi/wiki?PairProgrammingPingPongPattern), there is also a fun [Eclipse game]( http://www.happyprog.com/pairhero/) to guide it).
    * Please don't commit compiled and project files.
    * You can suggest other features by editing the requirements above.
1. [**Push**][ref-push]/sync the changes up to GitHub.
1. [Create a **pull request**][pull-request] to the original repository to turn in the assignment, don't forget to mention your pair.

(A pull-request screencast [demo](http://screencast-o-matic.com/watch/coe3IEeMDa) - done for another course)

### Submission
Submit a pull request by next next Tirgul, this time you don’t need to use the regular submitting form, but you can if you must :smile:).

Requirements: correctness, completness, code coverage, code quality, TDD cycle including Refactoring, meaningful commit messages.

We will give feedback through the pull-request system. 
We will reserve one more week for improvements (please leave a comment for every change you do after submitting the PR).<br/>
Good luck!

<!-- Links -->
[ref-or]: http://he.wikipedia.org/wiki/%D7%A8%D7%A2%D7%99%D7%93%D7%AA_%D7%94%D7%90%D7%93%D7%9E%D7%94_%D7%91%D7%A0%D7%A4%D7%90%D7%9C_(2015)#cite_note-7
[forking]: https://guides.github.com/activities/forking/
[ref-clone]: http://gitref.org/creating/#clone
[ref-commit]: http://gitref.org/basic/#commit
[ref-push]: http://gitref.org/remotes/#push
[ref-pull]: http://gitref.org/remotes/#pull
[config-remote]: https://help.github.com/articles/configuring-a-remote-for-a-fork/
[sync-remote]: https://help.github.com/articles/syncing-a-fork/
[pull-request]: https://help.github.com/articles/creating-a-pull-request
