from flet import * 
from Constant.variables import *

class Home_Frontend:

    class Home_Dashboard(Container):
        def __init__(self,page:Page,load_color:str,value:float = 0,):
            super().__init__()
            self.page = page
            self.value = value
            self.load_color = load_color
            self.width = self.page.window.width - 50
            self.height = 150
            self.padding = padding.only(top=15,left=15)
            self.bgcolor = Colors.WHITE
            self.border_radius = 15
            self.shadow=[BoxShadow(spread_radius=0,blur_radius=5 ,offset=Offset(0,2.5),blur_style=ShadowBlurStyle.OUTER)]

            #! ==================================================== Head Title Container ==============================================
            
            self.welcome_text = Text("Good Morning!",weight=FontWeight.W_700,size=22,font_family="Alex")
            self.question = Text("Ready For Today Challange ?",color=Colors.BLACK54,font_family="Alex")

            self.title = Column(controls=[self.welcome_text,self.question],alignment=MainAxisAlignment.CENTER,spacing=5)

            #! ==================================================== Progress Bar Contnet ==============================================
            
            self.daily= Text("Daily Goal Text",color=Colors.BLACK54,font_family="Inter")
            self.progress_rate = Text(f"{self.value}%",weight=FontWeight.W_600)
            self.Pregrees_bar = ProgressBar(value=(self.value/100),width=150,border_radius=25,bgcolor=Colors.GREY_400,color=self.load_color)

            self.daily_row = Row(controls=[self.daily],alignment=MainAxisAlignment.START)
            self.progress_row =Row(controls=[self.Pregrees_bar,self.progress_rate],spacing=8,alignment=MainAxisAlignment.CENTER) 
            self.progress_control = Column(controls=[self.daily_row,self.progress_row],alignment=MainAxisAlignment.CENTER,spacing=5)

            #! ==================================================== Widget Controls arrangement ==============================================

            self.Widget_column = Column(controls=[self.title,self.progress_control],spacing=15)
            self.ring = Row(controls=[self.RingProgress(value=self.value,color=self.load_color)],alignment=MainAxisAlignment.CENTER)

            #! ==================================================== Content ===================================================================

            self.content = Row(controls=[self.Widget_column,self.ring],spacing=25,alignment=MainAxisAlignment.CENTER)
        



        class RingProgress(Stack):
            def __init__(self, value: float, color=Colors.BLUE):
                super().__init__()
                self.value = value
                self.size = 100
                self.color = color
                self.bgcolor = Colors.GREY_400
                self.width = 200
                self.height = self.size
                        
                self.progress_ring = ProgressRing(value=(self.value / 100),width=100,bgcolor=self.bgcolor,color=self.color,stroke_cap=StrokeCap.ROUND,height=self.size,)
                self.container =  Container(alignment=alignment.center,width=self.size,height=self.size,content=Text(f"{int(self.value)}%",size=self.size * 0.25,weight=FontWeight.BOLD),)
                
                self.controls = [self.progress_ring,self.container]



    class Home_Button(Container):
        def __init__(self,text:str,icon_content,colors:list):
            super().__init__()
            self.text = text
            self.icon_content = icon_content
            self.colors = colors
            self.border_radius = 15
            self.width = 80
            self.height = 80 
            self.padding = padding.only(top=20)
            self.gradient = LinearGradient(colors=self.colors,stops=[0.15,1],begin=alignment.top_center,end=alignment.bottom_center)

            self.Button_name = Row([Text(value=self.text,color=Colors.WHITE,font_family="Alex",size=12)],alignment=MainAxisAlignment.CENTER)
            self.icon = Row([Icon(name=self.icon_content,color=Colors.WHITE)],alignment=MainAxisAlignment.CENTER)

            self.content = Column(controls=[self.icon , self.Button_name],spacing=3)
    


    class User_stats(Container):
        def __init__(self,value:str,text:str,icon,colors:list):
            super().__init__()
            self.value = value
            self.text = text
            self.icon = icon
            self.colors = colors
            self.border_radius = 15
            self.width = 110
            self.height = 110
            self.color = Colors.WHITE
            self.gradient = LinearGradient(colors=self.colors,stops=[0.15,1],begin=alignment.top_center,end=alignment.bottom_center)

            #! ==================================================== Content ===================================================================
            self.container_icon = Container(content=Icon(name=self.icon,color=self.color),bgcolor=Colors.WHITE24,border_radius=10,width=35,height=35)
            self.icons_row = Row(controls=[self.container_icon,Icon(name=Icons.TRENDING_UP,color = self.color)],alignment=MainAxisAlignment.CENTER,spacing=40)

            #! ==================================================== Content ===================================================================
            self.text_control = Text(value=self.text,color=self.color,weight=FontWeight.W_500,font_family="Alex")
            self.text_conatainer = Container(content=self.text_control,padding=padding.only(left=5))
            self.text_row = Row(controls=[self.text_conatainer],alignment=MainAxisAlignment.START)

            #! ==================================================== Content ===================================================================
            self.value_text = Text(value=self.value,color=self.color,weight=FontWeight.BOLD,font_family="Alex")
            self.value_conatiner = Container(content=self.value_text,padding=padding.only(left=5))
            self.Value_row = Row(controls=[self.value_conatiner],alignment=MainAxisAlignment.START)

            #! ==================================================== Content ===================================================================
            self.content = Column(controls=[self.icons_row,Column([self.text_row, self.Value_row,],spacing=0,alignment=MainAxisAlignment.CENTER)],alignment=MainAxisAlignment.CENTER,spacing=15)


    class Quickstart_timer(Container):
        def __init__(self,title:str,Container_width:int,image:Image):
            super().__init__()
            self.title = title
            self.Container_width = Container_width
            self.width = self.Container_width
            self.stack_image = image
            self.border_radius = 15
            self.height = 130
            self.padding = 20
            self.bgcolor = Colors.WHITE

            #! ==================================================== Title text ===================================================================
            self.title_text = Text(value=self.title,font_family="Alex",weight=FontWeight.W_700,size=20)
            #! ==================================================== Start Button ===================================================================
            self.start_text = Text(value="Start Timer")
            self.start_icon = Icon(name=Icons.TIMER)
            self.Start_button = TextButton(content=Row(controls=[self.start_icon,self.start_text],spacing=3,alignment=MainAxisAlignment.CENTER))
            #! =================================================== Start Button ===================================================================
            self.image_container = Container(content=self.stack_image,alignment=alignment.top_center,height=200,border_radius=10)
            #! ==================================================== Start Button ===================================================================
            self.left_continar = Column(controls=[self.title_text,self.Start_button],spacing=10,alignment=MainAxisAlignment.CENTER)
            #! ==================================================== Start Button ===================================================================
            self.content = Row(controls=[self.left_continar,self.image_container],alignment=MainAxisAlignment.SPACE_BETWEEN)     

            
            



    
        