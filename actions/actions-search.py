from actions.actions import *

class ActionSearchEstabelecimentos(Action):

    def name(self) ->  Text:
        return "action_search_estabelecimentos"
    
    def findByName(self,name):
        name = name.lower()
        map = {
            "sorveteria": "sorveteria 1, sorveteria 2, sorveteria 3, sorveteria 4",
            "farmacia":  "farmacias 1, farmacias 2, farmacias 3, farmacias 4",
            "farmacias":  "farmacias 1, farmacias 2, farmacias 3, farmacias 4",
            "restaurante": "restaurante 1, restaurante 2, restaurante 3, restaurante 4"}
        message = map.get(name)
        if not message:
            message = Error.ESTABELECIMENTO_NOTFOUND
        return message

    def run(self, 
            dispatcher:  CollectingDispatcher,
            tracker:  Tracker,
            domain:  Dict[ Text,  Any]) ->  List[ Dict[ Text,  Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)
        estabelecimento = ''
        for e in entities:
            if e['entity'] == 'categoria_estabelecimentos':
                estabelecimento = e['value']   

        message = self.findByName(estabelecimento)
        dispatcher.utter_message(text=message)

        return []


class ActionSearchProdutos( Action):

    def name(self) ->  Text:
        return "action_search_produtos"
    
    def api(self, estabelecimento) ->  Text:
        apiResponse = "salada, pizza, xis cebola, xis salada, bauru 4 queijos, bauro filé"
        return apiResponse

    def run(self, dispatcher:  CollectingDispatcher,
            tracker:  Tracker,
            domain:  Dict[ Text,  Any]) ->  List[ Dict[ Text,  Any]]:

        entities = tracker.latest_message['entities']
        print(entities)
        
        produto = ''
        estabelecimento =''
        message = ''

        for e in entities:
            if e['entity'] == 'produtos': 
                produto = e['value']

            if e['entity'] == 'estabelecimento_lancheria':
                estabelecimento = e['value']

            if produto == "cardapio":
                cardapioApi = ' ' + self.api(estabelecimento)
                message = "Cardapio" + " " + cardapioApi

    
        dispatcher.utter_message(text=message)

        return []


class ActionSearchTelefone(Action):

    def name(self) ->  Text:
        return "action_search_telefone"
    
    def findTelefoneByEstabelecimento(self,name):
        name = name.lower()
        print(name)
        lancherias = {
            "famintos": "987487932",
            "altas horas":  "55532564122",
            "elião":  "32552060",
            "pajador": "4453221456"}
        message = name + ' ' + lancherias.get(name)
        if not message:
            message = Error.ESTABELECIMENTO_NOTFOUND
        return message

    def findAllTelefoneByCategoria(self,name):
        lancherias = {
            "famintos": "987487932",
            "altas horas":  "55532564122",
            "elião":  "32552060",
            "pajador": "4453221456"}
        message = json.dumps(lancherias)
        return message
            
    def run(self, 
            dispatcher:  CollectingDispatcher,
            tracker:  Tracker,
            domain:  Dict[ Text,  Any]) ->  List[ Dict[ Text,  Any]]:
        
        print("Search telefone")
        entities = tracker.latest_message['entities']
        print(entities)
        message = ''
        ok = False
        for e in entities:
            if e['entity'] == 'estabelecimento_lancheria':
                lancheria = e['value']   
                message = self.findTelefoneByEstabelecimento(lancheria)

            if e['entity'] == 'categoria_estabelecimentos':
                categoria = e['value']
                message = self.findAllTelefoneByCategoria(categoria)
            print(message)
        

            dispatcher.utter_message(text=message)

        return []
