import json
import os


class Storage:
    def __init__(self,file:str):
        self.file = file
        FLET_APP_STORAGE_DATA = os.getenv("FLET_APP_STORAGE_DATA")
        if FLET_APP_STORAGE_DATA is None:
            FLET_APP_STORAGE_DATA = os.path.join(os.path.dirname(__file__), f"data")
            os.makedirs(FLET_APP_STORAGE_DATA, exist_ok=True)
        self.COUNTER_FILE_PATH = os.path.join(FLET_APP_STORAGE_DATA, self.file)

    def Set(self,user_data: dict):
        with open(self.COUNTER_FILE_PATH,"w") as file:
            json.dump(user_data , file,indent=2)

    def Get(self) -> dict :
        try:
            with open(self.COUNTER_FILE_PATH,"r") as file:
                data = json.load(file)
            return data
        except:
            self.Set({})

    def Get_Email(self) -> str:
            try:
                with open(self.COUNTER_FILE_PATH,"r") as file:
                    data = json.load(file)["caregiver_email"]
                return data
            except:
                return ""
        
    

    def Get_Caloreis(self) -> float:
        with open(self.COUNTER_FILE_PATH,"r") as file:
            data = json.load(file)["calories"]
        return data
    

    def Rmove_data(self):
        """Delete the storage file"""
        try:
            os.remove(self.COUNTER_FILE_PATH)
            return True
        except FileNotFoundError:
            return False 
        except Exception as e:
            print(f"Error removing file: {e}")
            return False

    

