🤖 Medico Chatbot – Healthcare FAQ Assistant
The Medico Chatbot is a simple, rule-based chatbot that uses Natural Language Processing (NLP) with NLTK to answer user queries based on a dataset of frequently asked questions in the medical domain.

📂 Dataset
The chatbot uses a CSV file named medical.csv with two main columns:

Indent: The user query or keyword.

Reply: The appropriate answer the chatbot should return.

Example:

Indent,Reply
headache,Try to rest and drink plenty of fluids. Consult a doctor if it persists.
fever,Please take paracetamol and monitor your temperature regularly.
...




🔧 Requirements
Install the necessary Python libraries:
!pip install nltk pandas
Download the required NLTK data:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
🧠 How It Works


1. User Input Tokenization and Filtering
Converts user input to lowercase

Tokenizes the sentence

Removes stop words and punctuation
tokens = word_tokenize(user_input.lower())
filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]

2. Matching Against Dataset
Compares filtered tokens with each row's Indent tokens.

If a match is found, it returns the corresponding Reply.
if any(keyword in filtered_tokens for keyword in word_tokenize(rows["Indent"].lower())):
    return rows["Reply"]
🗨️ Chatbot Flow
def chat():
    print("Welcome to the Medico Chatbot! How can I assist you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit', 'bye', ...]:  # multiple ways to exit
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = fetch_response(user_input)
        print("Chatbot:", response)
💬 Example Conversation
User: I have a headache
Chatbot: Try to rest and drink plenty of fluids. Consult a doctor if it persists.

User: What should I do for fever?
Chatbot: Please take paracetamol and monitor your temperature regularly.

User: Bye
Chatbot: Goodbye! Have a great day.


📦 Output
After execution, the chatbot saves the loaded dataset to a pickle file for later use:
faq_df.to_pickle('faq.pkl')




👤 Author
Sachin Sarvesh S C
