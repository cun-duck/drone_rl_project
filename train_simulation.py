import gym
from stable_baselines3 import PPO
from utils.drone_env_simulation import DroneEnvSim

env = DroneEnvSim()
model = PPO("CnnPolicy", env, verbose=1)
model.learn(total_timesteps=100000)
model.save("ppo_drone_sim")
