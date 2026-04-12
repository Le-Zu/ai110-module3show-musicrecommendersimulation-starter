import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV file and returns a list of dictionaries with numerical types converted."""
    songs = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numerical types
                row['id'] = int(row['id'])
                row['energy'] = float(row['energy'])
                row['tempo_bpm'] = float(row['tempo_bpm'])
                row['valence'] = float(row['valence'])
                row['danceability'] = float(row['danceability'])
                row['acousticness'] = float(row['acousticness'])
                songs.append(row)
    except FileNotFoundError:
        print(f"Error: File {csv_path} not found.")
    
    print(f"Successfully loaded {len(songs)} songs from {csv_path}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates a relevance score and match reasons for a song based on user preferences."""
    score = 0.0
    reasons = []

    # 1. Genre Match (+2.0)
    fav_genres = user_prefs.get('favorite_genres', [])
    if not isinstance(fav_genres, list): fav_genres = [fav_genres]
    if 'genre' in user_prefs: fav_genres.append(user_prefs['genre'])
    
    if song['genre'] in fav_genres:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # 2. Energy Similarity (+2.0)
    target_energy = user_prefs.get('target_energy', user_prefs.get('energy'))
    if target_energy is not None:
        energy_score = 2.0 * (1.0 - abs(song['energy'] - target_energy))
        score += energy_score
        reasons.append(f"energy alignment (+{energy_score:.2f})")

    # 3. Mood Match (+1.5)
    fav_moods = user_prefs.get('favorite_moods', [])
    if not isinstance(fav_moods, list): fav_moods = [fav_moods]
    if 'mood' in user_prefs: fav_moods.append(user_prefs['mood'])
    
    if song['mood'] in fav_moods:
        score += 1.5
        reasons.append("mood match (+1.5)")

    # 4. Acousticness Similarity (+1.5)
    target_acoustic = user_prefs.get('target_acousticness', user_prefs.get('acousticness'))
    if target_acoustic is not None:
        acoustic_score = 1.5 * (1.0 - abs(song['acousticness'] - target_acoustic))
        score += acoustic_score
        reasons.append(f"acoustic texture (+{acoustic_score:.2f})")

    # 5. Valence Similarity (+1.0)
    target_valence = user_prefs.get('target_valence', user_prefs.get('valence'))
    if target_valence is not None:
        valence_score = 1.0 * (1.0 - abs(song['valence'] - target_valence))
        score += valence_score
        reasons.append(f"mood positivity (+{valence_score:.2f})")

    # 6. Tempo Similarity (+0.5)
    target_tempo = user_prefs.get('target_tempo_bpm', user_prefs.get('tempo_bpm'))
    if target_tempo is not None:
        tempo_diff = abs(song['tempo_bpm'] - target_tempo)
        tempo_score = max(0, 0.5 * (1.0 - (tempo_diff / 100.0)))
        score += tempo_score
        reasons.append(f"tempo alignment (+{tempo_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores, ranks, and returns the top k recommended songs for the given user profile."""
    # Score all songs and format explanations
    scored_list = [
        (song, *score_song(user_prefs, song)) 
        for song in songs
    ]
    
    # Convert reasons list to string and prepare final format
    results = [
        (song, score, ", ".join(reasons))
        for song, score, reasons in scored_list
    ]
    
    # Sort by score (index 1) descending and return top K
    return sorted(results, key=lambda x: x[1], reverse=True)[:k]
