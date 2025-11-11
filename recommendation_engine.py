import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_content(expanded_csv="recommendations.csv"):
    """
    Loads the 100k dataset created by generate_data.py and runs an interactive recommendation system.

    Steps:
      1. User picks content type: "Movie" or "Webseries".
      2. Filter dataset accordingly.
      3. Combine text features (genres, keywords, tagline, cast, director).
      4. Build TF-IDF vectors for the filtered set.
      5. Prompt user for a specific title (fuzzy matched).
      6. Compute 1 x N similarity for that single item vs. entire set.
      7. Print top recommendations.
    """

    content_data = pd.read_csv(expanded_csv, engine='python')
    content_data.reset_index(drop=True, inplace=True)

    for col in ['genres','keywords','tagline','cast','director','title','Type']:
        if col not in content_data.columns:
            content_data[col] = ''
        else:
            content_data[col].fillna('', inplace=True)

    user_pref = ""
    while user_pref.lower() not in ["movie", "webseries"]:
        user_pref = input("Enter your preferred content type (Movie/Webseries): ").strip()

    filtered_data = content_data[content_data['Type'].str.lower() == user_pref.lower()].copy()
    if filtered_data.empty:
        print(f"Sorry, no entries found for '{user_pref}'.")
        return

    filtered_data['combined_features'] = (
        filtered_data['genres'] + " " +
        filtered_data['keywords'] + " " +
        filtered_data['tagline'] + " " +
        filtered_data['cast'] + " " +
        filtered_data['director']
    )

    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(filtered_data['combined_features'])

    list_of_titles = filtered_data['title'].tolist()
    print("\nHere are a few titles in the selected category:")
    for idx, title in enumerate(list_of_titles[:10]):
        print(f"{idx+1}. {title}")
        
    user_title = input("\nEnter your favorite title (from the list above or any known title): ").strip()

    close_matches = difflib.get_close_matches(user_title, list_of_titles)
    if not close_matches:
        print("No close match found. Check the spelling and try again.")
        return

    chosen_title = close_matches[0]
    print(f"\nWe matched your input to: {chosen_title}\n")

    row_of_chosen_item = filtered_data[filtered_data['title'] == chosen_title]
    if row_of_chosen_item.empty:
        print("Couldn't locate the chosen title. Please try again.")
        return

    index_of_content = row_of_chosen_item.index[0]

    user_vector = feature_vectors[filtered_data.index.get_loc(index_of_content)] 
    similarity_vector = cosine_similarity(user_vector, feature_vectors).flatten()

    item_sim_scores = list(enumerate(similarity_vector))
    sorted_similar_items = sorted(item_sim_scores, key=lambda x: x[1], reverse=True)

    print("Content recommendations for you:\n")
    rec_count = 0
    for item_idx, score in sorted_similar_items:
        if filtered_data.iloc[item_idx]['title'] == chosen_title:
            continue

        title = filtered_data.iloc[item_idx]['title']
        genres = filtered_data.iloc[item_idx]['genres']
        cast = filtered_data.iloc[item_idx]['cast']
        director = filtered_data.iloc[item_idx]['director']

        print(f"{rec_count+1}. {title}")
        print(f"   Genres  : {genres}")
        print(f"   Cast    : {cast}")
        print(f"   Director: {director}\n")

        rec_count += 1
        if rec_count >= 30:
            break

if __name__ == "__main__":
    print("Running...")
    recommend_content("recommendations.csv")
