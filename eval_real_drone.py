import rospy
from stable_baselines3 import PPO
from utils.drone_env_real import RealDroneEnv

env = RealDroneEnv()
model = PPO.load("ppo_drone_real")

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()
