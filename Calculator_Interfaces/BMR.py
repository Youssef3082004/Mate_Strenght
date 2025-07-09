from flet import * 
from .Calculator import Frontend
from Constant.variables import Variables

class Calculator_BMR(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page 
        self.expand = True
        self.page = page
        self.page.padding = 0
        self.page.window.height = 700
        self.page.window.width = 400
        self.page.window.resizable = False
        self.page.fonts = {"andalus": "font/andalus.ttf", "Alex": "font/Alex.ttf" , "pac":"font/Pacifico-Regular.ttf","Inter":"font/Inter.ttf"}
        self.page.theme = Theme(page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.OPEN_UPWARDS,android=PageTransitionTheme.OPEN_UPWARDS))
        self.page.theme_mode = ThemeMode.LIGHT
        self.page.window.center()
        self.null = Text(" ")
        
        #! ==================================================== Interface Title ==============================================
        self.title_text = Text(value="BMR Score",color=Colors.BLACK54,size=25,font_family="Inter",weight=FontWeight.BOLD)

        #! ==================================================== BMR Score ==============================================
        self.Score_text = Text(value="0",color=Colors.BLACK54,size=80,font_family="Inter",weight=FontWeight.BOLD)
        self.Scorelevel_text = Text(value="Not Calcaulted Yet",color=Colors.BLACK54,size=20,font_family="Inter",weight=FontWeight.BOLD)
        self.scoretext_Row = Row(controls=[self.Score_text],alignment=MainAxisAlignment.CENTER)
        self.Scorelevel_text_Row = Row(controls=[self.Scorelevel_text],alignment=MainAxisAlignment.CENTER)
        self.score_column = Column(controls=[self.scoretext_Row,self.Scorelevel_text_Row],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,spacing=0)

        #! ==================================================== Textfeilds ==============================================
        self.Height = Frontend.Calcultor_textfeild(Label="Height",prefix_icon=Icons.HEIGHT_ROUNDED,hint_text="",keyboard_type=KeyboardType.NUMBER)
        self.Weight = Frontend.Calcultor_textfeild(Label="Weight",prefix_icon=Icons.MONITOR_WEIGHT_ROUNDED,hint_text="",keyboard_type=KeyboardType.NUMBER)

        self.Weight_units = Frontend.Calcultor_dropdown(options=["Kilograms **(kg)**","Pounds **(lb)**"])
        self.Height_units = Frontend.Calcultor_dropdown(options=["Centimeters **(cm)**","Feet **(ft)**"])

        self.age = Frontend.Calcultor_textfeild(Label="Age",prefix_icon=Icons.CALENDAR_MONTH_ROUNDED,Width=310,hint_text="",keyboard_type=KeyboardType.NUMBER)

        #! ==================================================== Radio Button ==============================================
        label_style = TextStyle(weight=FontWeight.W_500,font_family="Alex")
        self.male = Radio(label="Male",value="0",label_position=LabelPosition.RIGHT,active_color=Variables.TAN,label_style=label_style)
        self.Female = Radio(label="Female",value="1",label_position=LabelPosition.RIGHT,active_color=Variables.TAN,label_style=label_style)

        self.Gender_options = Row(controls=[self.male,self.Female],spacing=15)
        self.gender = RadioGroup(content=self.Gender_options,value="")

        #! ========================================================= Calculate Button =========================================================

        self.Calculate_text = Text("Calculate",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_700)
        self.Calculate = Container(content=Row([Icon(Icons.CALCULATE,size=24,color=Colors.WHITE),self.Calculate_text],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True,border=border.all(1,Colors.WHITE))


        #! ========================================================= Arcticture =========================================================
        self.row0 = Row(controls=[self.title_text],alignment=MainAxisAlignment.CENTER)
        self.row1 = Row(controls=[self.score_column],alignment=MainAxisAlignment.CENTER)
        self.row2 = Row(controls=[self.age],alignment=MainAxisAlignment.CENTER)
        self.row3 = Row(controls=[self.Height,self.Height_units],alignment=MainAxisAlignment.CENTER)
        self.row4 = Row(controls=[self.Weight,self.Weight_units],alignment=MainAxisAlignment.CENTER)
        self.row5 = Row(controls=[self.age],alignment=MainAxisAlignment.CENTER)
        self.row6 = Row(controls=[Text("Gender:",weight=FontWeight.W_600,font_family="Alex",color=Variables.TAN),self.gender],alignment=MainAxisAlignment.CENTER,spacing=50)
        self.row7 = Row(controls=[self.Calculate],alignment=MainAxisAlignment.CENTER)

        #! ========================================================= controls =========================================================
        self.controls = [self.null,self.row0,self.row1,self.null,self.row2,self.row3,self.row4,self.row6,self.null,self.row7]



if __name__ == "__main__":
    def main(page:Page):
        page.add(Calculator_BMR(page))
    
    app(main)