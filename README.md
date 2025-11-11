# Global Movie & Webseries Recommendation System

This repository provides a **large-scale content recommendation system** for movies and web series. 

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [1. Generating the Dataset](#1-generating-the-dataset)
  - [2. Running the Recommendation Engine](#2-running-the-recommendation-engine)
- [Dependencies](#dependencies)

---

## Features

- **Large Synthetic Dataset**: Generates 100,000 entries that blend realistic movie and web series titles with diverse genres, casts, directors, and other attributes.
- **Enhanced Diversity**: Minimizes repetition through broad lists of unique titles, actors, and directors.
- **TF-IDF Based Similarity**: Merges metadata (genres, keywords, cast, director, and tagline) into a unified text field, then applies TF-IDF and cosine similarity to find similar content.
- **1 x N Computation**: Computes similarity between the selected item and all others efficiently, avoiding the overhead of a full NxN comparison matrix.

---

## Project Structure

```
├── generate_data.py               # Script to generate the 100K-row dataset
├── recommendation_engine.py       # Script to run the interactive recommendation system
├── final_100k_movies_webseries.csv    # Generated CSV file (after you run generate_data.py)
├── MovieRecommendationSystem.ipynb    # (Optional) Jupyter Notebook version (if any)
├── README.md                      # Project documentation
```

---

## Getting Started

1. **Clone** this repository.
2. Ensure you have a **Python 3.x** environment set up..

---

## Usage

### 1. Dataset Generation

Run:
```bash
python generate_data.py
```

This creates a file called **`final_100k_movies_webseries.csv`** in the same directory, containing 100,000 rows of synthetic data.  

### 2. Recommendation Engine

After generating the dataset, run:
```bash
python recommendation_engine.py
```

The program will:
1. Ask you to choose **Movie** or **Webseries**.  
2. Display some titles from that category.  
3. Ask you to **enter your favorite title**.  
4. Find the closest match.  
5. Compute **cosine similarity** (1 x N) between your chosen item and all others.  
6. Print the **top recommendations** (up to 30).

---

## Dependencies

- **Python 3.x**
- [NumPy](https://pypi.org/project/numpy/)
- [Pandas](https://pypi.org/project/pandas/)
- [scikit-learn](https://pypi.org/project/scikit-learn/)

Install them with:
```bash
pip install -r requirements.txt
```
Or individually:
```bash
pip install numpy pandas scikit-learn
```




