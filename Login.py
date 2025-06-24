from flet import * 
from Constant.variables import Variables



class Login_interface(Column):
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
        self.page_text = Text("    Welcome back! \n    Sign in to get started",font_family="Alex",weight=FontWeight.W_500,color=Colors.WHITE,size=24)
        self.White_container = Container(bgcolor=Colors.WHITE,width=self.page.window.width - 15,height=800,border_radius=50,padding=padding.only(top=25))

        #! ==================================================== first Layer Controls in interface ==============================================
        self.row0 = Column(controls=[Variables.space15,self.page_text])
        self.row1 = Row(controls=[self.White_container])
        self.first_layer = Column(controls=[self.row0,self.row1],spacing=90)

        #! ==================================================== White Container Textfeilds ==============================================
        self.e_mail = TextField(
            label="E-mail",
            prefix_icon=Icons.PERSON_2_ROUNDED,
            label_style=TextStyle(size=20, weight=FontWeight.W_900, color=Variables.TAN,font_family="andalus"),
            border=InputBorder.OUTLINE,
            border_color=Variables.BLACK,
            hint_text="Your E-mail ?",
            hint_style=TextStyle(color=Colors.BLACK45),
            hint_fade_duration=1000,
            text_style=TextStyle(size=15, weight=FontWeight.W_400,font_family="Alex"),
            keyboard_type=KeyboardType.EMAIL
        )

        self.password = TextField(
            label= "Password",
            border_color=Variables.BLACK,
            prefix_icon=Icons.LOCK,
            can_reveal_password=True,
            password=True,
            hint_text="Your Password ?",
            hint_style=TextStyle(color=Colors.BLACK45),
            hint_fade_duration=1500,
            text_style=TextStyle(size=15, weight=FontWeight.W_400,font_family="Alex"),
            label_style=TextStyle(size=20, weight=FontWeight.W_900, color=Variables.TAN,font_family="andalus"),
            border=InputBorder.OUTLINE,
        )


        self.remember_me = Checkbox(
            label= "Remember me!",
            value=False ,
            label_position=LabelPosition.RIGHT,
            label_style= TextStyle(font_family="Alex"),
            active_color=Variables.TAN
        )
        self.password.counter = Row([self.remember_me],alignment=MainAxisAlignment.CENTER)


        #! ==================================================== Sign In Button ==============================================
        self.login_text = Text("SIGN IN",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_500)
        self.login_button = Container(content=Row([Icon(Icons.LOGIN_ROUNDED,size=24,color=Colors.WHITE),self.login_text],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True)

        #! ==================================================== White Container Controls ==============================================
        self.Signup_text =  Text("Dont have an account?",color=Colors.BLACK54,size=14,font_family="Inter",weight=FontWeight.W_500)
        self.Signup =  Text("SIGN UP".center(25),color=Variables.TAN,size=14,font_family="Inter",weight=FontWeight.W_500)

        self.signup_button = TextButton(content=self.Signup)
        self.Singup_area = Column(controls=[self.Signup_text,Row(controls=[self.signup_button],alignment=CrossAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== White Container Controls ==============================================
        self.White_container_text = Row(controls=[Text("Sign-In",font_family="Alex",weight=FontWeight.W_500,color=Colors.BLACK,size=24)],alignment=MainAxisAlignment.CENTER)
        
        self.email_row = Row(controls=[self.e_mail],alignment=MainAxisAlignment.CENTER)
        self.password_row = Row(controls=[self.password],alignment=MainAxisAlignment.CENTER)
        self.textFeilds_column = Column(controls=[self.email_row,self.password_row],spacing=30)
        self.login_row = Row(controls=[self.login_button],alignment=MainAxisAlignment.CENTER)
        self.signup_row = Row(controls=[self.Singup_area],alignment=MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)


        self.White_container.content = Column(controls=[self.White_container_text,self.textFeilds_column,self.login_row,self.signup_row],spacing=60)
        #! ==================================================== Main Page Conatiner ===================================================
        

        self.Interface_controls = Column(controls=[self.first_layer])
        self.main_container = Container(content=self.Interface_controls,gradient=Variables.LINEARGRADIENT,width=400,height=700)
        self.controls = [SafeArea(content=self.main_container)]



if __name__ == "__main__":
    def main(page:Page):
        page.add(Login_interface(page))
        page.update()
    app(target=main,assets_dir= r"D:\Python\Strenght Mate\assets")