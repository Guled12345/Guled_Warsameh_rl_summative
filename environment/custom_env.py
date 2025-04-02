import gymnasium as gym
from gymnasium import spaces
import numpy as np

class LearningPlatformEnv(gym.Env):
    def __init__(self):
        super(LearningPlatformEnv, self).__init__()

        # Define state space: Student Learning Levels
        self.state_space = ["Beginner", "Active Learner", "Proficient", "Independent Thinker"]
        self.current_state = 0  # Start as a Beginner

        # Define action space: What the platform can do
        self.action_space = spaces.Discrete(5)  # 5 actions

        # Reward system
        self.rewards = {
            "complete_lesson": 15,
            "ace_quiz": 25,
            "assist_peer": 30,
            "ignore_recommendation": -10,
            "inactivity": -20
        }

        self.max_steps = 50  # Max steps per episode
        self.current_step = 0

    def step(self, action):
        reward = 0

        # Define action effects
        if action == 0:  # Suggest lessons
            reward = self.rewards["complete_lesson"]
        elif action == 1:  # Provide extra material
            reward = self.rewards["ace_quiz"]
        elif action == 2:  # Adjust lesson difficulty
            reward = self.rewards["assist_peer"]
        elif action == 3:  # Insert challenges
            reward = self.rewards["ignore_recommendation"]
        elif action == 4:  # Encourage participation
            reward = self.rewards["inactivity"]

        self.current_step += 1
        done = self.current_step >= self.max_steps

        # Move to next state randomly
        if np.random.rand() > 0.5 and self.current_state < len(self.state_space) - 1:
            self.current_state += 1

        return self.current_state, reward, done, {}

    def reset(self, seed=None, options=None):
        self.current_state = 0
        self.current_step = 0
        return self.current_state, {}

    def render(self):
        print(f"Student Learning Level: {self.state_space[self.current_state]}")
