import os
import io

from google.oauth2 import service_account

from google.cloud.speech_v1 import types
from google.cloud.speech_v1 import enums
from google.cloud import speech
# from google.cloud.proto.speech.v1.cloud_speech_pb2 import RecognitionConfig
# from google.cloud.proto.speech.v1.cloud_speech_pb2 import RecognitionAudio
import google.cloud.proto.speech.v1.cloud_speech_pb2_grpc


def return_recognized(PATH, words):
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    SERVICE_ACCOUNT_FILE = 'C:/Users/Janek/PycharmProjects/test/klucz.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = speech.SpeechClient(credentials=credentials)

    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        PATH)

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='pl-PL', speech_contexts =[speech.types.SpeechContext(phrases=words)])

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    transcribed = {}

    for result in response.results:
       # print('Transcript: {}, {}'.format(result.alternatives[0].transcript, result.alternatives[0].confidence))
        transcribed[result.alternatives[0].transcript] = result.alternatives[0].confidence

    return transcribed
"""
import os
import io
from google.cloud import speech_v1
from google.oauth2 import service_account
import google.cloud.speech_v1
from google.cloud.speech_v1 import types
from google.cloud.speech_v1 import enums
from google.cloud.proto.speech.v1.cloud_speech_pb2 import SpeechContext
# from google.cloud.proto.speech.v1.cloud_speech_pb2 import RecognitionConfig
# from google.cloud.proto.speech.v1.cloud_speech_pb2 import RecognitionAudio
import google.cloud.proto.speech.v1.cloud_speech_pb2_grpc


def return_recognized(PATH):
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    SERVICE_ACCOUNT_FILE = 'C:/Users/Janek/PycharmProjects/test/klucz.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = speech_v1.SpeechClient(credentials=credentials)

    phrases = ["tak"]
    context = SpeechContext()

    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        PATH)

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='pl-PL', SpeechContext=context)

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}, {}'.format(result.alternatives[0].transcript, result.alternatives[0].confidence))
        transcribed = result.alternatives[0].transcript

    return transcribed """
