!pip install nltk
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize # Changed word_tokensize to word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
faq_df=pd.read_csv("/medical.csv")
print(faq_df)
def fetch_response(user_input):
  tokens=word_tokenize(user_input.lower())
  stop_words=set(stopwords.words('english'))
  filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
  for index,rows in faq_df.iterrows():
    if any(keyword in filtered_tokens for keyword in word_tokenize(rows["Indent"].lower())):
      return rows["Reply"]
  return "Sorry,we couldn't find a response to your inquiry."
def chat():
  print("Welcome to the Medico Chatbot! How can I assist you today?")
  while True:
    user_input=input("User:")
    if user_input.lower() in[
'exit', 'quit', 'stop', 'bye', 'goodbye', 'end', 'close', 'I’m done', 'That’s all', 'I’m leaving', 'Talk later', 'See you', 'End chat', 'Ctrl + C', '/exit', '/quit', '/stop']:
      print("Chatbot:Goodbye! Have a great day.")
      break
    response=fetch_response(user_input)
    print("Chatbot:",response)

  faq_df.to_pickle('faq.pkl')

chat()
