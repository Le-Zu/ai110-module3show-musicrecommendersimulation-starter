"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Define test profiles
    test_profiles = [
        {
            "name": "High-Energy Pop",
            "prefs": {"favorite_genres": ["pop"], "favorite_moods": ["happy"], "target_energy": 0.9, "target_valence": 0.8}
        },
        {
            "name": "Chill Lofi",
            "prefs": {"favorite_genres": ["lofi"], "favorite_moods": ["chill"], "target_energy": 0.3, "target_acousticness": 0.8}
        },
        {
            "name": "Deep Intense Rock",
            "prefs": {"favorite_genres": ["rock", "metal"], "favorite_moods": ["intense", "aggressive"], "target_energy": 0.9, "target_tempo_bpm": 160}
        },
        {
            "name": "Conflicting Preferences (Adversarial)",
            "prefs": {"favorite_genres": ["ambient"], "favorite_moods": ["melancholic"], "target_energy": 0.9}
        }
    ]

    for profile in test_profiles:
        name = profile["name"]
        user_prefs = profile["prefs"]
        
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "="*50)
        print(f" 🎧 TOP RECOMMENDATIONS FOR: {name} 🎧")
        print("="*50 + "\n")

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   ✨ Final Relevance Score: {score:.2f} / 8.5")
            print(f"   💡 Why: {explanation}")
            print("-" * 50)
    
    print("\nHappy Listening! 🎵\n")


if __name__ == "__main__":
    main()
