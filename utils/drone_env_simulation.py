import gym
import airsim
import numpy as np

class DroneEnvSim(gym.Env):
    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

    def reset(self):
        self.client.reset()
        return self.get_observation()

    def step(self, action):
        self.client.moveByVelocity(action[0], action[1], action[2], 1)
        reward = self.calculate_reward()
        done = self.check_done()
        return self.get_observation(), reward, done, {}

    def get_observation(self):
        response = self.client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene)])
        img1d = np.fromstring(response[0].image_data_uint8, dtype=np.uint8)
        img_rgb = img1d.reshape(response[0].height, response[0].width, 3)
        return img_rgb

    def calculate_reward(self):
        return reward

    def check_done(self):
        return done
