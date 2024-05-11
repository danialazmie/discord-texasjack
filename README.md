# texasjack

## Description

This project is a simple project in implementing a Chatbot in Discord using an LLM. The Chatbot was designed to only have a few features:

- History-aware chat 
- Vulgarity detection
- Have a sense of humor

There are a number of ideas to be implemented in the future. See [Future Work](#future-work)

## Prerequisites

### Credentials

There are two credentials required for this project:

- Discord Bot token - `src/credentials.py`
- OpenAI API key - `src/llm/credentials.py`

Insert your tokens in the files respectively. 

### Python

This project was developed in `Python 3.10.14`. So for the best of interest, please use the same version to avoid any issues.

The official binary installer for `Python 3.10.14` is not publicly available anymore due to their policy. Here you have two options:

#### Install via Miniconda (**Recommended**)

- These installers are easier to manage, and handle most things for you.
- Download and install Miniconda [here](https://docs.anaconda.com/free/miniconda/miniconda-other-installer-links/)


#### Install through third-party providers

- There are repositories that keep all the released binary installers
- Might be untrustworthy as they might be tampered with

### Dependencies

The requirements for the project can be found in the `requirements.txt` file. 

#### Detailed steps (Using Miniconda)

- For Windows, search and run `Anaconda Prompt (miniconda3)` program from Windows Search
- For Linux, run `conda activate` to start the interpreter. It should display something like:

```shell
(base) user@host:~$ 
```

- (Optional) Create a virtual environment `conda create --name <env-name> python=3.10.14`
- (Optional) Activate the new environment `conda activate <env-name>`
- Navigate to the src directory `cd <some_path>/src`
- Execute `pip install -r requirements.txt`

This will install all the required packages for the project to work.

## Running the server

Navigate to the `src` folder and run `python bot.py` which will start the bot.

To stop the server, just hit `CTRL+C`.

## Future Work

- User-aware chat 
- Actions using agents:
  - Discord administrative actions
  - Aware to major events (e.g how many times a user is warned)
- Act as a source of reference for military facts (laws/history)