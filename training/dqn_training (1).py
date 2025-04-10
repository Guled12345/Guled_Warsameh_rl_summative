import gymnasium as gym
from stable_baselines3 import DQN

# Try importing the custom environment, handle ModuleNotFoundError
try:
    from environment.custom_env import LearningPlatformEnv
except ModuleNotFoundError:
    import sys
    sys.path.append("C:/Users/Hp/Desktop/Guled_Warsameh_rl_summative")
    from environment.custom_env import LearningPlatformEnv

# Create the environment
env = LearningPlatformEnv()

# Define and train DQN model
model = DQN("MlpPolicy", env, learning_rate=0.001, gamma=0.95, verbose=1)
model.learn(total_timesteps=10000)

# Save the trained model
model.save("models/dqn/learning_model.zip")

print("DQN training complete!")
