from training.dqn_training import model as dqn_model
from training.pg_training import model as ppo_model
from environment.custom_env import LearningPlatformEnv

def evaluate(model, env):
    state = env.reset()
    total_reward = 0
    done = False
    while not done:
        action, _states = model.predict(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward
    return total_reward

# Initialize environment
env = LearningPlatformEnv()

# Evaluate DQN
dqn_reward = evaluate(dqn_model, env)
print(f"DQN Total Reward: {dqn_reward}")

# Evaluate PPO
ppo_reward = evaluate(ppo_model, env)
print(f"PPO Total Reward: {ppo_reward}")
