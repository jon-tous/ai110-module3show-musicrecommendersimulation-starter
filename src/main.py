"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


USER_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.88,
        "target_tempo_bpm": 128,
        "target_valence": 0.82,
        "target_danceability": 0.86,
        "target_acousticness": 0.20,
        "genre_points": 2.0,
        "mood_points": 1.0,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.38,
        "target_tempo_bpm": 78,
        "target_valence": 0.60,
        "target_danceability": 0.58,
        "target_acousticness": 0.82,
        "genre_points": 2.0,
        "mood_points": 1.0,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "target_tempo_bpm": 150,
        "target_valence": 0.44,
        "target_danceability": 0.62,
        "target_acousticness": 0.12,
        "genre_points": 2.0,
        "mood_points": 1.0,
    },
}

ADVERSARIAL_PROFILES = {
    "Sad but High Energy": {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.90,
        "target_tempo_bpm": 140,
        "target_valence": 0.20,
        "target_danceability": 0.85,
        "target_acousticness": 0.10,
        "genre_points": 2.0,
        "mood_points": 1.0,
    },
    "Fast but Acoustic and Calm": {
        "favorite_genre": "folk",
        "favorite_mood": "serene",
        "target_energy": 0.20,
        "target_tempo_bpm": 165,
        "target_valence": 0.55,
        "target_danceability": 0.20,
        "target_acousticness": 0.95,
        "genre_points": 2.0,
        "mood_points": 1.0,
    },
    "Genre Overpower": {
        "favorite_genre": "lofi",
        "favorite_mood": "intense",
        "target_energy": 0.90,
        "target_tempo_bpm": 150,
        "target_valence": 0.40,
        "target_danceability": 0.70,
        "target_acousticness": 0.10,
        "genre_points": 6.0,
        "mood_points": 1.0,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs from the dataset.")

    all_profiles = {**USER_PROFILES, **ADVERSARIAL_PROFILES}

    for profile_name, user_prefs in all_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 72)
        print(f"TOP 5 RECOMMENDATIONS: {profile_name}")
        print("=" * 72)

        for index, rec in enumerate(recommendations, start=1):
            # Return format: (song, score, explanation)
            song, score, explanation = rec
            reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

            print(f"\n{index}. {song['title']} ({song['artist']})")
            print(f"   Final Score : {score:.2f}")
            print("   Reasons     :")
            for reason in reasons:
                print(f"   - {reason}")

    print("\n" + "=" * 72)


if __name__ == "__main__":
    main()
