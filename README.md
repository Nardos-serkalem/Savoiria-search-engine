# **Savoiria Search Engine**
**Savoiria** is derived from the French word "Savoir," which means "knowledge" or "to know." This search engine aims to bring knowledge to users by providing relevant Wikipedia summaries, images, and ranking them based on cosine similarity to the search query.
A custom search engine that fetches relevant Wikipedia summaries, images, and ranks them based on cosine similarity to your search query.

## **Features**

- **Search Wikipedia**: Input any search query, and get relevant Wikipedia summaries and images.
- **Cosine Similarity**: Results are ranked based on the cosine similarity between the query and fetched Wikipedia summaries.
- **Lemmatization**: Text processing is performed using lemmatization to improve the accuracy of the search.
- **Image Support**: Displays images (thumbnails) related to the search results from Wikipedia.

## **Technologies Used**

- **Python**: Flask web framework for backend.
- **scikit-learn**: For TF-IDF vectorization and cosine similarity calculation.
- **Requests**: For API calls to Wikipedia.
- **NLTK**: For lemmatization and text preprocessing.



