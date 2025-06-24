from flet import *
from Constant.variables import *

class welcome_screen(Column):
    def __init__(self,page:Page,on_next):
        super().__init__()
        self.page = page
        self.on_next = on_next
        self.page.window.width = 400
        self.page.window.resizable = True
        self.page.window.height = page.height
        self.page.padding = 0
        self.page.fonts = {"andalus": "font/andalus.ttf", "Alex": "font/Alex.ttf" , "pac":"font/Pacifico-Regular.ttf","Inter":"font/Inter.ttf"}
        self.page.theme = Theme(page_transitions=PageTransitionsTheme(windows=PageTransitionTheme.OPEN_UPWARDS,android=PageTransitionTheme.OPEN_UPWARDS))
        self.page.vertical_alignment = page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.window.center()

        #! ==================================================== main Title Text ==============================================
        main_text = Text(value="Train Like a Beast. Track Like a Mate",text_align=TextAlign.CENTER,color=Colors.WHITE,max_lines=1, width=page.window.width - 20 ,style=TextStyle(size=18,color=Colors.BLACK,weight=FontWeight.W_500,font_family="Pac",))
       
       #! ====================================================  main image ==============================================
        background_image = Image(src="icon-removebg.png",width=page.window.width-200,height=page.height,expand=True,fit=ImageFit.FIT_WIDTH)

       #! ====================================================  Start Button ==============================================
        self.start_button_text = Text(value= "Let’s Go",text_align=TextAlign.CENTER,color=Colors.WHITE,size=25,font_family= "pac")
        shadow=BoxShadow(offset=Offset(0, 4),blur_radius=4,color=Variables.BLACK)
        start_button = Container(content=self.start_button_text,ink=True,width=110,height=50,alignment=alignment.center,bgcolor=Variables.BLACK,border_radius=25,shadow=shadow,on_click=self.on_next)
        

       #! ====================================================  Interface Controls ==============================================
        self.stack =Stack([
            Container(content=background_image, alignment=alignment.center,expand=True),
            Container(content=main_text, alignment=alignment.center, top=100,expand=True),           
            Container(content=start_button, alignment=alignment.center, top=580, left=140,expand=True)]
        ,alignment=alignment.center)

       #! ====================================================  main Controls ==============================================
        gradeint = LinearGradient(colors=[Variables.BLACK,Variables.TAN],stops=[0.5,1],begin=alignment.top_center,end=alignment.bottom_center)
        self.container = Container(content=self.stack,width=page.window.width,height=page.height,gradient=gradeint)
        self.controls = [self.container]

        
if __name__ == "__main__":

    def main(page: Page):
        page.add(welcome_screen(page,print()))
    app(target=main,assets_dir= r"D:\Python\Strenght Mate\assets")