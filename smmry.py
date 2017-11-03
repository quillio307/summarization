from rake_nltk import Rake

transcript = [
    {'rank':0, 'name': "Ammar", 'transcription': "Hi Anoop, so today we are going to discuss the ins and out of text summarization. Before I begin, I would like to clarify that we will be using python for this meeting. No other language should be used because it will be the worst decision we ever make."},
    {'rank':0, 'name': "Anoop", 'transcription': "I don't agree with you. Python is great, but there are so many other languages we could be using. For example nodejs is a pretty good language I have heard. It is known as one of the best newest language ever."},
    {'rank':0, 'name': "Ammar", 'transcription': "Nodejs is really bad for machine learning work. There is no way to realistically implement something like a neural net. Python uses C bindings which is one of the most powerful features."},
    {'rank':0, 'name': "Anoop", 'transcription': "At least we can agree that Ruby sucks."},
    {'rank':0, 'name': "Ammar", 'transcription': "Yes, this we can agree on."}
]

text = ""

for t in transcript:
    text += "{0}: {1}\n".format(t['name'], t['transcription'])

r = Rake()  # initializes Rake with English (all punc) as default lang
r.extract_keywords_from_text(text)
topic_data=r.get_ranked_phrases_with_scores()

for topic in topic_data:
    if topic[0] < 5:
        topic_data.remove(topic)

for topic in topic_data:
    for ts in transcript:
        if topic[1] in ts['transcription']:
            ts['rank'] += topic[0]
arr = sorted(transcript, key=lambda k: k['rank'])
print(arr[-1:] )
print(arr[-2:])
# need to save tags into database (field already exists)
# need to correctly format tags page
# need to connect function to transcript saved in database for retreived meeting
# need to do a little more research into RAKE_NLTK --> remove punctuation from keywords
# write algorithm to only return highest-ranked keywords (tbd)