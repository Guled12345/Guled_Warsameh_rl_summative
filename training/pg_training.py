import gymnasium as gym
from stable_baselines3 import PPO
from environment.custom_env import LearningPlatformEnv

# Create the environment
env = LearningPlatformEnv()

# Define and train PPO model
model = PPO("MlpPolicy", env, learning_rate=0.001, gamma=0.95, verbose=1)
model.learn(total_timesteps=10000)

# Save the trained model
model.save("models/pg/learning_model.zip")

print("PPO training complete!")
