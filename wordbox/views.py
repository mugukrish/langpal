from django.shortcuts import render, redirect
import requests
import json
from django.http import JsonResponse
from .models import GlobalMeaningModel, UserMeaningHistory


# Create your views here.

def returnmeaningview(request):
    context = {'object':{}}
    

    if 'meaning_to_search' in request.GET:
        word = request.GET['meaning_to_search'].strip()
        try:
            final_meaning_data = GlobalMeaningModel.objects.get(word=word)
            context = {'object': json.loads(final_meaning_data.meaning)}
            print('got from database')
            return render(request, 'wordbox/meaning.html', context)
        except Exception as ex:
            print(ex)

        
        final_meaning_data = {}
        context = {'object': final_meaning_data}
        new_one = True
        all_meanings = []
        endpoint = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+word
        get_request = requests.get(endpoint).json()

        for item in get_request:
            #if no data found then a resolution dict is passed
            if 'resolution' in get_request:
                final_meaning_data['title'] = get_request.get('title')            
                final_meaning_data['message'] = get_request.get('message')            
                final_meaning_data['resolution'] = get_request.get('resolution') 
                return render(request, 'wordbox/meaning.html', context)
            else:          
                #return render(request, 'wordbox/meaning.html', context = {'object':'this came to else'})
                #phonetics is a list of dict
                if new_one:
                    phonetics = item.get('phonetics') 
                    if phonetics:
                        for phonetics_data in phonetics:
                            final_meaning_data['text'] = phonetics_data.get('text')
                            final_meaning_data['audio'] = phonetics_data.get('audio')
                            if phonetics_data.get('text'):
                                new_one = False
                
                #meanings is a list of dict
                meanings_data = item.get('meanings')

                if meanings_data:
                    for meaning_details in meanings_data:
                        definitions = meaning_details.get('definitions')
                        if definitions:
                            for definition in definitions:
                                all_meanings.append({'partsofspeech':meaning_details.get('partOfSpeech'),
                                                'meaning':definition.get('definition')})

            final_meaning_data['meanings'] = all_meanings
            try:
                to_save = GlobalMeaningModel.objects.create(word=word, meaning=json.dumps(final_meaning_data))
                to_save.save()

                history_store = UserMeaningHistory.objects.create(user=request.user, word_searched=word)
                history_store.save()
                
            except Exception as ex:
                print(ex)

    return render(request, 'wordbox/meaning.html', context)

''' 

'meanings': [{'partOfSpeech': 'noun', 'definitions': [{'definition': 'A being such as a monotheistic God: a single divine creator and ruler of the universe.', 'synonyms': [], 'antonyms': []}], 
'synonyms': [], 'antonyms': []} , 

{'partOfSpeech': 'proper noun', 
'definitions': [{'definition': 'The single deity of various monotheistic religions, especially the deity of Judaism, Christianity, and Islam.', 'synonyms': [], 'antonyms': [], 
'example': 'Dawn believes in God, but Willow believes in multiple gods and goddesses.'}, {'definition': 'The single male deity of various bitheistic or duotheistic religions.', 'synonyms': [], 'antonyms': []}], 'synonyms': [], 'antonyms': []}

{'partOfSpeech': 'noun', 'definitions': [{'definition': 'A deity or supreme being; a supernatural, typically immortal, being with superior powers, to which personhood is attributed.', 'synonyms': [], 'antonyms': [], 'example': 'The most frequently used name for the Islamic god is Allah.'}, {'definition': 'An idol.', 'synonyms': [], 'antonyms': [], 'example': 'Leo Messi is my god!'}, {'definition': 'A person in a high position of authority, importance or influence.', 'synonyms': [], 'antonyms': []}, {'definition': 'A powerful ruler or tyrant.', 'synonyms': [], 'antonyms': []}, {'definition': 'An exceedingly handsome man.', 'synonyms': [], 'antonyms': [], 'example': 'Lounging on the beach were several Greek gods.'}, {'definition': 'The person who owns and runs a multi-user dungeon.', 'synonyms': [], 'antonyms': []}], 'synonyms': [], 'antonyms': []}, {'partOfSpeech': 'verb', 'definitions': [{'definition': 'To idolize.', 'synonyms': [], 'antonyms': []}, {'definition': 'To deify.', 'synonyms': [], 'antonyms': []}], 'synonyms': [], 'antonyms': []}], 
'license': {'name': 'CC BY-SA 3.0', 'url': 'https://creativecommons.org/licenses/by-sa/3.0'}, 'sourceUrls': ['https://en.wiktionary.org/wiki/God', 'https://en.wiktionary.org/wiki/god']}]

'''