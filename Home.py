from flet import * 
from Constant.variables import Variables
from Constant.Controls import Matestrenght_Appbar 
from Backend.Home import Home_Frontend 

class Home_interface(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.window.height = 700
        self.page.window.width = 400
        self.page.scroll = ScrollMode.AUTO
        self.page.window.resizable = False
        self.page.bgcolor = Variables.PAGES_BACKGROUND_COLOR
        self.page.padding = padding.only(top=40)
        self.page.fonts = {"andalus": "font/andalus.ttf", "Alex": "font/Alex.ttf" , "pac":"font/Pacifico-Regular.ttf","Inter":"font/Inter.ttf"}
        self.page.theme = Theme(page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.OPEN_UPWARDS,android=PageTransitionTheme.OPEN_UPWARDS))
        self.page.theme_mode = ThemeMode.LIGHT
        self.page.window.center()
        self.page.appbar = Matestrenght_Appbar()


        #! ==================================================== Dashboard in Home Interface ==============================================
        self.Dashboard = Row([Home_Frontend.Home_Dashboard(page=self.page,load_color=Variables.TAN,value=25)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== Buttons Row ==============================================
        self.Schedule = Home_Frontend.Home_Button(text="Schedule",icon_content=Icons.CALENDAR_MONTH,colors=["#000000","#2375EF"])
        self.Analytical = Home_Frontend.Home_Button(text="Analytical",icon_content=Icons.PIE_CHART,colors=["#000000","#B30056"])
        self.Exercise = Home_Frontend.Home_Button(text="Exercise",icon_content=Icons.SPORTS_GYMNASTICS,colors=["#000000","#E54928"])
        self.Calculator = Home_Frontend.Home_Button(text="Calculator",icon_content=Icons.CALCULATE,colors=["#000000","#9058C8"])
        self.Button_Row = Row(controls=[self.Schedule,self.Analytical,self.Exercise,self.Calculator],alignment=MainAxisAlignment.CENTER,spacing=7)

        #! ==================================================== Buttons Row ==============================================
        self.today_text = Text(value="Today Stat's",font_family="Alex",weight=FontWeight.BOLD,color=Colors.BLACK)

        self.View_stats = Text("View All",color=Variables.BLACK,font_family="Alex",weight=FontWeight.BOLD)
        self.View_icon = Icon(Icons.ARROW_RIGHT,color=Variables.BLACK,size=24)
        self.View_stats = TextButton(content=Row(controls=[self.View_stats,self.View_icon],spacing=0,alignment=MainAxisAlignment.CENTER))

        self.Stats_row = Row(controls=[self.today_text,self.View_stats],alignment=MainAxisAlignment.CENTER,spacing=170)
        self.Stats_row_container = Row([Container(content=self.Stats_row,bgcolor=Variables.TAN,border_radius=10,padding=padding.only(left=9),width=self.page.window.width-45)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== user Stats ==============================================
        self.workout_time = Home_Frontend.User_stats(value="45m",text="Workout Time",icon=Icons.WATCH_LATER_OUTLINED,colors=["#000000","#2375EF"])
        self.User_Goal = Home_Frontend.User_stats(value="4/5 Day",text="Weekly Goal",icon=Icons.EMOJI_EVENTS_OUTLINED,colors=["#000000","#B30056"])
        self.User_perforamnce = Home_Frontend.User_stats(value="20m",text="Cardio Time",icon=Icons.DIRECTIONS_RUN_OUTLINED,colors=["#000000","#E54928"])

        self.userstats_Row = Row(controls=[self.workout_time,self.User_Goal,self.User_perforamnce],alignment=MainAxisAlignment.CENTER,spacing=7)


        #! ==================================================== user Stats ==============================================
        self.Start_expression = Text(value="No More Waiting. It's Time to Begin!",font_family="Alex",weight=FontWeight.BOLD,color=Colors.BLACK,size=18)
        self.Start_expression_row = Row(controls=[self.Start_expression],alignment=MainAxisAlignment.CENTER)
        self.Start_expression_row_container = Row([Container(content=self.Start_expression_row,bgcolor=Variables.TAN,border_radius=10,height=35,padding=padding.only(left=9),width=self.page.window.width-45)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== user Stats ==============================================
        self.cardio_image = Image(src=r"Cardio2.jpg",height=200,expand=True,fit=ImageFit.FIT_HEIGHT)
        self.cardio = Home_Frontend.Quickstart_timer(title="Cardio Exercise",Container_width=self.page.window.width - 45, image=self.cardio_image)

        self.Exercise_image = Image(src=r"Exercise.jpg",height=200,expand=True,fit=ImageFit.FIT_HEIGHT)
        self.Exercise = Home_Frontend.Quickstart_timer(title="Gym Exercise",Container_width=self.page.window.width - 45, image=self.Exercise_image)


        self.row = Row([Column(controls=[self.cardio,self.Exercise],alignment=MainAxisAlignment.CENTER)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== Page Controls  ==============================================

        self.Page_controls = Column(controls=[self.Dashboard,self.Button_Row,self.Stats_row_container,self.userstats_Row,self.Start_expression_row_container,self.row,Variables.Null],alignment=MainAxisAlignment.CENTER,spacing=20)
        self.main_conatainer = Container(content=self.Page_controls)
        self.controls = [self.main_conatainer]






if __name__ == "__main__":
    def main(page:Page):
        page.add(Home_interface(page))
        page.update()
    app(target=main,assets_dir= r"D:\Python\Strenght Mate\assets")