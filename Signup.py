from flet import * 
from Constant.variables import Variables
from Backend.Signup import *


class Signup_interface(Column):
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
        self.page_text = Text("    Let’s stay in touch \n    type your contact info here",font_family="Alex",weight=FontWeight.W_500,color=Colors.WHITE,size=24)
        self.White_container = Container(bgcolor=Colors.WHITE,width=self.page.window.width - 15,height=700,border_radius=BorderRadius(50,50,0,0),padding=padding.only(top=25))

        #! ==================================================== first Layer Controls in interface ==============================================
        self.row0 = Column(controls=[Variables.space15,self.page_text])
        self.row1 = Row(controls=[self.White_container])
        self.first_layer = Column(controls=[self.row0,self.row1],spacing=90)

        #! ==================================================== White Container Textfeilds ==============================================
        self.White_container_text = Row(controls=[Text("Create Account",font_family="Alex",weight=FontWeight.W_500,color=Colors.BLACK,size=24)],alignment=MainAxisAlignment.CENTER)
        
        self.FullName =Signup_Frontend.Signup_textfeild("Full Name",prefix_icon=Icons.PERSON_2_ROUNDED,hint_text="Ex: John Donald") 
        self.Email = Signup_Frontend.Signup_textfeild(Label="E-mail",prefix_icon=Icons.EMAIL,hint_text="Ex: xxxxx@gmail.com",keyboard_type=KeyboardType.EMAIL)
        self.Phonenumber = Signup_Frontend.Signup_textfeild(Label="Phone-Number",prefix_icon=Icons.PHONE,hint_text="",keyboard_type=KeyboardType.NUMBER)
        self.password = Signup_Frontend.Signup_textfeild(Label="Password",prefix_icon=Icons.LOCK,hint_text="")
        self.Confirm_password = Signup_Frontend.Signup_textfeild(Label="Confirm Password",prefix_icon=Icons.LOCK,hint_text="")

        self.remember_me = Checkbox(label= "Remember me!",value=False ,label_position=LabelPosition.RIGHT,label_style= TextStyle(font_family="Alex"),active_color=Variables.TAN)
        self.Confirm_password.counter = Row([self.remember_me],alignment=MainAxisAlignment.CENTER)


        #! ==================================================== Sign In Button ==============================================
        self.login_text = Text("Next",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_500)
        self.login_button = Container(content=Row([self.login_text,Icon(Icons.ARROW_RIGHT_ALT_OUTLINED,color=Colors.WHITE,size=24)],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True)

        #! ==================================================== White Container Controls ==============================================
        self.Signup_text =  Text("Already have an account?",color=Colors.BLACK54,size=14,font_family="Inter",weight=FontWeight.W_500)
        self.Signup =  Text("Sign in".center(35),color=Variables.TAN,size=14,font_family="Inter",weight=FontWeight.W_500)

        self.signup_button = TextButton(content=self.Signup)
        self.Singup_area = Column(controls=[self.Signup_text,Row(controls=[self.signup_button],alignment=CrossAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)],alignment=MainAxisAlignment.CENTER)

        #! ==================================================== White Container Controls ==============================================
        
        self.Fullname_row = Row(controls=[self.FullName],alignment=MainAxisAlignment.CENTER)
        self.email_row = Row(controls=[self.Email],alignment=MainAxisAlignment.CENTER)
        self.Phonenumber_row = Row(controls=[self.Phonenumber],alignment=MainAxisAlignment.CENTER)
        self.password_row = Row(controls=[self.password],alignment=MainAxisAlignment.CENTER)
        self.Confirmpassword_row = Row(controls=[self.Confirm_password],alignment=MainAxisAlignment.CENTER)

        self.textFeilds_column = Column(controls=[self.Fullname_row,self.email_row,self.Phonenumber_row,self.password_row,self.Confirmpassword_row],spacing=15)
        self.login_row = Row(controls=[self.login_button],alignment=MainAxisAlignment.CENTER)
        self.signup_row = Row(controls=[self.Singup_area],alignment=MainAxisAlignment.CENTER,vertical_alignment=CrossAxisAlignment.CENTER)


        self.White_container.content = Column(controls=[self.White_container_text,self.textFeilds_column,self.login_row,self.signup_row],spacing=60)
        #! ==================================================== Main Page Conatiner ===================================================
        

        self.Interface_controls = Column(controls=[self.first_layer],scroll=ScrollMode.AUTO)
        self.main_container = Container(content=self.Interface_controls,gradient=Variables.LINEARGRADIENT,width=400,height=700)
        self.controls = [SafeArea(content=self.main_container)]



if __name__ == "__main__":
    def main(page:Page):
        page.add(Signup_interface(page))
        page.update()
    app(target=main,assets_dir= r"D:\Python\Strenght Mate\assets")