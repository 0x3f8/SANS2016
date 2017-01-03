This folder contains a copy files I used in conjunction with the [Mobile Analytics Sprusage Git Repo](https://github.com/warriar/git) which is used to solve part 2 of the Mobile Analytics Server.

These two php scripts that can assist with exploiting the vulnerabilities.

[makeCookie.php](./makeCookie.php) will create a cookie for the administrator account for the Mobile Analytics Sprusage page.  After logging in to the page as guest you can modify the AUTH cookie with this data to switch to the administrator account.
  
[decodeCookie.php](.//decodeCookie.php) will decode the cookies from the Sprusage application, including any you create with the makeCookie script.

I solved this using recent stable 5.x version of PHP.  You'll also need the [mcrypt plugin](../../Misc%20Files/php) installed.
  
These scripts require files from the git repo and should be run from its root folder.  You should be able to clone that repo from the link above.

Alternately you can reference the repo online and look at past commits.  In there you'll find a working copy of the administrator password.

