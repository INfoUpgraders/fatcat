import requests

class Server:
    def __init__(self, url:str, text:bool=True, plain:bool=False):
        self.url = url
        self.text = text
        self.plain = plain

    def total_memory(self):
        response = requests.get(self.url + "meminfo")
        data = response.json()['data']
        if self.text == True and self.plain == False:
            total_memory = f"{round(int(data['MemTotal'])/1e+6, 2)} GB"
            return total_memory
        elif self.text == True and self.plain == True:
            total_memory = f"{data['MemTotal']} KB"
            return total_memory
        elif self.text == False and self.plain == True:
            total_memory = int(data['MemTotal'])
            return total_memory
        elif self.text == False and self.plain == False:
            total_memory = float(round(int(data['MemTotal'])/1e+6, 2))
            return total_memory
        else:
            raise Exception("text or plain type is not supported.")

        # total_memory = float(round(int(data['MemTotal'])/1e+6, 2))

    def free_memory(self):
        try:
            response = requests.get(self.url + "meminfo")
            data = response.json()['data']
            total_memory = float(round(int(data['MemFree'])/1e+6, 2))
            return total_memory
        except:
            return "-"

    def available_memory(self):
        try:
            response = requests.get(self.url + "meminfo")
            data = response.json()['data']
            total_memory = float(round(int(data['MemAvailable'])/1e+6, 2))
            return total_memory
        except:
            return "-"

    def cached_memory(self):
        try:
            response = requests.get(self.url + "meminfo")
            data = response.json()['data']
            total_memory = float(round(int(data['Cached'])/1e+6, 2))
            return total_memory
        except:
            return "-"

    def active_memory(self):
        try:
            response = requests.get(self.url + "meminfo")
            data = response.json()['data']
            total_memory = float(round(int(data['Active'])/1e+6, 2))
            return total_memory
        except:
            return "-"

    def inactive_memory(self):
        try:
            response = requests.get(self.url + "meminfo")
            data = response.json()['data']
            total_memory = float(round(int(data['Inactive'])/1e+6, 2))
            return total_memory
        except:
            return "-"

    def swap_total(self):
        try:
            response = requests.get(self.url + "meminfo")
            data = response.json()['data']
            total_memory = float(round(int(data['SwapTotal'])/1e+6, 2))
            return total_memory
        except:
            return "-"
