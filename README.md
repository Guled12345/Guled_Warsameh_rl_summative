# 🎓 Reinforcement Learning for Personalized Education

## 🎯 Project Mission

The goal of this project is to optimize an agent in an unique learning platform  environment by implementing and comparing two reinforcement learning techniques: Deep Q-Network (DQN) and Policy Gradient Methods (PPO). The agent chooses strategic actions in a specific context with the aim of optimizing student learning results. In order to assess value-based (DQN) and policy-based (PPO) approaches, the study examines their generalization capacity, exploration-exploitation tradeoff, and convergence speed. 

---

## 🌟 Features

- 🔧 Custom Gym Environment for RL-based education tracking  
- 🤖 Personalized Learning using adaptive reinforcement learning (DQN & PPO)  
- 🧩 Discrete State & Action Spaces for structured learning dynamics  
- 📈 Visualized Training Metrics for performance comparison  
- 🎥 Simulation Video showcasing the agent's learning behavior  

---

## 🔗 Links to Explore

- 📄 [Project Report Document (PDF)](https://drive.google.com/drive/folders/1Wz5X3NZTQiSou5ROVQnfuruxYYvs4j_8?usp=drive_link)  
- 💻 [GitHub Repository](https://github.com/Guled12345/Guled_Warsameh_rl_summative)  
- 🎬 [Simulation Video on Google Drive](https://drive.google.com/drive/folders/1Wz5X3NZTQiSou5ROVQnfuruxYYvs4j_8?usp=drive_link)

---

## 🧠 Reinforcement Learning in Education

### 📌 State Space (4 States)

1️⃣ **Beginner** – Just starting the learning process.  
2️⃣ **Active Learner** – Engaging actively with content.  
3️⃣ **Proficient** – Shows subject-matter understanding.  
4️⃣ **Independent Thinker** – Applies concepts independently.

---

### 🎮 Action Space (5 Actions)

- 📘 **Lesson Suggestion** – Recommend new lessons.  
- 📝 **Provide Additional Material** – Share more resources.  
- ⚙️ **Adjust Lesson Difficulty** – Make learning harder/easier.  
- 🧠 **Add Challenges** – Introduce thought-provoking tasks.  
- 💬 **Encourage Participation** – Boost learner motivation.

---

## 📊 Reward Structure

| Action                  | Reward |
|-------------------------|--------|
| Complete Lesson         | +15    |
| Ace Quiz                | +25    |
| Assist Peer             | +30    |
| Ignore Recommendation   | -10    |
| Inactivity              | -20    |

---

## 📈 Key Results

### 🧪 Cumulative Rewards
![Cumulative Reward Comparison](assets/cumulative_reward.png)
> PPO reaches higher cumulative rewards faster than DQN.

---

### 📉 Training Stability
![Training Loss and Policy Entropy](assets/training_stability.png)
> DQN shows early fluctuation in loss; PPO's entropy steadily decreases.

---

### 🏁 Convergence Speed
![Episodes to Convergence](assets/convergence.png)
> PPO stabilizes around 3,000 episodes; DQN takes about 5,500.

---

### 🧠 Generalization Performance
![Generalization Graph](assets/generalization.png)
> PPO maintains strong performance in unseen states. DQN struggles without retraining.

---

## 🔮 Future Improvements

- 🔧 Fine-tune hyperparameters for better adaptability.  
- 📚 Integrate curriculum learning for gradual difficulty progression.  
- 🎯 Expand action space with deeper interventions.  
- 🌍 Integrate with real educational platforms (LMS, EdTech tools).

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Guled12345/Guled_Warsameh_rl_summative.git
cd Guled_Warsameh_rl_summative
2️⃣ Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
On Windows:

bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🧪 Running the RL Agent
Run the environment without training:

bash
Copy
Edit
python play.py
📌 Author
Guled Hassan Warsameh
