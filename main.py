from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty
import math

# Устанавливаем цвет фона
Window.clearcolor = (0.1, 0.1, 0.1, 1)

Builder.load_string('''
<ConverterApp>:
    tab_width: dp(150)
    background_color: 0.1, 0.1, 0.1, 1
    border: [0, 0, 0, 0]

    TabbedPanelItem:
        text: 'Системы счисления'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            spacing: dp(15)

            Label:
                text: 'Конвертер систем счисления'
                font_size: dp(22)
                bold: True
                color: 0, 0.7, 1, 1
                size_hint_y: None
                height: dp(40)

            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                size_hint_y: None
                height: dp(120)

                TextInput:
                    id: num_input
                    hint_text: 'Введите число'
                    multiline: False
                    font_size: dp(20)
                    background_color: 0.2, 0.2, 0.2, 1
                    foreground_color: 1, 1, 1, 1
                    padding: [dp(10), dp(10), dp(10), dp(10)]
                    size_hint_y: None
                    height: dp(50)

                BoxLayout:
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(50)

                    Spinner:
                        id: from_system
                        text: 'Десятичная (10)'
                        values: ['Десятичная (10)', 'Двоичная (2)', 'Восьмеричная (8)', 'Шестнадцатеричная (16)']
                        background_color: 0.3, 0.3, 0.3, 1
                        size_hint_x: 0.5

                    Spinner:
                        id: to_system
                        text: 'Двоичная (2)'
                        values: ['Двоичная (2)', 'Восьмеричная (8)', 'Шестнадцатеричная (16)', 'Десятичная (10)']
                        background_color: 0.3, 0.3, 0.3, 1
                        size_hint_x: 0.5

            Button:
                text: 'Конвертировать'
                font_size: dp(20)
                bold: True
                background_color: 0, 0.5, 1, 1
                background_normal: ''
                size_hint_y: None
                height: dp(50)
                on_press: root.convert_number()

            ScrollView:
                TextInput:
                    id: num_result
                    text: 'Результат: '
                    font_size: dp(18)
                    readonly: True
                    background_color: 0.15, 0.15, 0.15, 1
                    foreground_color: 1, 1, 1, 1
                    padding: [dp(10), dp(10), dp(10), dp(10)]

    TabbedPanelItem:
        text: 'Единицы данных'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            spacing: dp(15)

            Label:
                text: 'Конвертер единиц данных'
                font_size: dp(22)
                bold: True
                color: 0, 0.7, 1, 1
                size_hint_y: None
                height: dp(40)

            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                size_hint_y: None
                height: dp(120)

                TextInput:
                    id: data_input
                    hint_text: 'Введите значение'
                    multiline: False
                    font_size: dp(20)
                    background_color: 0.2, 0.2, 0.2, 1
                    foreground_color: 1, 1, 1, 1
                    padding: [dp(10), dp(10), dp(10), dp(10)]
                    size_hint_y: None
                    height: dp(50)

                BoxLayout:
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(50)

                    Spinner:
                        id: from_unit
                        text: 'Мегабайт (MB)'
                        values: ['Бит (b)', 'Байт (B)', 'Килобайт (KB)', 'Мегабайт (MB)', 'Гигабайт (GB)', 'Терабайт (TB)']
                        background_color: 0.3, 0.3, 0.3, 1
                        size_hint_x: 0.5

                    Spinner:
                        id: to_unit
                        text: 'Килобайт (KB)'
                        values: ['Бит (b)', 'Байт (B)', 'Килобайт (KB)', 'Мегабайт (MB)', 'Гигабайт (GB)', 'Терабайт (TB)']
                        background_color: 0.3, 0.3, 0.3, 1
                        size_hint_x: 0.5

            Button:
                text: 'Конвертировать'
                font_size: dp(20)
                bold: True
                background_color: 0, 0.5, 1, 1
                background_normal: ''
                size_hint_y: None
                height: dp(50)
                on_press: root.convert_data()

            ScrollView:
                TextInput:
                    id: data_result
                    text: 'Результат: '
                    font_size: dp(18)
                    readonly: True
                    background_color: 0.15, 0.15, 0.15, 1
                    foreground_color: 1, 1, 1, 1
                    padding: [dp(10), dp(10), dp(10), dp(10)]

    TabbedPanelItem:
        text: 'История'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(15)
            spacing: dp(15)

            Label:
                text: 'История операций'
                font_size: dp(22)
                bold: True
                color: 0, 0.7, 1, 1
                size_hint_y: None
                height: dp(40)

            ScrollView:
                TextInput:
                    id: history_display
                    text: root.history_text
                    font_size: dp(16)
                    readonly: True
                    background_color: 0.15, 0.15, 0.15, 1
                    foreground_color: 1, 1, 1, 1
                    padding: [dp(10), dp(10), dp(10), dp(10)]

            Button:
                text: 'Очистить историю'
                font_size: dp(18)
                bold: True
                background_color: 0.8, 0.2, 0.2, 1
                background_normal: ''
                size_hint_y: None
                height: dp(45)
                on_press: root.clear_history()

    TabbedPanelItem:
        text: 'О программе'
        ScrollView:
            Label:
                text: root.about_text
                font_size: dp(18)
                color: 1, 1, 1, 1
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]
                padding: [dp(20), dp(20)]
                markup: True
''')


class ConverterApp(TabbedPanel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_once(self.post_init, 0.1)

    def post_init(self, dt):
        """Вызывается после полной инициализации"""
        if len(self.tab_list) > 0:
            self.switch_to(self.tab_list[0])  # Выбираем первую вкладку
        else:
            self.add_widget(Label(text='Добавьте вкладки'))  # Fallback

    def disable_default_tab(self, dt):
        self.current_tab = None


    def focus_first_tab(self, dt):
        self.switch_to(self.tab_list[0])

    history_text = StringProperty('')
    about_text = StringProperty('''
[b]UnDecimal[/b]

[color=00aaff]Версия 1.0[/color]

Мощный инструмент для конвертации:
- Систем счисления (2, 8, 10, 16)
- Единиц измерения данных (биты, байты, КБ, МБ, ГБ, ТБ)

[color=00ffaa]Особенности:[/color]
• Простой и удобный интерфейс
• Подробные результаты конвертации
• История всех операций
• Оптимизировано для мобильных устройств

[color=ffaa00]Разработчик:[/color]
Бадмаев Д.Д.


''')

    def validate_input(self, text, system):
        """Валидация в реальном времени"""
        if system == "Десятичная (10)":
            self.ids.num_input.foreground_color = (1, 1, 1, 1) if text.lstrip('-').isdigit() else (1, 0.5, 0.5, 1)
        elif system == "Двоичная (2)":
            self.ids.num_input.foreground_color = (1, 1, 1, 1) if all(c in '01' for c in text) else (1, 0.5, 0.5, 1)
        elif system == "Восьмеричная (8)":
            self.ids.num_input.foreground_color = (1, 1, 1, 1) if all(c in '01234567' for c in text) else (
                1, 0.5, 0.5, 1)
        elif system == "Шестнадцатеричная (16)":
            self.ids.num_input.foreground_color = (1, 1, 1, 1) if all(
                c.upper() in '0123456789ABCDEF' for c in text) else (1, 0.5, 0.5, 1)

    def full_validation(self, text, system):
        """Полная проверка перед конвертацией"""
        if not text:
            raise ValueError("Поле не может быть пустым")

    def convert_number(self):
        try:
            input_text = self.ids.num_input.text.strip()
            from_system = self.ids.from_system.text
            to_system = self.ids.to_system.text

            if not input_text:
                raise ValueError("Поле не может быть пустым")

            # Валидация ввода
            if "Десятичная" in from_system:
                if not input_text.lstrip('-').isdigit():
                    raise ValueError("Только цифры 0-9 и знак минус")
                input_num = int(input_text)

            elif "Двоичная" in from_system:
                if not all(c in '01' for c in input_text):
                    raise ValueError("Только 0 и 1")
                input_num = int(input_text, 2)

            elif "Восьмеричная" in from_system:
                if not all(c in '01234567' for c in input_text):
                    raise ValueError("Только цифры 0-7")
                input_num = int(input_text, 8)

            elif "Шестнадцатеричная" in from_system:
                cleaned_text = input_text.upper()
                if not all(c in '0123456789ABCDEF' for c in cleaned_text):
                    raise ValueError("Только 0-9 и A-F")
                input_num = int(cleaned_text, 16)

            # Конвертация
            if "Двоичная" in to_system:
                result = format(input_num, 'b')
            elif "Восьмеричная" in to_system:
                result = format(input_num, 'o')
            elif "Шестнадцатеричная" in to_system:
                result = format(input_num, 'X')
            else:
                result = str(input_num)

            self.ids.num_result.text = f"Результат: {result}"

        except ValueError as e:
            self.show_error(f"Ошибка ввода:\n{str(e)}")
        except Exception as e:
            self.show_error(f"Системная ошибка:\n{str(e)}")

    def show_error(self, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(
            text=message,
            color=(1, 1, 1, 1),
            font_size=dp(18),
            halign='center'
        ))
        btn = Button(
            text='OK',
            size_hint=(1, 0.3),
            background_color=(0.8, 0.2, 0.2, 1)
        )
        popup = Popup(
            title='[color=ff3333]ОШИБКА[/color]',
            title_size=dp(20),
            content=content,
            size_hint=(0.8, 0.4),
            separator_color=(1, 0, 0, 1),
            background='atlas://data/images/defaulttheme/button_pressed'
        )
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()

    def convert_data(self):
        try:
            value_text = self.ids.data_input.text.strip()
            from_unit = self.ids.from_unit.text.split()[0]
            to_unit = self.ids.to_unit.text.split()[0]

            if not value_text:
                raise ValueError("Пожалуйста, введите значение")

            value = float(value_text)
            if value < 0:
                raise ValueError("Значение должно быть положительным")

            # Конвертируем в биты сначала
            if from_unit == "Бит":
                bits = value
            elif from_unit == "Байт":
                bits = value * 8
            elif from_unit == "Килобайт":
                bits = value * 8 * 1024
            elif from_unit == "Мегабайт":
                bits = value * 8 * 1024 * 1024
            elif from_unit == "Гигабайт":
                bits = value * 8 * 1024 * 1024 * 1024
            elif from_unit == "Терабайт":
                bits = value * 8 * 1024 * 1024 * 1024 * 1024

            # Конвертируем из битов в целевую единицу
            if to_unit == "Бит":
                result = bits
            elif to_unit == "Байт":
                result = bits / 8
            elif to_unit == "Килобайт":
                result = bits / (8 * 1024)
            elif to_unit == "Мегабайт":
                result = bits / (8 * 1024 * 1024)
            elif to_unit == "Гигабайт":
                result = bits / (8 * 1024 * 1024 * 1024)
            elif to_unit == "Терабайт":
                result = bits / (8 * 1024 * 1024 * 1024 * 1024)

            explanation = (
                f"{value} {from_unit} = {result:.8f} {to_unit}\n\n"
                f"Этапы расчета:\n"
                f"1. Конвертируем {value} {from_unit} в биты: {bits} бит\n"
                f"2. Конвертируем биты в {to_unit}: {result:.8f}"
            )

            self.ids.data_result.text = explanation
            self.add_to_history(f"Конвертация данных: {value} {from_unit} - {result:.4f} {to_unit}")

        except ValueError as e:
            self.show_error(f"Некорректный ввод: {str(e)}")
        except Exception as e:
            self.show_error(f"Ошибка: {str(e)}")

    def add_to_history(self, entry):
        if self.history_text:
            self.history_text = f"{entry}\n{'=' * 50}\n{self.history_text}"
        else:
            self.history_text = entry

    def clear_history(self):
        self.history_text = ''


class ConverterProApp(App):
    def build(self):
        self.title = 'UnDecimal'
        return ConverterApp()


if __name__ == '__main__':
    ConverterProApp().run()