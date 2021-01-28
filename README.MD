# Reddit Kits Bot
A reddit bot that scraps data from r/Drumkits and r/LoopKits, helping producers not wasting their time searching random kits on reddit.

## Functionality
Running *main.py* will send you an email with all the "good" kits from the last week

## Technologies used
**Languages:** Python, HTML;

**Modules:** time, datetime, smtp, email, bs4, praw (reddit api wrapper)

## Using
To use this repo you need to install **Python** and the modules **bs4** and **praw**
```bash
pip3 install bs4
pip3 install praw
```

After that create a folder named ***secret***, on the same folder as *main.py*.

Then you should log in reddit and go to [Reddit](https://www.reddit.com/prefs/apps) and click on **I'm a developer** to get the *client id* and *client secret*.

Inside of that folder you must create a new file named ***passw.py*** where you write the following code, replacing the comments with the right keys/emails.

```python
sender = # email that will send
receiver = # email that will receive
pw = # sender email password
c_id= # reddit client id
c_secret= # reddit client secret
agent= # reddit client agent (must be unique) 
```

Congratulations!!! Now you can run *main.py* and you will receive an email containing the drumkits/loopkits.