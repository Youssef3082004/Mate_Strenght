from flet import * 

class Frontend:
    BLACK = "#1A1A1A"
    TAN = "#B99A45"

    class Signin_textfeild(TextField):
        def __init__(self,Label:str,prefix_icon,hint_text:str,keyboard_type:KeyboardType = KeyboardType.NONE):
            super().__init__()
            self.label = Label
            self.prefix_icon=prefix_icon
            self.label_style=TextStyle(size=20, weight=FontWeight.W_900, color=Frontend.TAN,font_family="andalus")
            self.border=InputBorder.OUTLINE
            self.border_color=Frontend.BLACK
            self.hint_text=hint_text
            self.hint_style=TextStyle(color=Colors.BLACK54)
            self.hint_fade_duration=1000
            self.text_style=TextStyle(size=15, weight=FontWeight.W_400,font_family="Alex")
            self.keyboard_type=keyboard_type
            