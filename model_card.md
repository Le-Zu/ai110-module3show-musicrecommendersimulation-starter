# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
**VibeEngine 1.0 (Experimental Energy-First Edition)**

---

## 2. Goal / Task
The goal of this recommender is to suggest the top 5 most relevant songs from a small catalog based on a user's stated musical preferences. It tries to predict "relevance" by calculating the mathematical similarity between a user's taste profile and a song's attributes.

---

## 3. Data Used
- **Dataset:** `data/songs.csv` containing 20 tracks.
- **Features:** Includes human-labeled categories (Genre, Mood) and technical audio metrics (Energy, Tempo BPM, Valence/Positivity, Acousticness).
- **Limitations:** The small catalog size limits variety, and the "Mood" and "Genre" labels are subjective and fixed.

---

## 4. Algorithm Summary
The system uses a "weighted point system." It awards points if a song matches your favorite genre or mood. It then gives higher scores to songs that are "closer" to your target energy, acousticness, and positivity levels. These points are added up into a final score, and the songs with the highest totals are recommended first.

---

## 5. Observed Behavior / Biases
- **Categorical Bias:** Originally, the system favored matching a "Genre" label so much that it would recommend slow songs to people who asked for high energy.
- **"Gym Hero" Effect:** Because some songs have very high values across multiple popular features (high energy + high danceability), they tend to appear as "safe bets" for many different types of users, even if they aren't a perfect match.

---

## 6. Evaluation Process
- **Profile Testing:** I tested the system with "High-Energy Pop," "Chill Lofi," "Deep Intense Rock," and an "Adversarial" profile with conflicting tastes.
- **Weight Experiment:** I halved the importance of Genre and doubled the importance of Energy to see if the system could become more sensitive to the actual sound of the music rather than just its labels.
- **Comparison:** I compared the results before and after the weight shift to verify if the "Adversarial" profile's results improved.

---

## 7. Intended Use and Non-Intended Use
- **Intended Use:** This system is for **educational exploration** and learning how recommendation algorithms work in a classroom setting.
- **Non-Intended Use:** This should **not** be used for real music streaming services, as it lacks a large enough catalog and does not account for user listening history or complex musical relationships.

---

## 8. Ideas for Improvement
1. **Diversity Multiplier:** Add a rule that prevents the top 5 from being all the same genre, forcing the system to show more variety.
2. **Genre Similarity:** Create a map so the system knows that "Rock" and "Metal" are similar, even if the user didn't list both.
3. **Negative Preferences:** Allow users to list "genres I hate" to subtract points from certain songs.

---

## 9. Personal Reflection

**Biggest Learning Moment:**
My biggest learning moment was discovering the "Adversarial Glitch." I realized that a single number—the "weight" of a genre—could completely silence a user's other preferences. Seeing a slow, sad song get recommended to someone asking for high-energy music just because of a label showed me how "human bias" in engineering can lead to poor AI results.

**Using AI Tools:**
AI tools helped me quickly generate multiple test profiles and analyze large blocks of terminal output. However, I had to double-check the math constantly. For example, when I doubled the energy weight, I had to verify that the final scores didn't exceed the "max score" in a way that would make the "Why" explanations confusing.

**Simple Algorithms vs. Recommendations:**
I was surprised by how a simple math formula (subtraction and addition) could create a result that "felt" like a real recommendation. It showed me that many complex systems we use every day are likely just much larger versions of this same basic logic.

**Next Steps:**
If I extended this project, I would try to add "Collaborative Filtering," where the system looks at what *other* users liked to make even better guesses, rather than just looking at the song's features.
