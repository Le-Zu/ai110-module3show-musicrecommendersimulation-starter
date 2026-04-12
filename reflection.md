# 🎼 Music Recommender Reflection

## Profile Comparisons

Comparing different user profiles helped me understand how the "VibeEngine" algorithm translates human preferences into numerical scores.

### High-Energy Pop vs. Chill Lofi
The **High-Energy Pop** profile consistently pulled tracks like "Sunrise City" because they hit the "trifecta": matching genre (pop), happy mood, and high energy (0.8+). In contrast, the **Chill Lofi** profile shifted the recommendations toward tracks like "Library Rain," which have very high "acousticness" (0.86) and much lower energy (0.35). This makes sense because our algorithm treats "energy" and "acousticness" as opposing forces for these two distinct vibes.

### Deep Intense Rock vs. High-Energy Pop
Both of these profiles like high energy, which is why a song like **"Gym Hero"** (an intense pop track) showed up in both lists. However, the **Deep Intense Rock** profile gave "Storm Runner" a higher score because it matched the "Rock" genre and "Intense" mood, while also being much faster (152 BPM vs. 132 BPM). This shows that the system can distinguish between different types of "loud" music using small details like tempo.

### High-Energy Pop vs. Conflicting Preferences (Adversarial)
The **High-Energy Pop** profile is "easy" for the system because its categories match its sound. But for the **Conflicting Preferences** user (who asked for "Ambient" music but with "High Energy"), the system struggled. Originally, it chose "Rainy Window" (a slow, quiet song) just because it was labeled "Ambient." After I shifted the weights, the system correctly prioritized high-energy tracks like "Storm Runner" even though they weren't the right genre. This highlights that "feeling" or "energy" can sometimes be more important than a genre label.

## Why "Gym Hero" Shows Up for Everyone
If you're wondering why "Gym Hero" appears even when you just want "Happy Pop," it's because that song is a "statistical powerhouse." It has very high energy (0.93) and a high danceability score (0.88). In a small catalog of only 20 songs, if the system can't find an exact match for your specific mood, it defaults to these "strong" songs that have high values in popular categories, making them appear like a safe "best guess" for many different types of users.
