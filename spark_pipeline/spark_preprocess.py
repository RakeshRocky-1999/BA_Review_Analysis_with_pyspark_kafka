from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def normalize_for_spark(text):
    import re
    import unicodedata
    import contractions
    import string
    import nltk

    from nltk.tokenize import wordpunct_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer

    # Download inside worker (safe for first call, idempotent)
    nltk.download("stopwords", quiet=True)
    nltk.download("punkt", quiet=True)
    nltk.download("wordnet", quiet=True)

    # Step-by-step exactly like your notebook
    try:
        def tokenize_text(text):
            return wordpunct_tokenize(text)

        def remove_non_ASCII_before(text):
            new_text = []
            for i in text:
                normalized_text = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore').decode('utf-8', 'ignore')
                new_text.append(normalized_text)
            return ' '.join(new_text)

        def separate_verification(review):
            return review.split('|')

        def remove_verified(text_list):
            irrelevant_list = ['Not Verified', 'Trip Verified']
            new_text = []
            for i in text_list:
                cleaned = i.strip()
                if cleaned not in irrelevant_list and cleaned.lower() not in ['trip verify', 'not verify']:
                    new_text.append(cleaned)
            return ' '.join(new_text)

        def replace_contractions(text):
            return contractions.fix(text)

        def remove_numbers(text):
            return re.sub(r'\d+', '', text)

        def remove_space(text):
            return re.sub(r'\s+', ' ', text)

        def punctuatin_remove(text):
            return text.translate(str.maketrans('', '', string.punctuation))

        def remove_punctuation(text):
            return [re.sub(r'[^\w\s]', '', word) for word in text]

        def remove_non_ASCII(text):
            return [unicodedata.normalize('NFKD', i).encode('ascii', 'ignore').decode('utf-8', 'ignore') for i in text]

        def lower_case(text):
            return [i.lower() for i in text]

        def remove_stopwrods(text):
            return [i for i in text if i not in stopwords.words('english')]

        def lemmatization(text):
            lemmatizer = WordNetLemmatizer()
            return [lemmatizer.lemmatize(i, pos='v') for i in text]

        # === Pipeline ===
        text = tokenize_text(text)
        text = remove_non_ASCII_before(text)
        text = separate_verification(text)
        text = remove_verified(text)
        text = replace_contractions(text)
        text = remove_numbers(text)
        text = remove_space(text)
        text = punctuatin_remove(text)
        text = tokenize_text(text)
        text = remove_punctuation(text)
        text = remove_non_ASCII(text)
        text = lower_case(text)
        text = remove_stopwrods(text)
        text = lemmatization(text)

        return ' '.join(text)

    except Exception as e:
        return ""  # return empty if error in UDF

# Define UDF to register with Spark
normalize_udf = udf(normalize_for_spark, StringType())
