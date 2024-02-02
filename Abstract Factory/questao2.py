from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass

class Menu(ABC):
    @abstractmethod
    def render(self):
        pass

class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_text_box(self):
        pass

    @abstractmethod
    def create_menu(self):
        pass

class ModernButton(Button):
    def render(self):
        print("Renderizando um botão no estilo moderno")

class ModernTextBox(TextBox):
    def render(self):
        print("Renderizando uma caixa de texto no estilo moderno")

class ModernMenu(Menu):
    def render(self):
        print("Renderizando um menu no estilo moderno")

class ModernWidgetFactory(WidgetFactory):
    def create_button(self):
        return ModernButton()

    def create_text_box(self):
        return ModernTextBox()

    def create_menu(self):
        return ModernMenu()

class ClassicButton(Button):
    def render(self):
        print("Renderizando um botão no estilo clássico")

class ClassicTextBox(TextBox):
    def render(self):
        print("Renderizando uma caixa de texto no estilo clássico")

class ClassicMenu(Menu):
    def render(self):
        print("Renderizando um menu no estilo clássico")

class ClassicWidgetFactory(WidgetFactory):
    def create_button(self):
        return ClassicButton()

    def create_text_box(self):
        return ClassicTextBox()

    def create_menu(self):
        return ClassicMenu()

def test_widget_system(factory):
    button = factory.create_button()
    text_box = factory.create_text_box()
    menu = factory.create_menu()
    button.render()
    text_box.render()
    menu.render()

print("Testando o sistema de widgets com o estilo moderno")
modern_factory = ModernWidgetFactory()
test_widget_system(modern_factory)

print("Testando o sistema de widgets com o estilo clássico")
classic_factory = ClassicWidgetFactory()
test_widget_system(classic_factory)