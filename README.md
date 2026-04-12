# 🎵 Music Recommender Simulation

## Project Summary

In this project, I built a Content-Based Filtering music recommender that suggests songs by calculating the mathematical "distance" between a user's taste profile and a track's metadata. My version, **VibeEngine 1.0**, specifically balances categorical data like Genre and Mood against technical audio features like Energy and Acousticness. Through iterative testing, I tuned the weights to ensure that the physical "vibe" of the music (energy) is prioritized over simple category labels, creating a more responsive and accurate recommendation experience.

---

## How The System Works

Major streaming platforms like Spotify and YouTube use hybrid recommendation systems that combine "Collaborative Filtering" (analyzing what similar users enjoy) with "Content-Based Filtering" (analyzing the specific attributes of a song).

This simulation employs a **Content-Based Filtering** approach. The system prioritizes "Sonic Alignment"—the mathematical similarity between a user's stated preferences and the available catalog.

### The Algorithm Recipe
The system calculates a "Relevance Score" (Max 8.5 pts) for every song in the catalog using a weighted point system:

| Feature | Weight (Max Points) | Scoring Logic |
| :--- | :--- | :--- |
| **Genre Match** | **+2.0 pts** | Exact match with user's favorite genres. |
| **Energy Similarity** | **+2.0 pts** | Reward songs closer to target energy (0.0-1.0). |
| **Mood Match** | **+1.5 pts** | Exact match with user's favorite moods. |
| **Acousticness** | **+1.5 pts** | Reward songs closer to target acousticness level. |
| **Valence** | **+1.0 pts** | Reward songs matching user's target positivity level. |
| **Tempo (BPM)** | **+0.5 pts** | Reward songs closer to target beats per minute. |

**Expected Biases:**
- **Genre Over-Prioritization:** Because a Genre match is weighted as highly as Energy, the system might ignore a perfect "chill lofi" track that exactly matches the user's energy and mood targets simply because the user didn't explicitly list "Lofi" in their favorite genres.
- **Precision Bias:** The system focuses on the closest mathematical matches, which can lead to a "filter bubble" where the recommendations lack diversity or surprise.

### Data Inputs
- **Song Features:** Metadata (Genre, Mood) and normalized acoustic data (Energy, Valence, Danceability).
- **User Profile:** A collection of target values representing ideal musical preferences.
- **Weights:** A configuration that determines the relative importance of each feature.

![Recommendation Output](image.png)

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

In this phase, I stress-tested the recommender with four distinct user profiles to evaluate how the scoring logic handles different musical tastes and edge cases.

### 1. High-Energy Pop
*   **Target:** Pop genre, Happy mood, 0.9 Energy.
*   **Result:** Successfully recommended **"Sunrise City" (6.30/8.5)** and **"Gym Hero" (4.91/8.5)**.
*   **Observation:** The system effectively combined genre and energy alignment for these "ideal" matches.

![High-Energy Pop Recommendations](Cursor_En0zx6YZVm.png)

### 2. Chill Lofi
*   **Target:** Lofi genre, Chill mood, 0.3 Energy, 0.8 Acousticness.
*   **Result:** Top pick was **"Library Rain" (6.81/8.5)**.
*   **Observation:** This profile achieved the highest overall scores, as the catalog has several tracks that perfectly match the "lofi-chill" archetype.

![Chill Lofi Recommendations](Cursor_8Hmy3T7GtR.png)

### 3. Deep Intense Rock
*   **Target:** Rock/Metal, Intense/Aggressive, 0.9 Energy, 160 BPM.
*   **Result:** **"Storm Runner" (5.94/8.5)** and **"Eternal Requiem" (5.78/8.5)**.
*   **Observation:** The system successfully prioritized BPM and energy alongside genre.

![Deep Intense Rock Recommendations](Cursor_Al2KYNF5JH.png)

### 4. Conflicting Preferences (Adversarial)
*   **Target:** Ambient genre, Melancholic mood, but with a high **0.9 Energy** target.
*   **Result:** **"Rainy Window" (4.14/8.5)**.
*   **Observation:** **The Glitch Found:** Even though the user wanted 0.9 energy, the system recommended a track with 0.22 energy because the **Genre Match (+2.0)** and **Mood Match (+1.5)** points outweighed the energy penalty. This reveals a bias where categorical data (Genre/Mood) can "drown out" the physical characteristics (Energy) of the music.

![Conflicting Preferences Recommendations](Cursor_sZiHhwIqTh.png)

---

## Limitations and Risks

- **Small Catalog Bias:** With only 20 songs, the system often recommends the same "statistical powerhouses" (like Gym Hero) to fill out top 5 lists, leading to a lack of variety.
- **Categorical Over-Prioritization:** Fixed point bonuses for Genre and Mood can sometimes "drown out" a user's actual target energy levels, as seen in my adversarial tests.
- **Lack of Cultural Context:** The system only understands numbers and labels; it doesn't understand the cultural connection between genres or the lyrical meaning of songs.

---

## Reflection

[**Detailed Reflection in reflection.md**](reflection.md)

Through this project, I learned that recommendation systems are essentially giant math problems where "relevance" is just a sum of weighted scores. I was surprised by how much a single weight change—like doubling the importance of energy—could completely flip the results from being category-focused to sound-focused. This realization highlighted the inherent "power" of the engineer: the AI doesn't have an objective opinion on what music is "good," it simply follows the weights we provide, which can easily introduce unintended biases or "filter bubbles."

Building this changed how I view real-world apps like Spotify; I now see them as massive balancing acts where human decisions about "what matters most" (is it genre? is it popularity? is it current mood?) directly shape our cultural experiences. It's a reminder that even the "smartest" models still require constant human oversight and iterative testing to remain fair and useful.

---

## 7. Final Model Card

The finalized documentation for this system can be found in the link below.

[**View Final Model Card**](model_card.md)
