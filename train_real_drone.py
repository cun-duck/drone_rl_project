import rospy
from stable_baselines3 import PPO
from utils.drone_env_real import RealDroneEnv

env = RealDroneEnv()
model = PPO("CnnPolicy", env, verbose=1)
model.learn(total_timesteps=100000)
model.save("ppo_drone_real")
