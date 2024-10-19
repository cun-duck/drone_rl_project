# Drone Reinforcement Learning Project

## Project Overview
This project aims to train an AI model using reinforcement learning (RL) for autonomous drone control in photography, mapping, and topography tasks. The training is initially performed in a simulated environment using AirSim and then transferred to a real drone environment using sensor data from the actual drone.

## Requirements
- Python 3.8 or above
- TensorFlow / PyTorch
- Stable-Baselines3
- Microsoft AirSim (for simulation)
- ROS (for real-world drone control)

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/your-github/drone-rl-project.git
    cd drone-rl-project
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Set up AirSim for simulation:
   Follow [AirSim Documentation](https://microsoft.github.io/AirSim/) to set up the simulation environment.

4. For real drone deployment, ensure ROS and MAVROS are properly configured on your onboard computer (Jetson/Raspberry Pi).

## Running the Simulation
1. Train the model in a simulated environment:
    ```
    python train_simulation.py
    ```
   This will train the model and save it as `ppo_drone_sim`.

## Running on a Real Drone
1. Deploy the model on a real drone by running the following:
    ```
    python train_real_drone.py
    ```

2. To evaluate the model on a real drone, run:
    ```
    python eval_real_drone.py
    ```

## Data Used
- The project utilizes simulation data from AirSim for initial training.
- For real-world deployment, it uses sensor data from the drone's camera, GPS, and IMU.

## Future Improvements
- Integrate additional sensors like Lidar for obstacle detection.
- Optimize the model for more complex navigation tasks in real-world environments.
