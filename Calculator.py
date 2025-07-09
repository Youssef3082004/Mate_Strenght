from flet import * 
from Constant.variables import Variables
from Constant.Controls import Common_Appbar 
from Calculator_Interfaces import BMI
from Calculator_Interfaces import BMR
from Calculator_Interfaces import TDEE
from Calculator_Interfaces import Water_Intake
from Calculator_Interfaces import MHR
from Calculator_Interfaces import Macros


class Calculator_interface(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.expand = True
        self.page = page
        self.page.padding = 0
        self.page.window.height = 700
        self.page.window.width = 400
        self.page.window.resizable = False
        self.page.bgcolor = Variables.PAGES_BACKGROUND_COLOR
        self.page.fonts = {"andalus": "font/andalus.ttf", "Alex": "font/Alex.ttf" , "pac":"font/Pacifico-Regular.ttf","Inter":"font/Inter.ttf"}
        self.page.theme = Theme(page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.OPEN_UPWARDS,android=PageTransitionTheme.OPEN_UPWARDS))
        self.page.theme_mode = ThemeMode.LIGHT
        self.page.window.center()
        self.page.appbar = Common_Appbar("Calcultor")

        #! ==================================================== Application Logo Row ==============================================
        
        self.tabs_control = Tabs(expand=True,scrollable=True,
        indicator_padding=0,
        divider_height=0,
        selected_index=0,
        padding=0,
        splash_border_radius=15,
        animation_duration=1000,
        indicator_color=Variables.BLACK,
        label_color=Variables.TAN,
        unselected_label_color=Colors.BLACK45,
        tabs=[Tab(
                tab_content=Text("Body Mass Index - BMI"),
                content=BMI.Calculator_BMI(self.page)
            ),
            Tab(text="Basal Metabolic Rate - BMR",
                content=BMR.Calculator_BMR(self.page)
            ),
            Tab(
                tab_content=Text("Total Daily Energy Expenditure - TDEE"),
                content=TDEE.Calculator_TDEE(self.page)
            ),
            Tab(
                tab_content=Text("Macronutrients"),
                content=Macros.Calculator_Macros(self.page)
            ),
            Tab(
                tab_content=Text("Max Heart Rate - MHR"),
                content=MHR.Calculator_MHR(self.page)
            ),
            Tab(
                tab_content=Text("Water Intake"),
                content=Water_Intake.Calculator_Water(self.page)
            ), 
        ])

      
        self.controls = [SafeArea(self.tabs_control)]
    



if __name__ == "__main__":
    def main(page:Page):

        page.add(Calculator_interface(page))
    app(target=main)
