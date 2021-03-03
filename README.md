# KINGBOT
This is a userbot of Telegram which is based on telethon API.


<p align="center">
  <img src="./resources/extras/logo_rdm.png" alt="Kartikrajofficial">
</p>

[![Stars](https://img.shields.io/github/stars/kartikrajofficial/KINGBOT?style=flat-square&color=blue)](https://github.com/kartikrajofficial/KINGBOT/stargazers)
[![Forks](https://img.shields.io/github/forks/kartikrajofficial/KINGBOT?style=flat-square&color=green)](https://github.com/kartikrajofficial/KINGBOT/fork)
[![Python Version](https://img.shields.io/badge/Python-v3.9-red)](https://www.python.org/)
[![Contributors](https://img.shields.io/github/contributors/kartikrajofficial/KINGBOT?style=flat-square&color=green)](https://github.com/kartikrajofficial/KINGBOT/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/kartikrajofficial/KINGBOT/blob/master/LICENSE)
[![Size](https://img.shields.io/github/repo-size/kartikrajofficial/KINGBOT?style=flat-square&color=yellow)](https://github.com/kartikrajofficial/KINGBOT/)




# Deploy 
- [Heroku](https://github.com/kartikrajofficial/KINGBOT#Deploy-to-Heroku)
- [Local Machine](https://github.com/kartikrajofficial/KINGBOT#Deploy-Locally)

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)





## Deploy Locally
- Get your `API_ID` and `API_HASH` from [here](https://my.telegram.org/)
- Get your `REDIS_URI` and `REDIS_PASSWORD` from [here](https://redislabs.com), tutorial [here](./resources/extras/redistut.md).
- Clone the repository: <br />
`git clone https://github.com/kartikrajofficial/KINGBOT.git`
- Go to the cloned folder: <br />
`cd Ultroid`
- Create a virtual env:   <br />
`virtualenv -p /usr/bin/python3 venv`   
`. ./venv/bin/activate`
- Install the requirements:   <br />
`pip install -r requirements.txt`   
- Generate your `SESSION`:   
`bash sessiongen`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/TeamUltroid/Ultroid/blob/main/.env.sample).    
(You can either edit and rename the file or make a new file.)
- Run the bot:   
`bash resources/startup/startup.sh`
