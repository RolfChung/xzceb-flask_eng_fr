import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText, lgt=language_translator):
        # lt_2 = eval(lt)
        translation_response_fr = \
        lgt.translate(text=englishText, model_id='en-fr')
        translation_fr=translation_response_fr.get_result()
        frenchText = translation_fr['translations'][0]['translation']
        return frenchText

def frenchToEnglish(frenchText, lgt=language_translator):
        translation_response_fr_engl = \
        language_translator.translate(\
        text=frenchText, model_id='fr-en')
        translation_fr_engl=translation_response_fr_engl.get_result()
        englishText =translation_fr_engl['translations'][0]['translation']
        return englishText




