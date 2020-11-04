from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import FollowupAction 
from rasa_sdk.events import UserUttered
class ActionOne(Action):

    def name(self) -> Text:
        return "action_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/1.mp3")


        return []

class ActionOneRebuttle(Action):
    
    def name(self) -> Text:
        return "action_RS_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS1.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/1a.mp3")

        return []

class ActionTwo(Action):

    def name(self) -> Text:
        return "action_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/2.mp3")


        return []
class ActionTwoRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS2.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/2a.mp3")
        return []


class ActionThree(Action):

    def name(self) -> Text:
        return "action_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/3.mp3")

        return []

class ActionThreeRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS3.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/3b.mp3")
        return []


class ActionFour(Action):
    
    def name(self) -> Text:
        return "action_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/4.mp3")

        return []
class ActionFourRebuttle(Action):
    
    def name(self) -> Text:
        return "action_RS_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS4.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/4.mp3")
        return []


class ActionFive(Action):

    def name(self) -> Text:
        return "action_5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/5.mp3")
        return []

class ActionFiveRebuttle(Action):
    
    def name(self) -> Text:
        return "action_RS_5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS5.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/5a.mp3")

        return []


class ActionSix(Action):

    def name(self) -> Text:
        return "action_6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/6_1.mp3")
        return []

class ActionSixRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS6.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/7.mp3")
        return []



class ActionSeven(Action):

    def name(self) -> Text:
        return "action_7"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("email")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/7.mp3")
        return []

class ActionSevenRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_7"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("email")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS7.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/7.mp3")
        return []


class ActionEight(Action):

    def name(self) -> Text:
        return "action_8"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("occupation")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/8.mp3")
        
        return []




class ActionEightRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_8"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("occupation")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS8.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/8.mp3")
        return []

class ActionNine(Action):

    def name(self) -> Text:
        return "action_9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("experience")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/9.mp3")
        return []

class ActionNineRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("experience")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS9.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/9a.mp3")
        return []

class ActionTen(Action):

    def name(self) -> Text:
        return "action_10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("age")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/10.mp3")


        return []

class ActionTenRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("age")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS10.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/10a.mp3")

        return []

class ActionTwelve(Action):

    def name(self) -> Text:
        return "action_12"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/12.mp3")



        return []

class ActionTwelveRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_12"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS12.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/12a.mp3")

        return []

class ActionThirteen(Action):

    def name(self) -> Text:
        return "action_13"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/13.mp3")
   
        return []

class ActionThirteenRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_13"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS13.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/13b.mp3")

        return []



class ActionEleven(Action):

    def name(self) -> Text:
        return "action_11"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/11.mp3")

        return []

class ActionElevenRebuttle(Action):

    def name(self) -> Text:
        return "action_RS_11"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/RS11.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/Recovery_Snippets/11b.mp3")

        return []

class ActionFifteen(Action):

    def name(self) -> Text:
        return "action_15"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("transfer")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/15.mp3")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/16.mp3")
        return []



class ActionBye(Action):

    def name(self) -> Text:
        return "action_14"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/14.mp3")


        return []


class ActionBye(Action):
    
    def name(self) -> Text:
        return "action_bye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("disconnect")


        return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
            
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/final_Script/D.mp3")


class ActionCheckIntentName(Action):
    
    def name(self) -> Text:
        return "action_check_intent_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'not_intrested':
            return [
                UserUttered("/i m not intrested",intent={'name': 'not_intrested', 'confidence': 1.0}),
            ]
        else:
            return [
                UserUttered("well i stopped a long time ago",intent={'name': 'force', 'confidence': 1.0}),
            ]
            

class ActionAcquaintance(Action):

    def name(self) -> Text:
        return "action_acquaintance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/acquaintance.mp3")

        return []


class ActionReal(Action):

    def name(self) -> Text:
        return "action_real"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/real.mp3")

        return []

class ActionInformation(Action):

    def name(self) -> Text:
        return "action_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/information.mp3")

        return []

class ActionLocation(Action):
    
    def name(self) -> Text:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/location.mp3")

        return []

class ActionMyProfession(Action):

    def name(self) -> Text:
        return "action_my_profession"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/my_profession.mp3")

        return []


class ActionVoicemail(Action):

    def name(self) -> Text:
        return "action_Voicemail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("disconnect")

        return []

class ActionRealEstate(Action):
    
    def name(self) -> Text:
        return "action_real_estate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/real_estate.mp3")

        return []

class ActionDuration(Action):

    def name(self) -> Text:
        return "action_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision_final/{voice}/small_talk/duration.mp3")

        return []