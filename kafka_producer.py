import streamlit as st
from kafka import KafkaProducer
import json

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda m: json.dumps(m).encode("utf-8")
)

st.title("✍️ British Airways Review Sender")
st.markdown("Write a review and submit it to Kafka for real-time analysis!")

# Session state to manage text clearing
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Function to clear text after submission
def submit_review():
    review_text = st.session_state.review_input
    if review_text.strip():
        message = {"review_text": review_text}
        producer.send("reviews", value=message)
        st.success("✅ Review sent successfully!")
        st.session_state.submitted = True
        st.session_state.review_input = ""  # clear input
    else:
        st.warning("⚠️ Please enter a review.")

# Text area with session state
st.text_area("Your Review", key="review_input", height=100)

# Submit button
st.button("🚀 Submit Review", on_click=submit_review)


# import streamlit as st
# from kafka import KafkaProducer
# import json

# # Kafka setup
# producer = KafkaProducer(
#     bootstrap_servers="localhost:9092",
#     value_serializer=lambda m: json.dumps(m).encode("utf-8")
# )

# st.title("✍️ British Airways Review Sender")
# st.markdown("Write a review and submit it to Kafka for real-time analysis!")

# # Initialize session state
# if "review_input" not in st.session_state:
#     st.session_state.review_input = ""

# # Function to submit review and clear
# def submit_review():
#     review_text = st.session_state.review_input
#     if review_text.strip():
#         message = {"review_text": review_text}
#         producer.send("reviews", value=message)
#         st.success("✅ Review sent successfully!")
#         st.session_state.review_input = ""  # clear the input
#         st.experimental_rerun()  # rerun to reflect the change
#     else:
#         st.warning("⚠️ Please enter a review.")

# # Text area with session state
# st.text_area("Your Review", key="review_input", height=200)

# # Submit button
# st.button("🚀 Submit Review", on_click=submit_review)
