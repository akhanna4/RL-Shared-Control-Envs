import gym
import retro
import sys
import os
import time
import numpy as np
from collections import deque
from argparse import ArgumentParser
from IPython import display
import matplotlib.pyplot as plt


# ------------------------- Code for keyboard agent ------------------------- #
# from https://github.com/openai/gym/blob/master/examples/agents/keyboard_agent.py

do_user_action = False
user_action = -1

# w - move paddle up
# s - move paddle down

def key_press(k, mod):
    global do_user_action, user_action
    if k == ord('w'):
        user_action = 0
        do_user_action = True
    if k == ord('s'):
        user_action = 1
        do_user_action = True



def key_release(k, mod):
    global do_user_action, user_action
    do_user_action = False
    user_action = -1

# -------------------------------------------------------------------------- #

def main(args):
    # you can modify this players argument to create a multi agent environment
    env = retro.make(game='Pong-Atari2600', players=1)

    # for playing with keyboard
    # enable key presses
    env.render()
    env.unwrapped.viewer.window.on_key_press = key_press
    env.unwrapped.viewer.window.on_key_release = key_release
    global do_user_action, user_action

    user_action = -1
    do_user_action = False

    running_reward = None
    reward_sum = 0
    for i_episode in range(args.num_episodes):
        state = env.reset()
        for t in range(args.max_steps):
            
            # translate action based on key presses
            translated_action = [0, 0, 0, 0, 0, 0, 0, 0]

            if user_action != -1:
                if user_action == 0:
                    translated_action[4] = 1

                elif user_action == 1:
                    translated_action[5] = 1

                else:
                    translated_action[4] = 0
                    translated_action[5] = 0 

            state, reward, done, _ = env.step(translated_action)
            reward_sum += reward_sum

            env.render()
            if done:
                running_reward = reward_sum if running_reward is None else running_reward * 0.99 + reward_sum * 0.01
                print('resetting env. episode reward total was %f. running mean: %f' % (reward_sum, running_reward))
                reward_sum = 0
                break

            if reward != 0:
                print('ep %d: game finished, reward: %f' % (i_episode, reward) + ('' if reward == -1 else ' !!!!!!!'))

            time.sleep(0.05)

    env.close()


if __name__ == "__main__":
    parser = ArgumentParser(description='Retro Pong-v0')

    parser.add_argument('--num_episodes', type=int, default = 2000,
                        help='number of episodes for training')
    parser.add_argument('--max_steps', type=int, default=10000,
                        help='max number of time steps per episode')

    args = parser.parse_args()
    main(args)

