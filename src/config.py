from pathlib import Path

# === Project Root ===
# Adjust this if needed depending on where this file lives
ROOT_DIR = Path(__file__).resolve().parents[1]  # Assumes: /src/config.py

# === Data Directories ===
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# === Notebooks Directories ===
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"

# === Models Directories ===
MODELS_DIR = ROOT_DIR / "models"
VADER_MODEL_DIR = MODELS_DIR / "vader"
CARDIFF_MODEL_DIR = MODELS_DIR / "cardiff-roberta"
LDA_MODEL_DIR = MODELS_DIR / "lda"
BERTOPIC_MODEL_DIR = MODELS_DIR / "bertopic"

# === Results Directories ===
RESULTS_DIR = ROOT_DIR / "results"

# Sentiment Analysis Results
SENTIMENT_RESULTS_DIR = RESULTS_DIR / "sentiment-analysis"
VADER_RESULTS_DIR = SENTIMENT_RESULTS_DIR / "vader"
TRANSFORMER_RESULTS_DIR = SENTIMENT_RESULTS_DIR / "cardiff-roberta"

# Topic Modeling Results
TOPIC_RESULTS_DIR = RESULTS_DIR / "topic-modeling"
LDA_RESULTS_DIR = TOPIC_RESULTS_DIR / "lda"
LDA_METRICS_RESULTS_DIR = LDA_RESULTS_DIR / "metrics"
LDA_DOCUMENTS_RESULTS_DIR = LDA_RESULTS_DIR / "documents"
LDA_TOPICS_RESULTS_DIR = LDA_RESULTS_DIR / "topics"
BERTOPIC_RESULTS_DIR = TOPIC_RESULTS_DIR / "bertopic"
BERTOPIC_METRICS_RESULTS_DIR = BERTOPIC_RESULTS_DIR / "metrics"
BERTOPIC_DOCUMENTS_RESULTS_DIR = BERTOPIC_RESULTS_DIR / "documents"
BERTOPIC_TOPICS_RESULTS_DIR = BERTOPIC_RESULTS_DIR / "topics"

# === Figures Directories ===
FIGURES_DIR = ROOT_DIR / "figures"

# Sentiment Analysis Figures
SENTIMENT_FIGURES_DIR = FIGURES_DIR / "sentiment-analysis"
VADER_FIGURES_DIR = SENTIMENT_FIGURES_DIR / "vader"
TRANSFORMER_FIGURES_DIR = SENTIMENT_FIGURES_DIR / "cardiff-roberta"

# Topic Modeling Figures
TOPIC_FIGURES_DIR = FIGURES_DIR / "topic-modeling"
LDA_FIGURES_DIR = TOPIC_FIGURES_DIR / "lda"
BERTOPIC_FIGURES_DIR = TOPIC_FIGURES_DIR / "bertopic"

# Sentiment and Topic Progression Figures
SENTIMENT_TOPIC_DIR = FIGURES_DIR / "sentiment-topic-progression"

# === Book Titles List ===
BOOKS = [
    "this-side-of-paradise",
    "the-beautiful-and-damned",
    "the-great-gatsby"
]

# === Book URLs ===
BOOK_URLS = {
    "this-side-of-paradise": "https://www.gutenberg.org/cache/epub/805/pg805.txt",
    "the-beautiful-and-damned": "https://www.gutenberg.org/cache/epub/9830/pg9830.txt",
    "the-great-gatsby": "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
}

# === Ensure all required directories exist ===
for path in [
    # Data
    RAW_DIR,
    PROCESSED_DIR,
    
    # Models
    VADER_MODEL_DIR,
    CARDIFF_MODEL_DIR,
    LDA_MODEL_DIR,
    
    # Results
    VADER_RESULTS_DIR,
    TRANSFORMER_RESULTS_DIR,
    LDA_RESULTS_DIR,
    LDA_METRICS_RESULTS_DIR,
    LDA_METRICS_RESULTS_DIR, 
    LDA_DOCUMENTS_RESULTS_DIR,
    LDA_TOPICS_RESULTS_DIR,
    BERTOPIC_RESULTS_DIR,
    BERTOPIC_METRICS_RESULTS_DIR,
    BERTOPIC_DOCUMENTS_RESULTS_DIR,
    BERTOPIC_TOPICS_RESULTS_DIR,

        # Figures
    VADER_FIGURES_DIR,
    TRANSFORMER_FIGURES_DIR,
    TOPIC_FIGURES_DIR,
    LDA_FIGURES_DIR, 
    BERTOPIC_FIGURES_DIR
]:
    path.mkdir(parents=True, exist_ok=True)