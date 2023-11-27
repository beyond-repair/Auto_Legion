# Auto_Legion/superagi_integration.py
from superagi_sdk import SuperAGI

class SuperAgiIntegration:
    def __init__(self, api_key):
        self.superagi = SuperAGI(api_key)

    def process_input(self, input_data):
        result = self.superagi.process(input_data)
        return result
