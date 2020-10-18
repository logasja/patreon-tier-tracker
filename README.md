# Patreon Notifier

<img align=center src="./imgs/patreon_ico.png" alt="Patreon logo" title="patreon.com" height=100 />

<img align=center src="./imgs/plus.png" height=50 margin=25 />

<img align=center src="./imgs/ifttt_ico.png" alt="IFTTT logo" title="IFTTT icon" height=100/>

This is a tool used to notify you if a slot opens in a limited tier on Patreon. It is done by scraping the Patreon page of the account you choose and activating a webhook in IFTTT. The IFTTT integration must be set up manually and the tool can be run on a remote heroku instance that I lay out here.

## Install
To install this script's dependencies you will need Python 3 with pip installed and run the following:

```
pip install -r requirements.txt
```

## Configuration
The configuration file (config.json) needs to be filled out before running the script. 

```account``` refers to the Patreon account you'd like to track and ```tier``` is the name of the tier you'd like to track.

IFTTT configuration uses values found in the Webhooks services documentation on ifttt.com. The url you are looking for looks like this: https://maker.ifttt.com/trigger/{ifttt_event}/with/key/{ifttt_key}. You will create your own Webhook service with a custom event name and attach it to any action you'd like (e.g. send a text, ifttt notification).

A filled config file looks like the following:
```
{
  "account": "ThoughtSlime",
  "ifttt_key": "YOURSECRETKEY",
  "ifttt_event": "my_event",
  "tier": "Slime Warriors"
}
```

## Running Locally
After the installation and configuration steps running the script is simple, just call: ```python run.py```

## Running on Heroku
Using Heroku allows you to have the script constantly checking Patreon without needing to take up computer resources. Follow these instructions to run the script on a Heroku server.

1. Install the Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli)
2. Login to the CLI
```
heroku login
```
3. Create new application
```
heroku create appname
```
4. Add files to push
```
heroku git:remote -a appname
```
5. Push to heroku
```
git push heroku main
```

# Contributing
Feel free to fork and open pull requests! This was a small project I put together in an afternoon so I'm sure there are some little bugs or ways that this can be done slightly more intelligently. Happy Hacking!