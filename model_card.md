# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeEngine 1.0 (Experimental Energy-First Edition)**

---

## 2. Intended Use  

This model is a classroom exploration tool designed to simulate a Content-Based Filtering music recommender. It suggests 5 songs from a small 20-song catalog by mathematically calculating the "distance" between a user's stated preferences (Genre, Mood, Energy, etc.) and a track's metadata. It is intended for educational purposes only and not for real-world commercial use.

---

## 3. How the Model Works  

The recommender uses a "weighted point system" to rank songs. For every song in the catalog, it checks if the Genre and Mood match the user's favorites (+1.0 and +1.5 pts respectively). It then calculates how close the song's energy, acousticness, and positivity (valence) are to the user's targets, awarding up to 4.0 points for energy and 1.5 points for acousticness. Finally, it adds a small bonus for matching tempo. All these points are summed into a "Relevance Score" out of 8.5, and the top 5 highest-scoring songs are recommended.

---

## 4. Data  

The dataset consists of 20 songs in a CSV format (`data/songs.csv`). It covers a variety of genres like pop, lofi, rock, ambient, and metal. Each song is tagged with human-labeled metadata (Mood, Genre) and technical audio features (Energy, Tempo, Valence, Acousticness). While diverse for its size, the catalog is extremely limited and does not represent complex sub-genres or non-English language tracks.

---

## 5. Strengths  

The system is highly effective at finding "ideal" matches when a user's categorical preferences (like Genre) align with their technical ones (like Energy). It excels at identifying clear-cut vibes like "Chill Lofi" or "High-Energy Pop" because the scoring system prioritizes the strongest common denominators between multiple musical features.

---

## 6. Limitations and Bias 

One major weakness is the "Categorical Bias" discovered during stress testing. Because Genre and Mood matches are fixed point bonuses, they can sometimes "drown out" a user's actual target for how the music should sound. For example, in the original configuration, a user who specifically asked for high-energy music was recommended a very slow, quiet track simply because the track's genre label matched their favorite list. This suggests that the system may over-prioritize human-labeled categories over the actual technical characteristics of the audio, potentially creating a "filter bubble" where users only see music labeled with their favorite genre, even if it doesn't match the energy level they requested.

---

## 7. Evaluation  

The model was evaluated using four distinct user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an "Adversarial" profile with conflicting preferences. I specifically looked for cases where the top recommendation didn't "feel" right. This led to a "Weight Shift" experiment where the energy importance was doubled and the genre importance was halved, which successfully fixed a major bias where slow music was being recommended to high-energy seekers.

---

## 8. Future Work  

If I had more time, I would introduce a "Diversity Multiplier" to ensure that the top 5 results aren't all from the same genre. I would also move away from "Exact Match" logic for genres and use a "Genre Similarity Matrix" so that the system knows "Rock" and "Metal" are related, even if the user didn't explicitly list both.

---

## 9. Personal Reflection  

Building this simulation showed me how "simple" math like subtraction and addition can drive the multi-billion dollar algorithms we use daily. I was surprised by how much a single number (like the +2.0 weight on Genre) could completely change the user experience. It made me realize that even if an AI seems objective, its "personality" is really just a set of weights chosen by a human engineer, which can easily introduce unintended biases into what we hear and see online.
