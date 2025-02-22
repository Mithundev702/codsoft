import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget,
    QListWidgetItem, QFrame, QCheckBox, QComboBox, QInputDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(300, 100, 500, 600)
        self.is_dark_mode = False
        self.tasks = []  # Stores (task_text, completed)
        self.init_ui()
        self.apply_light_theme()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Title
        self.title_label = QLabel("TODO LIST")
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)

        # Search and Filter
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search note...")
        self.search_input.textChanged.connect(self.update_task_list)
        search_layout.addWidget(self.search_input)

        self.filter_dropdown = QComboBox()
        self.filter_dropdown.addItems(["ALL", "Active", "Completed"])
        self.filter_dropdown.currentIndexChanged.connect(self.update_task_list)
        search_layout.addWidget(self.filter_dropdown)

        self.toggle_theme_btn = QPushButton("🌙")
        self.toggle_theme_btn.clicked.connect(self.toggle_theme)
        search_layout.addWidget(self.toggle_theme_btn)

        main_layout.addLayout(search_layout)

        # Task List
        self.task_list = QListWidget()
        main_layout.addWidget(self.task_list)

        # Floating Add Button
        self.add_button = QPushButton("+")
        self.add_button.setFixedSize(50, 50)
        self.add_button.clicked.connect(self.add_task)
        main_layout.addWidget(self.add_button, alignment=Qt.AlignRight)

        self.setLayout(main_layout)

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #ffffff; }
            QLabel { color: #000000; }
            QLineEdit, QListWidget, QComboBox { border: 1px solid #cccccc; border-radius: 5px; padding: 5px; }
            QPushButton { background-color: #6A5ACD; color: white; border-radius: 10px; font-size: 16px; }
            QPushButton:hover { background-color: #483D8B; }
        """)
        self.toggle_theme_btn.setText("🌙")
        self.is_dark_mode = False

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #1E1E1E; }
            QLabel { color: #ffffff; }
            QLineEdit, QListWidget, QComboBox { background-color: #2E2E2E; color: white; border: 1px solid #444444; border-radius: 5px; padding: 5px; }
            QPushButton { background-color: #6A5ACD; color: white; border-radius: 10px; font-size: 16px; }
            QPushButton:hover { background-color: #483D8B; }
        """)
        self.toggle_theme_btn.setText("☀️")
        self.is_dark_mode = True

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()

    def add_task(self):
        task_text, ok = QInputDialog.getText(self, "New Task", "Enter task:")
        if ok and task_text.strip():
            self.tasks.append((task_text.strip(), False))
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear()
        search_text = self.search_input.text().lower()
        filter_option = self.filter_dropdown.currentText()
        for task_text, completed in self.tasks:
            if search_text and search_text not in task_text.lower():
                continue
            if filter_option == "Active" and completed:
                continue
            if filter_option == "Completed" and not completed:
                continue
            self.create_task_item(task_text, completed)

    def create_task_item(self, text, completed):
        item = QListWidgetItem()
        frame = QFrame()
        layout = QHBoxLayout()
        checkbox = QCheckBox()
        checkbox.setChecked(completed)
        checkbox.stateChanged.connect(lambda state, t=text: self.toggle_task(t))
        layout.addWidget(checkbox)

        label = QLabel(text)
        label.setFont(QFont("Arial", 14))
        if completed:
            label.setStyleSheet("text-decoration: line-through; color: gray;")
        layout.addWidget(label)
        layout.addStretch()
        frame.setLayout(layout)
        item.setSizeHint(frame.sizeHint())
        self.task_list.addItem(item)
        self.task_list.setItemWidget(item, frame)

    def toggle_task(self, text):
        for i, (task_text, completed) in enumerate(self.tasks):
            if task_text == text:
                self.tasks[i] = (task_text, not completed)
                break
        self.update_task_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
