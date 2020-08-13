from actions import actions

class ActionSearchEstabelecimentos(actions.Action):

    def name(self) -> actions.Text:
        return "action_search_estabelecimentos"

    def run(self, dispatcher: actions.CollectingDispatcher,
            tracker: actions.Tracker,
            domain: actions.Dict[actions.Text, actions.Any]) -> actions.List[actions.Dict[actions.Text, actions.Any]]:

        entities = tracker.latest_message['entities']
        print(entities)
        nome = ''
        message = ''
        for e in entities:
            if e['entity'] == 'estabelecimentos':
                nome = e['value']

            if nome == "farmacias":
                message = "farmacias 1, farmacias 2, farmacias 3, farmacias 4"
            if nome == "restaurantes":
                message = "restaurante 1, restaurante 2, restaurante 3, restaurante 4"

        dispatcher.utter_message(text=message)

        return []



class ActionSearchProdutos(actions.Action):

    def name(self) -> actions.Text:
        return "action_search_produtos"
    
    def api(self, estabelecimento) -> actions.Text:
        apiResponse = "salada, pizza, xis cebola, xis salada, bauru 4 queijos, bauro filé"
        return apiResponse

    def run(self, dispatcher: actions.CollectingDispatcher,
            tracker: actions.Tracker,
            domain: actions.Dict[actions.Text, actions.Any]) -> actions.List[actions.Dict[actions.Text, actions.Any]]:

        entities = tracker.latest_message['entities']
        print(entities)
        
        produto = ''
        estabelecimento =''
        message = ''

        for e in entities:
            if e['entity'] == 'produto': 
                produto = e['value']

            if e['entity'] == 'estabelecimento':
                estabelecimento = e['value']

            if produto == "cardapio":
                cardapioApi = ' ' + self.api(estabelecimento)
                message = "Cardapio" + " " + cardapioApi

    
        dispatcher.utter_message(text=message)

        return []
