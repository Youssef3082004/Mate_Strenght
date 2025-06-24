from flet import * 
from Constant.variables import Variables
from Backend.Signup import *


class Signup_interface_2(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.window.height = 700
        self.page.window.width = 400
        self.page.scroll = ScrollMode.AUTO
        self.page.window.resizable = False
        self.page.fonts = {"andalus": "font/andalus.ttf", "Alex": "font/Alex.ttf" , "pac":"font/Pacifico-Regular.ttf","Inter":"font/Inter.ttf"}
        self.page.theme = Theme(page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.OPEN_UPWARDS,android=PageTransitionTheme.OPEN_UPWARDS))
        self.page.theme_mode = ThemeMode.LIGHT
        self.page.window.center()
        

        #! ==================================================== first Layer in interface ==============================================
        self.page_text = Text("    You're almost done!  \n    Setup complete after this",font_family="Alex",weight=FontWeight.W_500,color=Colors.WHITE,size=24)
        self.White_container = Container(bgcolor=Colors.WHITE,width=self.page.window.width - 15,height=self.page.height-50,border_radius=BorderRadius(50,50,0,0),padding=padding.only(top=25))

        #! ==================================================== first Layer Controls in interface ==============================================
        self.row0 = Column(controls=[Variables.space15,self.page_text])
        self.row1 = Row(controls=[self.White_container])
        self.first_layer = Column(controls=[self.row0,self.row1],spacing=90)

        #! ==================================================== White Container Textfeilds ==============================================
        self.White_container_text = Row(controls=[Text("Create Account",font_family="Alex",weight=FontWeight.W_500,color=Colors.BLACK,size=24)],alignment=MainAxisAlignment.CENTER)
        
        self.Birthday =Signup_Frontend.Signup_textfeild(label="Birthday",prefix_icon=Icons.CAKE,hint_text="Your Birthday?",read_only=True,width=150) 
        self.Age =Signup_Frontend.Signup_textfeild(label="Age",prefix_icon=Icons.CALENDAR_MONTH,hint_text="Your Age?",read_only=True,width=150) 

        self.Weight = Signup_Frontend.Signup_textfeild(label="Weight",prefix_icon=Icons.MONITOR_WEIGHT,hint_text="Your Weight?",keyboard_type=KeyboardType.EMAIL,width=150)
        self.Height = Signup_Frontend.Signup_textfeild(label="Height",prefix_icon=Icons.HEIGHT,hint_text="Your Weight?",keyboard_type=KeyboardType.NUMBER,width=150)
        self.fitness_Goal = Dropdown(leading_icon=Icon(Icons.FITNESS_CENTER),label="Goal",label_style=Signup_variables.dropdown_style,editable=True,border_color=Variables.BLACK,width=145,border_radius=BorderRadius(10,10,10,10),options=Signup_variables.Fitness_Goal_options)
        self.Your_activity =Dropdown(leading_icon=Icon(Icons.SPORTS_GYMNASTICS),label="Activity",label_style=Signup_variables.dropdown_style,editable=True,border_color=Variables.BLACK,width=145,border_radius=BorderRadius(10,10,10,10),options=Signup_variables.Activities_options)
        
        
        radio_options = Row([
            Radio("Male",value="Male",label_style=Signup_variables.Gender_style,fill_color=Variables.TAN,label_position=LabelPosition.RIGHT ),
            Radio("Female",value="Female",label_style=Signup_variables.Gender_style,fill_color=Variables.TAN,label_position=LabelPosition.RIGHT )
            ],spacing=40)
        

        #! ==================================================== Sign up Button ==============================================
        self.signup_text = Text("SIGN UP",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_500)
        self.signup = Container(content=Row([Icon(Icons.HOW_TO_REG_ROUNDED,size=24,color=Colors.WHITE),self.signup_text],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True)


        self.Back_text = Text("Back",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_500)
        self.Back = Container(content=Row([Icon(name=Icons.ARROW_BACK_OUTLINED,color=Colors.WHITE,size=24),self.Back_text],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True)

        self.signup_area = Column(controls=[self.signup,self.Back],alignment=MainAxisAlignment.CENTER)
        self.signup_area = Row(controls=[self.signup_area],alignment=MainAxisAlignment.CENTER)        

        #! ==================================================== White Container Controls ==============================================
        self.Signup_text =  Text("Already have an account?",color=Colors.BLACK54,size=14,font_family="Inter",weight=FontWeight.W_500)
        self.Signup =  Text("SIGN IN".center(35),color=Variables.TAN,size=14,font_family="Inter",weight=FontWeight.W_500)

        self.login_Button = TextButton(content=self.Signup)
        self.Login_area = Column(controls=[self.Signup_text,Row(controls=[self.login_Button],alignment=CrossAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== White Container Controls ==============================================
        
        self.age = Row(controls=[self.Birthday,self.Age],alignment=MainAxisAlignment.CENTER)
        self.Weight_Height = Row(controls=[self.Weight,self.Height],alignment=MainAxisAlignment.CENTER,spacing=5)
        self.user_activity_row = Row(controls=[self.fitness_Goal,self.Your_activity],alignment=MainAxisAlignment.CENTER)
        self.Gender_row = Row(controls=[radio_options],alignment=MainAxisAlignment.CENTER)

        self.textFeilds_column = Column(controls=[self.age,self.Weight_Height,self.user_activity_row,self.Gender_row],spacing=15)
        self.login_row = Row(controls=[self.signup],alignment=MainAxisAlignment.CENTER)
        self.login_row = Row(controls=[self.Back],alignment=MainAxisAlignment.CENTER)

        self.signup_row = Row(controls=[self.Login_area],alignment=MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)


        self.White_container.content = Column(controls=[self.White_container_text,self.textFeilds_column,self.signup_area,self.signup_row],spacing=60)
        #! ==================================================== Main Page Conatiner ===================================================
        
        self.Interface_controls = Column(controls=[self.first_layer],scroll=ScrollMode.AUTO)
        self.main_container = Container(content=self.Interface_controls,gradient=Variables.LINEARGRADIENT,width=400,height=self.page.height)
        self.controls = [SafeArea(content=self.main_container)]


        self.date_picker = Signup_Frontend.DatePicker_custom(self.page,self.Birthday,self.Age)
        self.Birthday.on_click = lambda e:self.date_picker.open_Datepicker()
        self.page.overlay.append(self.date_picker)



if __name__ == "__main__":
    def main(page:Page):
        page.add(Signup_interface_2(page))
        page.update()
    app(target=main,assets_dir= r"D:\Python\Strenght Mate\assets")