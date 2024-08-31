import re
import logging
from transformers import pipeline

# Initialize the pipeline with T5 for text generation
nlp = pipeline("text2text-generation", model="t5-small")

def process_natural_language_query(query: str):
    try:
        # Use the NLP model to generate a response
        response = nlp(query, max_length=50, do_sample=False)
        processed_query = response[0]['generated_text']
        logging.info(f"Generated text: {processed_query}")

        # Initialize variables for parsed values
        min_passing_yards = None
        min_passing_tds = None

        # Example regex-based parsing for custom labels
        if "passing yards" in processed_query.lower():
            passing_yards_match = re.search(r'(\d+)\s*passing yards', processed_query, re.IGNORECASE)
            if passing_yards_match:
                min_passing_yards = int(passing_yards_match.group(1))
        if "passing tds" in processed_query.lower() or "passing touchdowns" in processed_query.lower():
            passing_tds_match = re.search(r'(\d+)\s*passing tds?', processed_query, re.IGNORECASE)
            if passing_tds_match:
                min_passing_tds = int(passing_tds_match.group(1))

        logging.info(f"Extracted parameters: min_passing_yards={min_passing_yards}, min_passing_tds={min_passing_tds}")

        return {
            "min_passing_yards": min_passing_yards,
            "min_passing_tds": min_passing_tds
        }
    except Exception as e:
        logging.error(f"Error processing query: {e}")
        return {}
