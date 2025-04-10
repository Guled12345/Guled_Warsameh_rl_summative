# 🎓 Reinforcement Learning for Personalized Education

## 🎯 Project Mission

My mission at ALU is to transform the education system of Somalia by empowering youth through emerging technologies. This initiative aims to build a **Business Innovation Hub**, bringing together entrepreneurs, innovators, leaders, and students for collaboration and creativity.  

This RL-powered **Personalized Learning & Skill Development** system adapts dynamically to student progress, ensuring tailored challenges and resources for every learner.

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

- 🧪 **DQN** required ~5500 episodes to converge.  
- ⚡ **PPO** converged faster, at ~3000 episodes.  
- 🔄 PPO showed better generalization to new states.  
- 📉 DQN had more variance early on and required more tuning.

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
