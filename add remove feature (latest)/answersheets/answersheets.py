from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window

# Set the window size for testing
Window.size = (310, 580)

class OMRDownloadScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(OMRDownloadScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text="Download OMR Sheet")
        self.add_widget(self.label)

        # File chooser for downloading OMR
        self.file_chooser = FileChooserListView(size_hint=(1, 0.8))
        self.add_widget(self.file_chooser)

        # Buttons to download or cancel
        btn_layout = BoxLayout(size_hint=(1, 0.2))
        self.download_btn = Button(text="Download")
        self.cancel_btn = Button(text="Cancel")
        self.cancel_btn.bind(on_press=self.dismiss_popup)
        btn_layout.add_widget(self.download_btn)
        btn_layout.add_widget(self.cancel_btn)

        self.add_widget(btn_layout)

    def dismiss_popup(self, *args):
        self.parent.parent.dismiss()

class CreateExamScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CreateExamScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Exam name input
        self.add_widget(Label(text="Exam Name"))
        self.exam_name = TextInput(hint_text="Enter Exam Name", multiline=False)
        self.add_widget(self.exam_name)

        # Number of questions input
        self.add_widget(Label(text="Number of Questions"))
        self.num_questions = TextInput(hint_text="Enter number of questions", multiline=False)
        self.add_widget(self.num_questions)

        # Buttons to Create or Cancel
        btn_layout = BoxLayout(size_hint=(1, 0.2))
        self.create_btn = Button(text="Create Exam")
        self.cancel_btn = Button(text="Cancel")
        self.cancel_btn.bind(on_press=self.dismiss_popup)
        btn_layout.add_widget(self.create_btn)
        btn_layout.add_widget(self.cancel_btn)

        self.add_widget(btn_layout)

    def dismiss_popup(self, *args):
        self.parent.parent.dismiss()


class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # Title for the App
        title = Label(text="Answer Sheets", size_hint=(1, 0.1))
        root.add_widget(title)

        # Button to create exam
        create_exam_btn = Button(text="Create Exam", size_hint=(1, 0.2))
        create_exam_btn.bind(on_press=self.open_create_exam_popup)
        root.add_widget(create_exam_btn)

        # Button to download OMR sheet
        download_omr_btn = Button(text="Download OMR Sheet", size_hint=(1, 0.2))
        download_omr_btn.bind(on_press=self.open_download_omr_popup)
        root.add_widget(download_omr_btn)

        # Button to Scan OMR (not fully functional as it requires OCR or external libraries)
        scan_omr_btn = Button(text="Scan OMR", size_hint=(1, 0.2))
        root.add_widget(scan_omr_btn)

        return root

    def open_create_exam_popup(self, instance):
        content = CreateExamScreen()
        popup = Popup(title="Create Exam", content=content, size_hint=(0.8, 0.8))
        popup.open()

    def open_download_omr_popup(self, instance):
        content = OMRDownloadScreen()
        popup = Popup(title="Download OMR", content=content, size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    MainApp().run()
