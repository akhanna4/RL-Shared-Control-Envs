# Retro Pong-v0 (Discrete)
Keyboard code for the OpenAI retro gym environment Pong-v0 with a discrete action space.
https://gym.openai.com/envs/Pong-v0/

## Installation

While there is a default Pong-v0 environment in OpenAI gym, it is not easy to use the environment for multiple agents. In other words, only one of the paddles can be controlled by us. The workaround for this problem is using the Pong-v0 environment in the OpenAI Retro Gym library, which is almost identical to the Gym Pong-v0 environment but you have the option to control both agents in the environment. 

The following dependencies need to be installed. 

```
pip install gym
pip install gym-retro
pip install torch torchvision
pip install ipython
pip install matplotlib
pip install argparse
```

You will then need to download the Atari-2600 ROMs via this link: http://www.atarimania.com/rom_collection_archive_atari_2600_roms.html. Unzip this file and then enter the ROMs directory. After, run

```
python -m retro.import .
```

## Run 

To run the program:

```
python main.py
```

The playing mode allows the user to play using keyboard input (using 'w' and 's'). 

## Notes

Have a max_steps value above 100 since the game starts acting strange when this value drops below 100.
