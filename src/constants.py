EMBEDDINGS_SIZE = 768
QUERIES_TO_USE_CACHE = 8
NUM_MAX_WORDS = 380 - 1
# this model has a max input tokens of 512, so it's about 380 words
EMBEDDINGS_FILENAME = "clothes-embeddings-2.ann"
DEFAULT_EMBEDDINGS_PATH = f"assets/{EMBEDDINGS_FILENAME}"
EMBEDDINGS_S3_URI = f"https://test-dbetm-lifecycle.s3.us-west-2.amazonaws.com/to_keep/{EMBEDDINGS_FILENAME}"
TOP_N = 6

# FRONT-END
NUMBER_COLS = 2