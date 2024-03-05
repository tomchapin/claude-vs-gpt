import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtGui import QIcon

class MoviePlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Player")
        self.setGeometry(100, 100, 800, 600)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_widget = QVideoWidget()

        self.play_button = QPushButton()
        self.play_button.setIcon(QIcon("play.png"))
        self.play_button.clicked.connect(self.play_video)

        self.pause_button = QPushButton()
        self.pause_button.setIcon(QIcon("pause.png"))
        self.pause_button.clicked.connect(self.pause_video)

        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon("stop.png"))
        self.stop_button.clicked.connect(self.stop_video)

        self.skip_backward_button = QPushButton()
        self.skip_backward_button.setIcon(QIcon("skip_backward.png"))
        self.skip_backward_button.clicked.connect(self.skip_backward)

        self.skip_forward_button = QPushButton()
        self.skip_forward_button.setIcon(QIcon("skip_forward.png"))
        self.skip_forward_button.clicked.connect(self.skip_forward)

        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        self.duration_label = QLabel()
        self.current_time_label = QLabel()

        self.open_button = QPushButton("Open Video")
        self.open_button.clicked.connect(self.open_file)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.skip_backward_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.pause_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.skip_forward_button)

        time_layout = QHBoxLayout()
        time_layout.addWidget(self.current_time_label)
        time_layout.addWidget(self.position_slider)
        time_layout.addWidget(self.duration_label)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.video_widget)
        main_layout.addLayout(control_layout)
        main_layout.addLayout(time_layout)
        main_layout.addWidget(self.open_button)

        self.setLayout(main_layout)

        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.stateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_current_time)
        self.timer.start(1000)

    def open_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Video Files (*.mp4 *.mkv *.avi *.flv *.wmv)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.play_video()

    def play_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

    def skip_backward(self):
        current_position = self.media_player.position()
        new_position = current_position - 10000  # Skip 10 seconds backward
        self.media_player.setPosition(new_position)

    def skip_forward(self):
        current_position = self.media_player.position()
        new_position = current_position + 10000  # Skip 10 seconds forward
        self.media_player.setPosition(new_position)

    def media_state_changed(self, state):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(QIcon("pause.png"))
        else:
            self.play_button.setIcon(QIcon("play.png"))

    def position_changed(self, position):
        self.position_slider.setValue(position)

    def duration_changed(self, duration):
        self.position_slider.setRange(0, duration)
        self.duration_label.setText(self.format_time(duration))

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_current_time(self):
        current_time = self.media_player.position()
        self.current_time_label.setText(self.format_time(current_time))

    def format_time(self, milliseconds):
        seconds = (milliseconds // 1000) % 60
        minutes = (milliseconds // (1000 * 60)) % 60
        hours = (milliseconds // (1000 * 60 * 60)) % 24
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MoviePlayer()
    player.show()
    sys.exit(app.exec_())