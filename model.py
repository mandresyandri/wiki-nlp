from summarizer import Summarizer, TransformerSummarizer

def bert_summarizer(text_data):
    bert_model = Summarizer()
    text_summary = ''.join(bert_model(text_data, min_length=60))
    return text_summary