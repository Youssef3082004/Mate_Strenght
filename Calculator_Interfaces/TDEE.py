from flet import * 
from .Calculator import Frontend
from Constant.variables import Variables



class Calculator_TDEE(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page 
        self.expand = True
        self.page = page
        self.scroll = ScrollMode.AUTO
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
        self.title_text = Text(value="Your Calories",color=Colors.BLACK54,size=25,font_family="Inter",weight=FontWeight.BOLD)

        #! ==================================================== TDEE Score ==============================================
        self.Score_text = Text(value="0",color=Colors.BLACK54,size=80,font_family="Inter",weight=FontWeight.BOLD)
        self.Scorelevel_text = Text(value="Not Calcaulted Yet",color=Colors.BLACK54,size=20,font_family="Inter",weight=FontWeight.BOLD)
        self.scoretext_Row = Row(controls=[self.Score_text],alignment=MainAxisAlignment.CENTER)
        self.Scorelevel_text_Row = Row(controls=[self.Scorelevel_text],alignment=MainAxisAlignment.CENTER)
        self.score_column = Column(controls=[self.scoretext_Row,self.Scorelevel_text_Row],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,spacing=0)

        #! ==================================================== BMR TextFeild ==============================================
        self.BMR = Frontend.Calcultor_textfeild(Label="BMR",prefix_icon=Icons.ACCESSIBILITY_NEW,Width=310,hint_text="Basal Metabolic Rate",keyboard_type=KeyboardType.NUMBER)

        #! ==================================================== Activity Level ==============================================
        self.options = ["Sedentary \n**(No Exercise)**","Lightly Active \n**(1-3 days/week)**","Moderately Active \n**(3-5 days/week)**","Very Active \n**(6-7 days/week)**","Super Active \n**(Very hard exercise, Training twice a day)**"]
        self.keys = [1.2,1.375,1.55,1.725,1.9]
        self.active_level = Frontend.Calcultor_dropdown(options=self.options,width=310,label="Activity Level",icon=Icons.FITNESS_CENTER)
        

        #! ========================================================= Calculate Button =========================================================
        self.Calculate_text = Text("Calculate",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_700)
        self.Calculate = Container(content=Row([Icon(Icons.CALCULATE,size=24,color=Colors.WHITE),self.Calculate_text],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True,border=border.all(1,Colors.WHITE))


        #! ========================================================= Arcticture =========================================================
        self.row0 = Row(controls=[self.title_text],alignment=MainAxisAlignment.CENTER)
        self.row1 = Row(controls=[self.score_column],alignment=MainAxisAlignment.CENTER)
        self.row2 = Row(controls=[self.BMR],alignment=MainAxisAlignment.CENTER)
        self.row3 = Row(controls=[self.active_level],alignment=MainAxisAlignment.CENTER)
        self.row4 = Row(controls=[self.Calculate],alignment=MainAxisAlignment.CENTER)



        #! ========================================================= Controls =========================================================

        self.controls = [self.null,self.row0,self.row1,self.null,self.null,self.row2,self.row3,self.null,self.row4]



if __name__ == "__main__":
    def main(page:Page):
        page.add(Calculator_TDEE(page))
    
    app(main)