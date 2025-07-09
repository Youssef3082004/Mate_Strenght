from flet import * 



class Frontend:
    BLACK = "#1A1A1A"
    TAN = "#B99A45"

    class Calcultor_textfeild(TextField):
        def __init__(self,Label:str,prefix_icon,hint_text:str,Width:int = 150,keyboard_type:KeyboardType = KeyboardType.NONE):
            super().__init__()
            self.label = Label
            self.prefix_icon=prefix_icon
            self.width = Width
            self.label_style=TextStyle(size=20, weight=FontWeight.W_900, color=Frontend.TAN,font_family="andalus")
            self.border=InputBorder.OUTLINE
            self.border_color=Frontend.BLACK
            self.hint_text=hint_text
            self.hint_style=TextStyle(color=Colors.BLACK54,weight=FontWeight.W_700)
            self.hint_fade_duration=1000
            self.text_style=TextStyle(size=15, weight=FontWeight.W_400,font_family="Alex")
            self.keyboard_type=keyboard_type
            self.border_radius = 10
    


    class Calcultor_dropdown(Dropdown):
        def __init__(self,options:list,keys:list = [],width:int= 150,label:str = "Units",icon:Icons = Icons.STRAIGHTEN,):
            super().__init__()
            self.leading_icon = Icon(icon)
            self.label = label
            self.label_style = TextStyle(size=15, weight=FontWeight.W_900, color=Frontend.TAN,font_family="andalus",overflow=TextOverflow.ELLIPSIS,letter_spacing=0)
            self.editable = False
            self.border_color = Frontend.BLACK
            self.width =width
            self.border_radius = 10

            if keys:
                self.options = [dropdown.Option(content=Markdown(value=option),leading_icon=Icon(icon,color="#B99A45"),key=key) for option ,key in zip(options,keys)]

            else:
                self.options = [dropdown.Option(content=Markdown(value=option),leading_icon=Icon(icon,color="#B99A45"),key=option) for option in options]


    class Macros_chart(PieChart):
        def __init__(self,page:Page):
            super().__init__()
            self.page = page 
            self.sections_space=0.5
            self.width = 300
            self.height = 150
            self.center_space_radius=0
            self.on_chart_event=self.on_chart
            self.expand=True
            self.normal_radius = 90
            self.hover_radius = 100
            self.normal_title_style = TextStyle(size=16, color=Colors.WHITE, weight=FontWeight.BOLD)
            self.hover_title_style = TextStyle(size=22,color=Colors.WHITE,weight=FontWeight.BOLD,shadow=BoxShadow(blur_radius=2, color=Colors.BLACK54))
            self.Protein = PieChartSection(value=10,title="Protein",title_style=self.normal_title_style,radius=self.normal_radius,color="#73b5f0",data="Protein")
            self.carb = PieChartSection(value=10,title="Carb",title_style=self.normal_title_style,radius=self.normal_radius,color="#eb9147",data="Carb")
            self.fat = PieChartSection(value=10,title="Fat",title_style=self.normal_title_style,radius=self.normal_radius,color="#9383d7",data="Fat")

            
            
            self.sections = [self.Protein,self.carb,self.fat]



        def on_chart(self,e: PieChartEvent):
            for idx, section in enumerate(self.sections):
                if idx == e.section_index:
                    section.radius = self.hover_radius
                    section.title_style = self.hover_title_style
                    section.title = f"{section.value} g" if section.value > 10 else "Not Calculted" 
                else:
                    section.radius = self.normal_radius
                    section.title_style = self.normal_title_style
                    section.title = f"{section.data}"

            self.update()
        

        

