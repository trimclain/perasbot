<h1 align="center">
    <img src="img/peras-logo.png" alt="Peras">
</h1>

[Telegram Link](https://t.me/persassbot)

PERAS is a PERsonal ASsistant Bot in Telegram.
The initial idea behind this is to implement my knowledge into one single bot.

## How to setup
1. Make sure you have git and make:
```
sudo apt install -y git make
```
2. Clone this repository.
3. Run `make` to install pip3 and venv.
4. Run `make venv` to create a venv.
5. Run `make install_reqs` to install required modules.

## How to use this code with your own bot
1. Go to [Botfather](https://t.me/botfather)
2. Create a new bot and copy the token.
3. Save the token to a `.token` file in the same folder as `main.py`.
4. Run `./start` to start the bot as a background process. </br>
   The bot should work now. Check it with the `/start` command. </br>
   Run `./stop` to stop the bot.
