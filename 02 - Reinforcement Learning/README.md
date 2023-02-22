# Reinforcement Learning

In this lesson, we will introduce the gymnasium library and how to use it. The description of the basic functions of the library is in the file
`reinforcement.py`.

The `gymnasium` library started as OpenAI gym. This newer version is a direct replacement of the original library. You can upgrade to gymnasium simply by using the import `import gymnasium as gym`. Installing the library is also simple, just run `pip install gymnasium`. 

## Exercise (for the lesson, not a homework)

Implment a reinforcement learning agent for a simple environment (e.g. `MountainCar-v0`) using Q-learning. Note that the environment returns a continuous state -- you will need to discretize it somehow.