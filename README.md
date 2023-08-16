# discord-relay-bot


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/danik9/discord-relay-bot)
![GitHub issues](https://img.shields.io/github/issues/danik9/discord-relay-bot)


## Description
A python program to relay messages from one discord server to another server using bot accounts. This project is basically almost all heavlly writted by chatGPT A.I! with me tweaking a couple things here and there!

Inspired by [joshmalek/discord-relay](https://github.com/joshmalek/discord-relay).

## Use Case
This program is useful when you're part of a paid Discord server that charges for access (e.g., Reselling, Crypto, FBA). You can use one account to access the server and relay the information to your personal server, sharing the info for free or charging for access. Importantly, the listening account operates like a regular human Discord account (selfbot), making it difficult for server administrators to detect message scraping.

**Note:** This program requires a minimum of **two distinct Discord accounts**. The repository includes a version with one listener account and **8** relayer accounts. While I'm not an expert coder by all means, the code is simple enough to scale.

## How it works
The Listener selfbot listens to messages in specific source channels and relays them to corresponding relay bots through direct messages.

The listener selfbot script utilizes the ***discord.py-self*** API wrapper (a fork of the popular discord.py for user accounts). During the initial stages of development, I discovered that the regular discord.py API wrapper is incompatible with user tokens.

In contrast, the relay bots utilize the official ***discord.py*** API wrapper, as they are genuine application bots (https://discord.com/developers/applications).

However, there's a catch: you can't run the listener selfbot script and the relay bots script in the same directory. Here's how to address this issue.

**Solution 1: Creating a Virtual Environment (Linux Edition)**

1. Ensure that the listener bot and relay bot are in separate folders.
2. Navigate to a bot folder (start with the listener bot).
3. Create a virtual environment using the following command:
   ```
   python3 -m venv venv_name
   ```
4. Activate the virtual environment:
   ```
   source venv_name/bin/activate
   ```
   You'll see the virtual environment's name in your command prompt.
5. Now, you can install packages using pip within the virtual environment. In the listener bot directory, run:
   ```
   python3 -m pip install -U discord.py-self
   ```
6. Repeat the process for the relay bot (run `pip install discord.py` when you start the virtual environment session).

If your having trouble just google `venv pyhton how to`




**Solution 2 (Preferred method): Using Docker**

Two Docker templates are provided in this repository. Docker templates are easy to set up and use. The provided templates will install dependencies and get you up and running quickly.

(If your new to docker I reccomend watching this video the help you get up to speed! https://www.youtube.com/watch?v=eGz9DS-aIeY)


**REMINDER:** Remember to edit the dockerfiles in each provided file, along with the relay bots' supervisord.conf file.

1. Listener bot:
   - Navigate to the directory containing the listener bot Dockerfile and script.
   - Build the Docker image:
     ```
     docker build -t dislistener .
     ```
   - Start the Docker container with the following command (this ensures the container starts on reboot):
     ```
     docker run -d --name discord-listener --restart always dislistener
     ```
   - Your Docker container is now running, and the bot is online. To check the status, use `docker ps`.

2. Relay bot:
   - The provided dockerfile sets up 8 relay bots for forwarding 8 channels. Modify the dockerfile and a config file if you need more or fewer bots.
   - To simultaneously run multiple Python scripts within the discord-relay Docker container, we're using supervisord. Edit the supervisord.conf file with your script names.
   - Navigate to the directory containing the relay bot Dockerfile and scripts.
   - Build the Docker image:
     ```
     docker build -t disrelay .
     ```
   - Start the Docker container with the following command (this ensures the container starts on reboot):
     ```
     docker run -d --name discord-relay --restart always disrelay
     ```
   - Your Docker container is now running, and the bots are online. To check the status, use `docker ps`.

## Software Requirements
1. Python
2. pip
3. discord.py-self (for the listener bot)
4. discord.py (for the relay bots)
5. Docker (recommended)

#### Account Setup and Channel Requirements
1. Listener account token (can be bot or human account, use human at your own risk, technically bannable but I've had no issues)
2. Relayer account tokens (should usually be bot accounts)
3. Channel you want to relay messages *from* (must be a member)
4. Channel you want to relay messages *to* (must be an owner)

***URL for where to set up discord developer bots: https://discord.com/developers***

All information about keys and channel ID's can be easily found through Google.

Both account tokens will be 59-character strings, looking like "NDY0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx".

The channel ID will be an 18-digit string, resembling "42xxxxxxxxxxxxxxxx".
