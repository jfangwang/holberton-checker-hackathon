# Checker Daddy
A Holberton School checker tool.

## Requirements
* Python 3.4+
* Python Requests Module: `pip3 install requests`
* Flask 1.1+: `pip3 install Flask`

## Setup and Usage
1. Clone the repository and `cd` into it.
2. Run the command `python3 -m flask.app` to run the Flask app.
3. In your web browser, type `localhost:5000/login` into your search bar and hit `Enter`. If you are running the Flask app form a virtual machine, you will have to forward the port in order to view it on your host machine's browser.
4. You should see a login page wherein you can enter your Holberton School intranet credentials.
![Checker Daddy Login Page](https://i.imgur.com/wXVbADp.png)
5. In the `API Key` field, enter the API key that can be found on the intranet's "Tools" page under the header "Holberton's Intranet API Key".
6. In the `Your Email` and `Your Password` fields, enter the email address and password with which you log into the intranet.
7. If your credentials are not valid, you will be asked to fill in your information again.
8. Otherwise, paste a project's URL into the `Project URL` field and a task number into the `Task Number` field.
![Checker Daddy Project Page with Input Examples](https://i.imgur.com/YQuXxDG.png)

## Authors
* Tim Assavarat (<721@holbertonschool.com>)
* Scout Curry (<546@holbertonschool.com>)
* Nga La (<708@holbertonschool.com>)
* Drew Maring (<675@holbertonschool.com>)
* Ethan Mayer (<653@holbertonschool.com>)
* Koome Mwiti (<698@holbertonschool.com>)
* Julienne Tesoro (<484@holbertonschool.com>)
