# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

## 2. Intended Use  

VibeMatch is a classroom exploration tool designed to teach how recommendation algorithms work. It takes a user's genre, mood, and vibe preferences (energy level, tempo, danceability, etc.) and suggests the top 5 songs that match. It assumes users can describe their taste in simple terms and want to understand *why* each song got recommended. It is **not** for real production use—it's for learning.

## 3. How the Model Works  

VibeMatch scores each song against your taste by adding up points:
- **Genre match**: +2.0 points if the song is your favorite genre
- **Mood match**: +1.0 point if the song matches your mood (happy, chill, intense, etc.)
- **Numeric matching**: For energy, tempo, valence, danceability, and acousticness, we measure how close each song is to your target. A song that perfectly matches your energy level gets full points; one that's far off gets fewer points.

The system adds all these together to get a final score, then ranks songs from highest to lowest and shows you the top 5. You also see the breakdown of points so you understand why each song was recommended.

## 4. Data  

We use 18 songs across 14 genres. The dataset expanded from a starter set of 10 songs—we added 8 new tracks to get more diversity. Each song has 10 features: ID, title, artist, genre, mood, energy (0–1 scale), tempo (BPM), valence, danceability, and acousticness. **The dataset is imbalanced**: pop and lofi have 5 songs combined, while jazz, classical, metal, and hip-hop each have only 1 song. This means fans of underrepresented genres won't get great recommendations.

## 5. Strengths  

**Works well for**: People who like pop, lofi, or rock—these genres are well-represented in the data. **Explainability**: Every recommendation comes with a score breakdown, so you know exactly why each song was picked. **Numeric matching**: The system does a good job capturing trade-offs—if you want high energy but low acousticness and high danceability, it finds songs that balance those traits. **Mood + genre alignment**: When a song matches both your genre and mood preferences, the recommendations feel intuitive and right.

## 6. Limitations and Bias 

**Genre Dominance Creates a Hard Barrier**: The +2.0 point bonus for exact genre matching severely limits cross-genre discovery. In tests, the High-Energy Pop profile recommended non-pop songs (Sunset Bazaar, Tidal Hearts, Rooftop Lights) only when they had near-perfect numeric matches for energy and danceability. When we doubled the energy weight in an experiment, these songs gained only marginal score improvements because genre matching still dominated. This suggests that in a larger dataset with more pop options available, the system would likely exclude cross-genre recommendations entirely, filtering out serendipitous discoveries and locking users into echo chambers.

**Sparse Genre Representation Distorts Results**: The 18-song dataset has severe imbalances—pop and lofi dominate with 5 songs combined, while jazz, classical, metal, and hip-hop each have only 1 song. This forces niche genre fans to accept numeric matches from unrelated genres rather than getting true genre-based recommendations. A jazz lover would see Coffee Shop Stories (the only jazz track) ranked with lofi and pop alternatives, rather than discovering more jazz options.

**Inconsistent Feature Scaling Silences Tempo Preferences**: Tempo uses a scale of 120.0 BPM while energy uses 1.0, making tempo roughly 120x less impactful than energy in the scoring. A user who specifically wants fast music at 90 BPM gets severely penalized for 20 BPM variance, but this penalty is mathematically equivalent to the energy penalty for a 0.15 difference—yet feels unintentionally weak. This disproportionately disadvantages tempo-focused listeners and rhythm-sensitive users.

---

## 7. Evaluation  

**Profiles Tested**: We tested three main user types—High-Energy Pop (someone who wants upbeat, happy pop music), Chill Lofi (someone who wants calm, focused study music), and Deep Intense Rock (someone who wants powerful, driving rock). We also tested three "edge case" profiles with conflicting preferences: someone who wants sad music but at high energy, someone who wants fast acoustic songs that are calm, and someone who weights genre so heavily it dominates all other preferences.

**What Surprised Us**: The most interesting finding was why "Gym Hero" kept showing up for people looking for "Happy Pop" music, even though the song has an "intense" mood, not "happy." It turns out the system gave it +2 points just for being pop (the right genre), and that advantage was so strong that it placed second even though the mood didn't match at all. The song *is* energetic and danceable, which helped, but the real shock was realizing that genre matching alone could override the mood preference entirely. This made us realize that if we wanted recommendations to truly respect what people ask for, we'd need to either make genre less powerful or require *both* genre and mood matches.

**What We Ran**: We conducted a direct comparison test where we doubled how much the system cares about "energy" and cut genre importance in half. We expected this would let reggaeton and afrobeat songs rank higher for pop fans. Instead, the top 5 songs stayed the same—only the scores changed slightly. This taught us that with a small dataset, genre dominance is so strong that it's almost impossible to break out of it, which has real implications for diversity in recommendations.

---

## 8. Future Work  

1. **Fix tempo scaling**: Right now, tempo is scaled by 120, which makes it 120x weaker than energy. We'd normalize both to the same range so tempo preferences get fair weight.
2. **Add diversity penalties**: After picking the top song, subtract points from similar songs so the top-5 doesn't end up all pop or all lofi.
3. **Expand the dataset**: Test with 100+ songs to see if genre dominance gets worse and to give niche genre fans real choices.
4. **Make genre optional**: Add a user preference for "strict genre match" vs. "genre flexibility" so people can ask for cross-genre recommendations.
5. **Implement OOP interface**: Finish the Recommender class methods so the system can run automated tests.

---

## 10. Intended Use and Non-Intended Use

**DO use VibeMatch for:**
- Learning how recommender algorithms score and rank items
- Understanding music taste as numeric features + categories
- Exploring how weighting decisions shape recommendations
- Classroom projects and teaching bias/fairness in AI
- Experimenting with different preference profiles

**DO NOT use VibeMatch for:**
- Real music streaming services (too small, too simple, too biased)
- Making actual music purchase decisions (sample size is too tiny)
- Recommending music to diverse users (lacks representation for many genres)
- Production deployments (no error handling, no scalability)
- Users who expect state-of-the-art recommendations (this is a teaching tool)

## 9. Personal Reflection  

**My Biggest Learning**: I started this project thinking that "good recommendations" meant matching as many features as possible. What surprised me was discovering that **the *weighting* between features matters far more than which features you choose**. A single +2.0 point bonus for genre created an invisible wall that no amount of numeric tuning could break through. This taught me that recommender systems aren't neutral—every number you write down is a design choice that shapes whose preferences get served. The moment I realized "Gym Hero" (intense mood) was ranking second for users who explicitly asked for "happy" music just because it's pop... that's when I understood that algorithms encode values, not just math.

**Working with AI Tools**: Having an AI to quickly run experiments and test hypotheses was invaluable. I'd say "What if we double the energy weight?" and within seconds I had results showing it barely changed the top-5. This let me iterate fast. However, I had to be careful to *interpret* the results myself—the AI ran the code, but I had to ask the hard questions like "Why did this not work the way I expected?" When the tempo scaling bug appeared (120.0 vs 1.0), the AI could explain what it did, but it took human judgment to realize it was a *problem*, not just a quirk. I also had to double-check the bias analysis—I generated hypotheses, but only by running actual test profiles could I confirm they were real.

**The Surprising Power of Simple Numbers**: What amazed me is that you can build something that *feels* like a real recommendation engine with just six lines of scoring logic. Adding +2 for genre match and +1 for mood match, plus five numeric features... it's absurdly simple. Yet it immediately revealed startling truths about trade-offs: Can you want both "fast" and "acoustic"? The system said no. Can you like reggaeton if you asked for pop? Not if pop songs exist. It's a humbling lesson that even toy algorithms reflect real decisions about whose tastes matter.

**What I'd Try Next**: 
1. **Fix the tempo scale** (use 60–170 range instead of hardcoding 120) and **rerun all experiments**—I suspect this alone would reshape recommendations.
2. **Add a diversity constraint**: After picking the top song, subtract points from similar songs so the top-5 isn't all pop or all lofi.
3. **Test with 100+ songs** to see if the filter bubble effect gets worse (my hypothesis: yes).
4. **Make genre optional**: Add a user preference for "strict genre match" vs. "genre flexibility" so cross-genre explorers aren't punished.
5. **Implement the Recommender class methods** properly so the OOP interface works—right now they're stubs, but I'd love to plug this into tests and see if it scales to real data.  
