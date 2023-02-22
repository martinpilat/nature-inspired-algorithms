import numpy as np

def show_animation(agent, env, steps=200, episodes=1):
    ''' A helper function to show the behavior of an agent in an environment.

    Parameters
    ----------
    agent: 
        The agent that should be displayed, it must implement a method
        act(observation, reward, done)

    env:
        The OpenAI Gym environment to use
    
    steps: int
        The number of steps that should be simulated
    
    episodes: int
        Number of episodes to simulate - each has `steps` steps.
    '''
    for i in range(episodes):
        obs, info = env.reset()
        done = False
        terminated = False
        R = 0
        t = 0
        r = 0
        while not (done or terminated) and t < 200:
            env.render()
            action = agent.act(obs, r, done)
            obs, r, done, terminated, _ = env.step(action)
            R += r
            t += 1
        agent.reset()

def moving_average(x, n):
    weights = np.ones(n)/n
    return np.convolve(np.asarray(x), weights, mode='valid')