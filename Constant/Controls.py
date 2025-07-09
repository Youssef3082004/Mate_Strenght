from flet import *




class Matestrenght_Appbar(AppBar):
    def __init__(self):
        super().__init__()
        self.leading = IconButton(Icons.MENU)
        self.elevation = 0
        self.actions = [IconButton(Icons.NOTIFICATIONS)]
        self.center_title = True
        self.bgcolor = "#ffffff"
         
        #! ==================================================== Main and Sub Title ==============================================
        self.matestrnght_style = TextStyle(font_family="pac",size=20,weight=FontWeight.BOLD,foreground=Paint(gradient=PaintLinearGradient((50, 20), (120, 20), ["#1A1A1A", "#B99A45"],tile_mode=GradientTileMode.MIRROR)))
        self.sub_title = Text(value="Ready To Crush Your Goals ?",size=10,font_family="Alex",weight=FontWeight.W_600)
        self.main_title = Text(spans=[TextSpan("Strenght Mate",style=self.matestrnght_style)])
        self.title_column = Column(controls=[self.main_title,self.sub_title],alignment=MainAxisAlignment.CENTER)
        self.title = self.title_column



class Common_Appbar(AppBar):
    def __init__(self,Main_Title:str):
        super().__init__()
        self.Main_Title = Main_Title
        self.leading = IconButton(Icons.ARROW_BACK)
        self.elevation = 0
        self.center_title = True
        self.bgcolor = "#f1f5f8"
        
        #! ==================================================== Main and Sub Title ==============================================
        self.matestrnght_style = TextStyle(font_family="pac",size=20,weight=FontWeight.BOLD,color=Colors.BLACK)
        self.main_title = Text(spans=[TextSpan(f"{self.Main_Title}",style=self.matestrnght_style)])
        self.title = self.main_title
