import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    '''Translate English to French'''
    if english_text is not None:
        ret = language_translator.translate(english_text, source='en', target='fr')
        if ret:
            return ret.result['translations'][0]['translation']
    return " "

def french_to_english(french_text):
    #write the code here
    '''Translate French to English'''
    if french_text is not None:
        ret = language_translator.translate(french_text, source='fr', target='en')
        if ret:
            return ret.result['translations'][0]['translation']

    return " "

#print(frenchToEnglish("Bienvenue en France"))
