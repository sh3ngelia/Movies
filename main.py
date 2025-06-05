import sys
from PyQt5 import QtWidgets
from quiz import Ui_MainWindow
from movie_info import MovieInfoWindow
from PyQt5.QtCore import QTimer

class MovieApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals()

        self.timer_label = QtWidgets.QLabel("დრო: 0 წმ", self)
        self.timer_label.resize(200, 30)
        self.seconds = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.update_timer_position()
        
        self.movies_data = {
            "Interstellar": {
                "description": "ფილმი მოგვითხრობს არცისე შორეული მომავლის მოვლენებზე. ჩვენ ვიხილავთ დედამიწას სადაც მცენარეები პრაქტიკულად აღარ იზრდებიან, ადამიანებმა მთელი თავიანთი რესურსი ხორბლის მოყვანაში ჩადეს ეს პრაქტიკულად ერთადერთი საკვებია რომელიც მიმდინარე დროში მოიპოვება. მათ ესმით რომ ხორბლის პოტენციალიც მალე ამოიწურება...",
                "image": "MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
            },
            "The Martian": {
                "description": "მარსზე მისიის დროს მომხდარი შტორმის შემდეგ, მარკ უოტნი ჩამორჩა ეკიპაჟის წევრებს. ყველას ჰგონია რომ ის მოკვდა, მაგრამ უოტნი გადარჩა და მთელს პლანეტაზე მარტო აღმოჩნდა. ის ცდილობს გადარჩეს და დედამიწაზე დაბრუნდეს. ენდი უირის ამავე სახელწოდების რომანის ეკრანიზაცია. მარსიანელი",
                "image": "5BHuvQ6p9kfc091Z8RiFNhCwL4b.jpg"
            },
            "Hangover": {
                "description": "ბიჭებისთვის გამართლ წვეულებაზე სამმა მეგობარმა საქმრო დაკარგა. და ეს ქორწილამდე 40 საათით ადრე! ახლა მათ მოუწევთ მთელი თავისი აზრების აღდგენა, რომლებიც გაბრუებულია ალკოჰოლით, იმისათვის, რომ გაიგონ რა მოხდა.",
                "image": "MV5BNDI2MzBhNzgtOWYyOS00NDM2LWE0OGYtOGQ0M2FjMTI2NTllXkEyXkFqcGc@._V1_.jpg"
            }
        }


    def update_timer(self):
        self.seconds += 1
        self.timer_label.setText(f"დრო: {self.seconds} წმ")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_timer_position()

    def update_timer_position(self):
        x = 10
        y = self.height() - self.timer_label.height() - 10
        self.timer_label.move(x, y)

    def connect_signals(self):
        self.ui.pushButton.clicked.connect(lambda: self.show_movie_info("Interstellar"))
        self.ui.pushButton_2.clicked.connect(lambda: self.show_movie_info("The Martian"))
        self.ui.pushButton_3.clicked.connect(lambda: self.show_movie_info("Hangover"))
        self.ui.pushButton_4.clicked.connect(self.search_movie)

        self.ui.lineEdit.textChanged.connect(self.on_text_changed)

    def show_movie_info(self, movie_name):
        movie_data = self.movies_data[movie_name]
        info_window = MovieInfoWindow(
            movie_name,
            movie_data["description"],
            movie_data["image"],
            self
        )
        info_window.exec_()

    def search_movie(self):
        query = self.ui.lineEdit.text().lower().strip()
        found_movie = None
        for movie_name in self.movies_data.keys():
            if query in movie_name.lower():
                found_movie = movie_name
                break

        if found_movie:
            self.show_movie_info(found_movie)
        else:
            QtWidgets.QMessageBox.information(self, "შედეგი", "ფილმი ვერ მოიძებნა.")

    def on_text_changed(self, text):
        text = text.lower().strip()
        for movie_name in self.movies_data:
            if text in movie_name.lower():
                self.ui.lineEdit.setStyleSheet("background-color: rgb(200,255,200);")  
                return
        self.ui.lineEdit.setStyleSheet("background-color: rgb(255,200,200);")  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())