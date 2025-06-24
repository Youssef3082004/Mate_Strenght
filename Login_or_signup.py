from flet import *
from Constant.variables import *


class log_sign(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.window.height = 700
        self.page.window.width = 400
        self.page.window.resizable = False
        self.page.fonts = {"andalus": "font/andalus.ttf", "Alex": "font/Alex.ttf" , "pac":"font/Pacifico-Regular.ttf","Inter":"font/Inter.ttf"}
        self.page.theme = Theme(page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.OPEN_UPWARDS,android=PageTransitionTheme.OPEN_UPWARDS))
        self.page.theme_mode = ThemeMode.LIGHT
        self.page.window.center()

        #! ==================================================== Application Logo Row ==============================================
        self.logo_image = Image(src=r"icon-removebg.png",width=page.window.width-200,height=page.height,expand=True,fit=ImageFit.SCALE_DOWN)
        self.logo_image_conatiner = Stack([Container(content=self.logo_image,alignment=alignment.top_center,width=page.window.width,height=200)])

        #! ==================================================== Application Logo Row ==============================================
        self.welcome_text = Text("Welcome!",size=30,font_family="Inter",color=Colors.WHITE,weight=FontWeight.W_700)
        self.welcome_text_row = Row(controls=[self.welcome_text],alignment=MainAxisAlignment.CENTER)
        self.logo_area = Column(controls=[self.logo_image_conatiner,self.welcome_text_row],alignment=MainAxisAlignment.CENTER,spacing=30)
       
        #! ==================================================== Buttons ==============================================
        self.signup_text = Text("Create Account",color=Colors.WHITE,size=16,font_family="Inter",weight=FontWeight.W_700)
        self.signup = Container(content=Row([Icon(Icons.PERSON_ADD_ALT_1,size=24,color=Colors.WHITE),self.signup_text],alignment=MainAxisAlignment.CENTER),gradient=Variables.LINEARGRADIENT,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True,border=border.all(1,Colors.WHITE))

        self.signin_text = Text("SIGN IN",color=Variables.BLACK,size=16,font_family="Inter",weight=FontWeight.W_800)
        self.signin = Container(content=Row([Icon(Icons.LOGIN_ROUNDED,size=24,color=Variables.BLACK),self.signin_text],alignment=MainAxisAlignment.CENTER),bgcolor=Colors.WHITE,height=45,width=260,border_radius=25,on_click=lambda e: print(),ink=True)

        self.Buttons_area = Column(controls=[self.signup,self.signin],alignment=MainAxisAlignment.CENTER)
        self.Buttons_area_row = Row(controls=[self.Buttons_area],alignment=MainAxisAlignment.CENTER)
        #! ==================================================== main Container ==============================================
        self.main_container_controls = Column(controls=[self.logo_area,self.Buttons_area_row],alignment=MainAxisAlignment.CENTER,spacing=50)
        gradeint = LinearGradient(colors=[Variables.BLACK,Variables.TAN],stops=[0.5,1],begin=alignment.top_center,end=alignment.bottom_center)
        self.main_container = Container(content=self.main_container_controls,gradient=gradeint,width=400,height=700)
        
        #! ==================================================== interface Controls ==============================================
        self.controls = [SafeArea(content=self.main_container)]





if __name__ == "__main__":
    def main(page:Page):
        page.add(log_sign(page))
        page.update()
    app(target=main,assets_dir= r"D:\Python\Strenght Mate\assets")   