from flet import * 
import datetime
from Constant.data import Data


class Signup_variables:
    BLACK = "#1A1A1A"
    TAN = "#B99A45"
    options_style = TextStyle(size=12, weight=FontWeight.W_500,font_family="Inter",overflow=TextOverflow.ELLIPSIS,letter_spacing=0,color=TAN)
    Gender_style = TextStyle(size=15, weight=FontWeight.W_500,font_family="Inter",overflow=TextOverflow.CLIP,letter_spacing=0,color=BLACK)
    dropdown_style = TextStyle(size=15, weight=FontWeight.W_900, color=TAN,font_family="andalus",overflow=TextOverflow.ELLIPSIS,letter_spacing=0)

    __Fitness_Goal = ["Build Muscle","Lose Body Fat","Boost Endurance","Increase Flexibility","Stay Healthy"]    
    Fitness_Goal_options = [dropdown.Option(leading_icon=Icon(Icons.FITNESS_CENTER,color="#B99A45"),text=type,key=type) for type in __Fitness_Goal]

    __Activities = ["Sedentary","Lightly Active","Moderately Active","Very Active","Highly Active"]    
    Activities_options = [dropdown.Option(leading_icon=Icon(Icons.SPORTS_GYMNASTICS,color="#B99A45"),text=type,key=type) for type in __Activities]


    codes_contries = [dropdown.Option(leading_icon=Icon(Icons.PUBLIC,color="#B99A45"),content=Markdown(f"**{country[-1]}**  `{code}`"),key=code) for code,country in zip(Data.Country_codes.keys(),Data.Country_codes.values())]

class Signup_Frontend:

    def onchange_countries_code(page:Page,e:ControlEvent,country:TextField):
        country.value = Data.Country_codes[e.control.value][0]
        country.disabled = False
        country.opacity = 1
        page.update()




    class DatePicker_custom(DatePicker):
        def __init__(self,page:Page,Birthday:TextField,age:TextField):
            super().__init__()
            self.page = page
            self.Birthday = Birthday
            self.age = age
            self.current_date = datetime.datetime(year = 1940 ,month = 1 , day = 1)
            self.first_date=datetime.datetime(year = 1940 ,month = 1 , day = 1)
            self.last_date=self.__get_last_date()
            self.on_change = lambda e:self.__set_value()
            
        def open_Datepicker(self):
            self.open = True
            self.page.update()
        

        def __set_value(self):
            self.Birthday.value = str(self.value.date())
            days = (datetime.datetime.now().date() - self.value.date()).days
            self.age.value = days // 365
            self.page.update()
        

        def __get_last_date(self):
            today = datetime.date.today()
            try:
                ten_years_ago = today.replace(year=today.year - 10)
            except ValueError:
                ten_years_ago = today.replace(month=2, day=28, year=today.year - 10)
            

            return ten_years_ago

            

    
    class Signup_textfeild(TextField):
        
        def __init__(self, value = None, keyboard_type = None, multiline = None, min_lines = None, max_lines = None, max_length = None, password = None, can_reveal_password = None, read_only = None, shift_enter = None, text_align = None, autofocus = None, capitalization = None, autocorrect = None, enable_suggestions = None, smart_dashes_type = None, smart_quotes_type = None, show_cursor = None, cursor_color = None, cursor_error_color = None, cursor_width = None, cursor_height = None, cursor_radius = None, selection_color = None, input_filter = None, obscuring_character = None, enable_interactive_selection = None, enable_ime_personalized_learning = None, can_request_focus = None, ignore_pointers = None, enable_scribble = None, animate_cursor_opacity = None, always_call_on_tap = None, scroll_padding = None, clip_behavior = None, keyboard_brightness = None, mouse_cursor = None, strut_style = None, autofill_hints = None, on_change = None, on_click = None, on_submit = None, on_focus = None, on_blur = None, on_tap_outside = None, text_size = None, text_style = None, text_vertical_align = None, label = None, label_style = None, icon = None, border = None, color = None, bgcolor = None, border_radius = None, border_width = None, border_color = None, focused_color = None, focused_bgcolor = None, focused_border_width = None, focused_border_color = None, content_padding = None, dense = None, filled = None, fill_color = None, hover_color = None, hint_text = None, hint_style = None, helper = None, helper_text = None, helper_style = None, counter = None, counter_text = None, counter_style = None, error = None, error_text = None, error_style = None, prefix = None, prefix_icon = None, prefix_text = None, prefix_style = None, suffix = None, suffix_icon = None, suffix_text = None, suffix_style = None, focus_color = None, align_label_with_hint = None, hint_fade_duration = None, hint_max_lines = None, helper_max_lines = None, error_max_lines = None, prefix_icon_size_constraints = None, suffix_icon_size_constraints = None, size_constraints = None, collapsed = None, fit_parent_size = None, ref = None, key = None, width = None, height = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None, rtl = None, adaptive = None):
            super().__init__(value, keyboard_type, multiline, min_lines, max_lines, max_length, password, can_reveal_password, read_only, shift_enter, text_align, autofocus, capitalization, autocorrect, enable_suggestions, smart_dashes_type, smart_quotes_type, show_cursor, cursor_color, cursor_error_color, cursor_width, cursor_height, cursor_radius, selection_color, input_filter, obscuring_character, enable_interactive_selection, enable_ime_personalized_learning, can_request_focus, ignore_pointers, enable_scribble, animate_cursor_opacity, always_call_on_tap, scroll_padding, clip_behavior, keyboard_brightness, mouse_cursor, strut_style, autofill_hints, on_change, on_click, on_submit, on_focus, on_blur, on_tap_outside, text_size, text_style, text_vertical_align, label, label_style, icon, border, color, bgcolor, border_radius, border_width, border_color, focused_color, focused_bgcolor, focused_border_width, focused_border_color, content_padding, dense, filled, fill_color, hover_color, hint_text, hint_style, helper, helper_text, helper_style, counter, counter_text, counter_style, error, error_text, error_style, prefix, prefix_icon, prefix_text, prefix_style, suffix, suffix_icon, suffix_text, suffix_style, focus_color, align_label_with_hint, hint_fade_duration, hint_max_lines, helper_max_lines, error_max_lines, prefix_icon_size_constraints, suffix_icon_size_constraints, size_constraints, collapsed, fit_parent_size, ref, key, width, height, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, rtl, adaptive)
            self.label = label
            self.width = width
            self.prefix_icon=prefix_icon
            self.read_only = read_only
            self.suffix = suffix
            self.label_style=TextStyle(size=20, weight=FontWeight.W_900, color=Signup_variables.TAN,font_family="andalus")
            self.border=InputBorder.OUTLINE
            self.border_color=Signup_variables.BLACK
            self.hint_text=hint_text
            self.hint_style=TextStyle(color=Colors.BLACK54)
            self.hint_fade_duration=1000
            self.text_style=TextStyle(size=15, weight=FontWeight.W_400,font_family="Alex")
            self.keyboard_type=keyboard_type
            
    