import sys
import re
import requests  # Still imported but not used for fetching questions
import random
import html
from bs4 import BeautifulSoup  # Still imported but not used for fetching questions

# PyQt5 imports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QWidget, QRadioButton, QMessageBox, QLineEdit, QComboBox, QGroupBox, QSpinBox,
    QButtonGroup  # Import QButtonGroup
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt


# Define a class for managing question data (now hardcoded)
class DataRequest:
    """
    Manages question data, now sourced from a hardcoded list.
    """

    def __init__(self):
        """
        Initializes the hardcoded question data.
        """
        print("DataRequest initialized with hardcoded questions.")

        # Hardcoded questions from your provided PDF images (simplified for QLabel display)
        self.pdf_questions = [
            # Questions from the first PDF image (Digital Logic)
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many two input logic gates are required to construct the logic circuit for the expression F = ABC + A'BC'?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many times will carry be generated and how many times will carry be propagated if 872 is added to 1111 in an 8-bit binary number?",
                "correct_answer": "3,4",
                "incorrect_answers": ["2,2", "3,2", "4,3"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The 2's complement of (0101) base 2 is:",
                "correct_answer": "(1011) base 2",
                "incorrect_answers": ["(0101) base 2", "(1010) base 2", "(0011) base 2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The number of control lines for an 8 to 1 multiplexer is:",
                "correct_answer": "3",
                "incorrect_answers": ["2", "4", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many Flip-Flops are required for Mod-12 counter?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The binary code for Gray code 0100 is equivalent to:",
                "correct_answer": "0111",
                "incorrect_answers": ["0100", "0101", "0010"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A is a Boolean variable then, A+1 equals to:",
                "correct_answer": "1",
                "incorrect_answers": ["A", "0", "A"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The digital logic family which has minimum propagation delay is:",
                "correct_answer": "TTL",
                "incorrect_answers": ["RTL", "DTL", "CMOS"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If segments b, c, f and g are turned on for a seven segment display, the display will show:",
                "correct_answer": "4",
                "incorrect_answers": ["7", "3", "8"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The BCD sum of two decimal numbers, 4 and 6 is:",
                "correct_answer": "1010",
                "incorrect_answers": ["1000", "1001", "1011"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A, B and C are the Boolean variables, which of the following expression is the simplified expression for the given Boolean expression F(A,B,C) = A'BC' + ABC' + ABC?",
                "correct_answer": "A + C",
                "incorrect_answers": ["A + B", "A + C'", "A' + C"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The device which changes from parallel data to serial data is:",
                "correct_answer": "Encoder",
                "incorrect_answers": ["Demultiplexer", "Decoder", "Multiplexer"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A mod-6 up counter counts up to:",
                "correct_answer": "5",
                "incorrect_answers": ["6", "7", "26"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "An asynchronous binary counter constructed with JK flip-flops counts from 0 to 255. How many JK flip-flops are necessary for this counter?",
                "correct_answer": "8",
                "incorrect_answers": ["255", "32", "16"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Flip-flops are memory device which store:",
                "correct_answer": "one bit of information",
                "incorrect_answers": ["two bit of information", "three bit of information", "four bit of information"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following expression is correct for the given K-Map?\n\n(K-Map details: Row 0: 00=1, 01=1, 11=0, 10=0; Row 1: 00=0, 01=0, 11=0, 10=0; Row 2: 00=0, 01=0, 11=0, 10=0; Row 3: 00=1, 01=1, 11=0, 10=0)",
                "correct_answer": "B C'",
                "incorrect_answers": ["A B'", "B C + A'C D'", "B C + A'C D'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following represents the characteristic equation of SR flip flop?",
                "correct_answer": "Q(next) = S + R'Q",
                "incorrect_answers": ["Q(next) = S + RQ", "Q(next) = S + R'Q'", "Q(next) = S + RQ'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The figure below represents the state transition diagram of: (Image of state diagram: 00 <-> 01, 01 -> 11, 11 -> 10, 10 -> 00)",
                "correct_answer": "SR flip-flop",
                "incorrect_answers": ["JK flip-flop", "T flip-flop", "D flip-flop"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A decoder offers N inputs and maximum _______ output lines.",
                "correct_answer": "2^N",
                "incorrect_answers": ["N", "2N", "N^2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A 4-bit parallel input serial output shift register requires _______ D flip-flops and _______ SR gates respectively.",
                "correct_answer": "4 and 6",
                "incorrect_answers": ["4 and 3", "4 and 4", "4 and 2"]
            },
            # New questions from the second PDF image (Electronics)
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",  # Assuming easy as no specific difficulty indicated
                "question": "PN-junction diode is used for:",
                "correct_answer": "rectifier circuit",
                "incorrect_answers": ["amplifier", "oscillator", "bound holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Addition of pentavalent impurity to a pure semiconductor creates many:",
                "correct_answer": "electrons",
                "incorrect_answers": ["holes", "valence electrons", "free electrons"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following parameter will be very high in the CB configuration of a BJT?",
                "correct_answer": "output resistance",
                "incorrect_answers": ["current gain", "voltage gain", "input resistance"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of Rs required for an n-channel JFET with Vp = -10 V, IDSS = 40 mA, and VGS = -5V is:",
                "correct_answer": "250 ohm",
                "incorrect_answers": ["750 ohm", "1155 ohm", "1500 ohm"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of ripple factor in full wave rectifier circuit is nearly equal to:",
                "correct_answer": "0.48",
                "incorrect_answers": ["0.81", "1.21", "0.21"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following is NOT a necessary component in a clamper circuit?",
                "correct_answer": "Resistor",
                "incorrect_answers": ["Diode", "DC supply", "Capacitor"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input impedance of a transistor is:",
                "correct_answer": "very high",
                "incorrect_answers": ["low", "almost zero", "high"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The current amplification factor in CC configuration is:",
                "correct_answer": "1 + beta",
                "incorrect_answers": ["beta", "1/beta", "1 + alpha"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In BJT, the equation IC = alpha IE + ICEO is:",
                "correct_answer": "IC = alpha IE + ICEO",  # Keeping as is since it's an equation
                "incorrect_answers": ["IC = alpha IB + ICEO", "IC = beta IB + ICEO", "IC = beta IE + ICEO"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In a transistor, IC = 100 mA and IE = 100.2 mA, the value of beta is:",
                "correct_answer": "500",
                "incorrect_answers": ["1000", "1010", "100"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "As the temperature of a transistor goes up, the base-emitter resistance will:",
                "correct_answer": "decrease",
                "incorrect_answers": ["increase", "remains constant", "fluctuates"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "NPN transistors are preferred over NPN transistors because they have:",
                "correct_answer": "high mobility of electrons",
                "incorrect_answers": ["high mobility of holes", "high mobility of electrons compares to holes",
                                      "low mobility of holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input/output relationship of CB amplifier is:",
                "correct_answer": "180-degree",
                "incorrect_answers": ["0-degree", "90-degree", "270-degree"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The figure below is an example of: (Image of Op-Amp circuit)",
                "correct_answer": "inverting amplifier",
                "incorrect_answers": ["non-inverting amplifier", "differential amplifier", "voltage follower"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The cross-over distortion does not occur in:",
                "correct_answer": "Class A amplifier",
                "incorrect_answers": ["Class B amplifier", "Class C amplifier", "Class AB amplifier"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?",
                "correct_answer": "62.5 %",
                "incorrect_answers": ["75 %", "125 %", "50 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In case of Class A amplifier, the efficiency can be increased by transformer coupled concept by:",
                "correct_answer": "25 %",
                "incorrect_answers": ["12.5 %", "50 %", "75 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In Class B amplifier, the output current flows for:",
                "correct_answer": "less than half input cycle",
                "incorrect_answers": ["half input cycle", "more than half input cycle", "entire input cycle"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of very high gain, it converts into:",
                "correct_answer": "square wave",
                "incorrect_answers": ["triangular wave", "random wave", "sine wave"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The 'slew rate' of an operational amplifier indicates:",
                "correct_answer": "how fast its output current can be changed.",
                "incorrect_answers": ["how fast its output voltage can be changed.",
                                      "how fast its output power can be changed.",
                                      "how fast its output voltage can be changed."]
            }
        ]

    def fetch_questions(self, amount=None, category=None, difficulty=None, question_type=None):
        """
        Fetches questions from the hardcoded PDF questions list.
        Category, difficulty, and type filters are applied if specified.

        Returns:
            list: A list of question dictionaries based on filters.
        """
        filtered_questions = []
        for q in self.pdf_questions:
            match = True
            # Category filtering: 0 means "Any"
            if category is not None and category != 0 and q.get('category') != self.get_category_name(category):
                match = False
            # Difficulty filtering: "Any" means no filter
            if difficulty and difficulty != "Any" and q.get('difficulty') != difficulty:
                match = False
            # Type filtering: "Any" means no filter (removed from UI, but kept in logic for robustness)
            if question_type and question_type != "Any" and q.get('type') != question_type:
                match = False
            if match:
                filtered_questions.append(q)

        # Shuffle the filtered questions
        random.shuffle(filtered_questions)

        # Ensure 'amount' does not exceed available questions after filtering
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, show a message
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(None, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        return filtered_questions[:effective_amount]  # Return only the effective_amount of questions

    def fetch_categories(self):
        """
        Returns hardcoded categories based on the PDF questions.
        """
        # Extract unique categories from the hardcoded questions
        unique_categories = sorted(list(set(q['category'] for q in self.pdf_questions)))
        categories_dict = {i + 1: name for i, name in enumerate(unique_categories)}
        return categories_dict

    def get_category_name(self, category_id):
        """
        Helper to get category name from ID for hardcoded questions.
        """
        # Re-fetch categories to ensure it's up-to-date with hardcoded questions
        all_categories = self.fetch_categories()
        return all_categories.get(category_id)


class MainWindow(QMainWindow):
    """
    The main window of our PyQt5 quiz application.
    """

    def __init__(self):
        """
        Constructor for the MainWindow.
        Initializes the UI components and layout.
        """
        super().__init__()
        self.setWindowTitle("Quiz - quiz.ui")  # Window title from your screenshot
        self.setGeometry(100, 100, 800, 700)  # Adjusted size to fit the UI design

        self.data_requester = DataRequest()
        self.categories = {}
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None

        self.init_ui()
        self.load_categories()
        # Set spinbox max value to the number of hardcoded questions
        self.num_questions_spinbox.setRange(1, len(self.data_requester.pdf_questions))
        self.num_questions_spinbox.setValue(len(self.data_requester.pdf_questions))  # Default to all questions

    def init_ui(self):
        """
        Initializes the user interface elements and their layout based on the provided UI design.
        """
        # Central widget to hold all layouts
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # --- Top Bar Section (Matching your latest screenshot) ---
        top_bar_widget = QWidget()
        top_bar_layout = QHBoxLayout(top_bar_widget)
        top_bar_layout.setAlignment(Qt.AlignLeft)

        # "Type Here" QLineEdit
        self.type_here_input = QLineEdit()
        self.type_here_input.setPlaceholderText("Type Here")
        self.type_here_input.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        top_bar_layout.addWidget(self.type_here_input)

        # Add a stretch to push the "Quizz!" to the right
        top_bar_layout.addStretch(1)

        # Icon placeholder (using a QLabel for text "Quiz" as a placeholder for the icon)
        self.icon_label = QLabel("Quiz")  # Text representing the icon
        self.icon_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0; /* Light grey background for the icon area */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
                font-weight: bold;
                color: #555;
            }
        """)
        top_bar_layout.addWidget(self.icon_label)

        # Quizz! text label
        self.quiz_title_label = QLabel("Quizz!")
        self.quiz_title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #4CAF50; margin-left: 10px;")
        top_bar_layout.addWidget(self.quiz_title_label)

        # Add another stretch to push the "Quizz!" further right if needed, or balance
        top_bar_layout.addStretch(1)

        self.main_layout.addWidget(top_bar_widget)
        self.main_layout.addSpacing(10)  # Add some space after header

        # --- Settings Group Box ---
        self.settings_group_box = QGroupBox("Settings")
        self.settings_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        settings_layout = QVBoxLayout(self.settings_group_box)

        # Number of Questions and Difficulty
        num_difficulty_layout = QHBoxLayout()
        num_difficulty_layout.addWidget(QLabel("Number of Questions"))
        self.num_questions_spinbox = QSpinBox()
        self.num_questions_spinbox.setRange(1, 50)  # Will be updated after categories load
        self.num_questions_spinbox.setValue(10)
        num_difficulty_layout.addWidget(self.num_questions_spinbox)
        num_difficulty_layout.addSpacing(20)

        num_difficulty_layout.addWidget(QLabel("Select Difficulty"))
        self.difficulty_combo = QComboBox()
        # Removed "medium" difficulty option as requested
        self.difficulty_combo.addItems(["Any", "easy", "hard"])
        num_difficulty_layout.addWidget(self.difficulty_combo)
        num_difficulty_layout.addStretch(1)
        settings_layout.addLayout(num_difficulty_layout)

        # Category and Type (Type widgets removed as requested)
        category_type_layout = QHBoxLayout()
        category_type_layout.addWidget(QLabel("Select Category"))
        self.category_combo = QComboBox()
        self.category_combo.addItem("Any", 0)  # Default "Any" category with data 0
        category_type_layout.addWidget(self.category_combo)
        category_type_layout.addStretch(1)  # Stretch to fill the space where 'Select Type' used to be
        settings_layout.addLayout(category_type_layout)

        # Get New Question Button (within settings for now, can be moved)
        self.get_question_button = QPushButton("Get New Question")  # Reverted text
        self.get_question_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db; /* Blue color matching reference */
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
        """)
        self.get_question_button.clicked.connect(self.fetch_and_display_questions)
        settings_layout.addWidget(self.get_question_button)

        self.main_layout.addWidget(self.settings_group_box)
        self.main_layout.addSpacing(20)

        # --- Question Section ---
        self.question_group_box = QGroupBox("Question")
        self.question_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        question_layout = QVBoxLayout(self.question_group_box)

        # Category, Difficulty, and Question Counter
        question_info_layout = QHBoxLayout()
        question_info_layout.addWidget(QLabel("Category:"))
        self.current_category_label = QLabel("N/A")
        self.current_category_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_category_label)
        question_info_layout.addSpacing(20)

        question_info_layout.addWidget(QLabel("Difficulty:"))
        self.current_difficulty_label = QLabel("N/A")
        self.current_difficulty_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_difficulty_label)
        question_info_layout.addStretch(1)

        self.question_counter_label = QLabel("0/0")
        self.question_counter_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        question_info_layout.addWidget(self.question_counter_label)
        question_layout.addLayout(question_info_layout)

        # Question Text
        self.question_text_label = QLabel("Click 'Get New Question' to start the quiz!")
        self.question_text_label.setWordWrap(True)
        self.question_text_label.setStyleSheet("font-size: 18px; margin-top: 15px; margin-bottom: 20px;")
        question_layout.addWidget(self.question_text_label)

        # Answer Radio Buttons
        self.answer_buttons_layout = QVBoxLayout()
        self.radio_buttons = []
        self.answer_button_group = QButtonGroup(self)  # Initialize QButtonGroup
        self.answer_button_group.setExclusive(True)  # Ensure only one radio button can be selected at a time

        for i in range(4):  # Max 4 options for multiple choice
            radio_button = QRadioButton(f"Option {i + 1}")
            self.answer_button_group.addButton(radio_button, i)  # Add button to group with an ID
            self.answer_buttons_layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)
            radio_button.hide()  # Hide initially

        self.answer_button_group.buttonClicked.connect(self.on_answer_selected)  # Connect group signal
        question_layout.addLayout(self.answer_buttons_layout)

        # Action Buttons (Try Again, Check, Next)
        action_buttons_layout = QHBoxLayout()
        self.try_again_button = QPushButton("Try Again")
        self.try_again_button.clicked.connect(self.try_again)
        self.try_again_button.setEnabled(False)  # Disabled initially
        self.try_again_button.setStyleSheet("""
            QPushButton {
                background-color: #ffc107;
                color: #333;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
            QPushButton:pressed {
                background-color: #c69500;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.try_again_button)

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.check_answer)
        self.check_button.setEnabled(False)  # Disabled initially
        self.check_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #138496;
            }
            QPushButton:pressed {
                background-color: #0f6674;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.check_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setEnabled(False)  # Disabled initially
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.next_button)

        question_layout.addLayout(action_buttons_layout)
        self.main_layout.addWidget(self.question_group_box)

        self.main_layout.addStretch(1)  # Pushes content to the top

    def load_categories(self):
        """
        Populates the category combo box from hardcoded questions.
        """
        self.categories = self.data_requester.fetch_categories()
        if self.categories:
            self.category_combo.clear()
            self.category_combo.addItem("Any", 0)  # Add "Any" option first with data 0
            for cat_id, cat_name in sorted(self.categories.items(), key=lambda item: item[1]):
                self.category_combo.addItem(cat_name, cat_id)
        else:
            # If no categories are fetched (e.g., when using hardcoded questions),
            # ensure "Any" is still available and handle gracefully.
            if not self.category_combo.count():
                self.category_combo.addItem("Any", 0)
            print("Categories loaded from local data.")  # Changed message

    def fetch_and_display_questions(self):
        """
        Fetches questions based on selected settings from hardcoded data and displays the first one.
        """
        amount = self.num_questions_spinbox.value()
        category_id = self.category_combo.currentData()
        difficulty = self.difficulty_combo.currentText()
        if difficulty == "Any":
            difficulty = None

        # Removed question_type as it's no longer in the UI
        # question_type = self.type_combo.currentText()
        # if question_type == "Any":
        #     question_type = None

        print(f"--- Fetching Questions from Hardcoded Data ---")
        print(
            f"Requested: Amount={amount}, Category ID={category_id} ({self.category_combo.currentText()}), Difficulty={difficulty}")

        # Fetch questions based on filters from hardcoded data (removed question_type parameter)
        filtered_questions = self.data_requester.fetch_questions(
            amount=None,  # Amount is handled after filtering
            category=category_id,
            difficulty=difficulty,
            question_type=None  # Always pass None for type since it's removed from UI
        )

        # Determine the effective number of questions to display
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, inform the user
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(self, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        # Shuffle and select the effective_amount of questions
        random.shuffle(filtered_questions)
        self.current_questions = filtered_questions[:effective_amount]

        print(f"Actual questions to display: {len(self.current_questions)}")

        if self.current_questions:
            self.current_question_index = -1
            self.next_question()  # Display the first question
            self.get_question_button.setText("Restart Quiz")
        else:
            QMessageBox.warning(self, "No Questions",
                                "Could not find questions with the selected criteria in the local data. Please try different settings.")
            self.reset_quiz_state()

    def display_question(self):
        """
        Displays the current question and its answer options.
        """
        if not self.current_questions or self.current_question_index >= len(self.current_questions):
            self.reset_quiz_state()
            QMessageBox.information(self, "Quiz Finished", "You have completed all questions!")
            return

        question_data = self.current_questions[self.current_question_index]

        self.current_category_label.setText(question_data.get('category', 'N/A'))
        self.current_difficulty_label.setText(question_data.get('difficulty', 'N/A').capitalize())
        self.question_text_label.setText(question_data.get('question', ''))  # Display simplified text
        self.question_counter_label.setText(f"{self.current_question_index + 1}/{len(self.current_questions)}")

        # Prepare answers (correct + incorrect) and shuffle them
        all_answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        random.shuffle(all_answers)

        # Clear previous selections and update radio buttons
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for i, radio_button in enumerate(self.radio_buttons):
            if i < len(all_answers):
                radio_button.setText(all_answers[i])
                radio_button.setChecked(False)
                radio_button.show()
            else:
                radio_button.hide()  # Hide unused radio buttons
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.check_button.setEnabled(False)
        self.try_again_button.setEnabled(False)
        self.next_button.setEnabled(False)  # Only enable after checking or if quiz finishes

        # Enable radio buttons for interaction
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Reset styling

    def on_answer_selected(self, radio_button):
        """
        Handles selection of an answer by a radio button.
        """
        # The `radio_button` argument is automatically passed by QButtonGroup's buttonClicked signal
        self.selected_answer = radio_button.text()
        self.check_button.setEnabled(True)
        print(f"Selected answer: {self.selected_answer}")  # For debugging

    def check_answer(self):
        """
        Checks if the selected answer is correct and provides feedback.
        """
        if self.selected_answer is None:
            QMessageBox.warning(self, "No Answer Selected", "Please select an answer before checking.")
            return

        current_question = self.current_questions[self.current_question_index]
        correct_answer = current_question['correct_answer']

        # Disable radio buttons after checking
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(False)
            if radio_button.text() == correct_answer:
                radio_button.setStyleSheet("QRadioButton { color: green; font-weight: bold; }")
            elif radio_button.text() == self.selected_answer:
                radio_button.setStyleSheet("QRadioButton { color: red; font-weight: bold; }")

        if self.selected_answer == correct_answer:
            QMessageBox.information(self, "Correct!", "Your answer is correct!")
            self.next_button.setEnabled(True)
            self.try_again_button.setEnabled(False)
        else:
            QMessageBox.warning(self, "Incorrect",
                                f"Your answer is incorrect. The correct answer was: {correct_answer}")
            self.try_again_button.setEnabled(True)
            self.next_button.setEnabled(True)  # Allow moving to next question even if incorrect

        self.check_button.setEnabled(False)  # Disable check button after checking
        print("Answer checked.")  # For debugging

    def try_again(self):
        """
        Resets the current question for another attempt.
        """
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Clear styling
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(True)
        self.next_button.setEnabled(False)  # Disable next until checked again
        print("Try Again clicked.")  # For debugging

    def next_question(self):
        """
        Moves to the next question in the list.
        """
        self.current_question_index += (1)
        self.display_question()
        print(f"Moved to question {self.current_question_index + 1}.")  # For debugging

    def reset_quiz_state(self):
        """
        Resets the UI and internal state when the quiz ends or fails to load.
        """
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None
        self.question_text_label.setText("Click 'Get New Question' to start the quiz!")
        self.current_category_label.setText("N/A")
        self.current_difficulty_label.setText("N/A")
        self.question_counter_label.setText("0/0")

        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.hide()
            radio_button.setChecked(False)
            radio_button.setStyleSheet("")
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.get_question_button.setText("Get New Question")
        print("Quiz state reset.")  # For debugging


def main():
    """
    The main function to create and run the PyQt5 application.
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
import sys
import re
import requests  # Still imported but not used for fetching questions
import random
import html
from bs4 import BeautifulSoup  # Still imported but not used for fetching questions

# PyQt5 imports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QWidget, QRadioButton, QMessageBox, QLineEdit, QComboBox, QGroupBox, QSpinBox,
    QButtonGroup  # Import QButtonGroup
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt


# Define a class for managing question data (now hardcoded)
class DataRequest:
    """
    Manages question data, now sourced from a hardcoded list.
    """

    def __init__(self):
        """
        Initializes the hardcoded question data.
        """
        print("DataRequest initialized with hardcoded questions.")

        # Hardcoded questions from your provided PDF images (simplified for QLabel display)
        self.pdf_questions = [
            # Questions from the first PDF image (Digital Logic)
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many two input logic gates are required to construct the logic circuit for the expression F = ABC + A'BC'?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many times will carry be generated and how many times will carry be propagated if 872 is added to 1111 in an 8-bit binary number?",
                "correct_answer": "3,4",
                "incorrect_answers": ["2,2", "3,2", "4,3"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The 2's complement of (0101) base 2 is:",
                "correct_answer": "(1011) base 2",
                "incorrect_answers": ["(0101) base 2", "(1010) base 2", "(0011) base 2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The number of control lines for an 8 to 1 multiplexer is:",
                "correct_answer": "3",
                "incorrect_answers": ["2", "4", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many Flip-Flops are required for Mod-12 counter?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The binary code for Gray code 0100 is equivalent to:",
                "correct_answer": "0111",
                "incorrect_answers": ["0100", "0101", "0010"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A is a Boolean variable then, A+1 equals to:",
                "correct_answer": "1",
                "incorrect_answers": ["A", "0", "A"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The digital logic family which has minimum propagation delay is:",
                "correct_answer": "TTL",
                "incorrect_answers": ["RTL", "DTL", "CMOS"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If segments b, c, f and g are turned on for a seven segment display, the display will show:",
                "correct_answer": "4",
                "incorrect_answers": ["7", "3", "8"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The BCD sum of two decimal numbers, 4 and 6 is:",
                "correct_answer": "1010",
                "incorrect_answers": ["1000", "1001", "1011"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A, B and C are the Boolean variables, which of the following expression is the simplified expression for the given Boolean expression F(A,B,C) = A'BC' + ABC' + ABC?",
                "correct_answer": "A + C",
                "incorrect_answers": ["A + B", "A + C'", "A' + C"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The device which changes from parallel data to serial data is:",
                "correct_answer": "Encoder",
                "incorrect_answers": ["Demultiplexer", "Decoder", "Multiplexer"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A mod-6 up counter counts up to:",
                "correct_answer": "5",
                "incorrect_answers": ["6", "7", "26"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "An asynchronous binary counter constructed with JK flip-flops counts from 0 to 255. How many JK flip-flops are necessary for this counter?",
                "correct_answer": "8",
                "incorrect_answers": ["255", "32", "16"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Flip-flops are memory device which store:",
                "correct_answer": "one bit of information",
                "incorrect_answers": ["two bit of information", "three bit of information", "four bit of information"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following expression is correct for the given K-Map?\n\n(K-Map details: Row 0: 00=1, 01=1, 11=0, 10=0; Row 1: 00=0, 01=0, 11=0, 10=0; Row 2: 00=0, 01=0, 11=0, 10=0; Row 3: 00=1, 01=1, 11=0, 10=0)",
                "correct_answer": "B C'",
                "incorrect_answers": ["A B'", "B C + A'C D'", "B C + A'C D'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following represents the characteristic equation of SR flip flop?",
                "correct_answer": "Q(next) = S + R'Q",
                "incorrect_answers": ["Q(next) = S + RQ", "Q(next) = S + R'Q'", "Q(next) = S + RQ'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The figure below represents the state transition diagram of: (Image of state diagram: 00 <-> 01, 01 -> 11, 11 -> 10, 10 -> 00)",
                "correct_answer": "SR flip-flop",
                "incorrect_answers": ["JK flip-flop", "T flip-flop", "D flip-flop"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A decoder offers N inputs and maximum _______ output lines.",
                "correct_answer": "2^N",
                "incorrect_answers": ["N", "2N", "N^2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A 4-bit parallel input serial output shift register requires _______ D flip-flops and _______ SR gates respectively.",
                "correct_answer": "4 and 6",
                "incorrect_answers": ["4 and 3", "4 and 4", "4 and 2"]
            },
            # New questions from the second PDF image (Electronics)
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",  # Assuming easy as no specific difficulty indicated
                "question": "PN-junction diode is used for:",
                "correct_answer": "rectifier circuit",
                "incorrect_answers": ["amplifier", "oscillator", "bound holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Addition of pentavalent impurity to a pure semiconductor creates many:",
                "correct_answer": "electrons",
                "incorrect_answers": ["holes", "valence electrons", "free electrons"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following parameter will be very high in the CB configuration of a BJT?",
                "correct_answer": "output resistance",
                "incorrect_answers": ["current gain", "voltage gain", "input resistance"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of Rs required for an n-channel JFET with Vp = -10 V, IDSS = 40 mA, and VGS = -5V is:",
                "correct_answer": "250 ohm",
                "incorrect_answers": ["750 ohm", "1155 ohm", "1500 ohm"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of ripple factor in full wave rectifier circuit is nearly equal to:",
                "correct_answer": "0.48",
                "incorrect_answers": ["0.81", "1.21", "0.21"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following is NOT a necessary component in a clamper circuit?",
                "correct_answer": "Resistor",
                "incorrect_answers": ["Diode", "DC supply", "Capacitor"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input impedance of a transistor is:",
                "correct_answer": "very high",
                "incorrect_answers": ["low", "almost zero", "high"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The current amplification factor in CC configuration is:",
                "correct_answer": "1 + beta",
                "incorrect_answers": ["beta", "1/beta", "1 + alpha"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In BJT, the equation IC = alpha IE + ICEO is:",
                "correct_answer": "IC = alpha IE + ICEO",  # Keeping as is since it's an equation
                "incorrect_answers": ["IC = alpha IB + ICEO", "IC = beta IB + ICEO", "IC = beta IE + ICEO"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In a transistor, IC = 100 mA and IE = 100.2 mA, the value of beta is:",
                "correct_answer": "500",
                "incorrect_answers": ["1000", "1010", "100"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "As the temperature of a transistor goes up, the base-emitter resistance will:",
                "correct_answer": "decrease",
                "incorrect_answers": ["increase", "remains constant", "fluctuates"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "NPN transistors are preferred over NPN transistors because they have:",
                "correct_answer": "high mobility of electrons",
                "incorrect_answers": ["high mobility of holes", "high mobility of electrons compares to holes",
                                      "low mobility of holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input/output relationship of CB amplifier is:",
                "correct_answer": "180-degree",
                "incorrect_answers": ["0-degree", "90-degree", "270-degree"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The figure below is an example of: (Image of Op-Amp circuit)",
                "correct_answer": "inverting amplifier",
                "incorrect_answers": ["non-inverting amplifier", "differential amplifier", "voltage follower"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The cross-over distortion does not occur in:",
                "correct_answer": "Class A amplifier",
                "incorrect_answers": ["Class B amplifier", "Class C amplifier", "Class AB amplifier"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?",
                "correct_answer": "62.5 %",
                "incorrect_answers": ["75 %", "125 %", "50 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In case of Class A amplifier, the efficiency can be increased by transformer coupled concept by:",
                "correct_answer": "25 %",
                "incorrect_answers": ["12.5 %", "50 %", "75 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In Class B amplifier, the output current flows for:",
                "correct_answer": "less than half input cycle",
                "incorrect_answers": ["half input cycle", "more than half input cycle", "entire input cycle"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of very high gain, it converts into:",
                "correct_answer": "square wave",
                "incorrect_answers": ["triangular wave", "random wave", "sine wave"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The 'slew rate' of an operational amplifier indicates:",
                "correct_answer": "how fast its output current can be changed.",
                "incorrect_answers": ["how fast its output voltage can be changed.",
                                      "how fast its output power can be changed.",
                                      "how fast its output voltage can be changed."]
            }
        ]

    def fetch_questions(self, amount=None, category=None, difficulty=None, question_type=None):
        """
        Fetches questions from the hardcoded PDF questions list.
        Category, difficulty, and type filters are applied if specified.

        Returns:
            list: A list of question dictionaries based on filters.
        """
        filtered_questions = []
        for q in self.pdf_questions:
            match = True
            # Category filtering: 0 means "Any"
            if category is not None and category != 0 and q.get('category') != self.get_category_name(category):
                match = False
            # Difficulty filtering: "Any" means no filter
            if difficulty and difficulty != "Any" and q.get('difficulty') != difficulty:
                match = False
            # Type filtering: "Any" means no filter (removed from UI, but kept in logic for robustness)
            if question_type and question_type != "Any" and q.get('type') != question_type:
                match = False
            if match:
                filtered_questions.append(q)

        # Shuffle the filtered questions
        random.shuffle(filtered_questions)

        # Ensure 'amount' does not exceed available questions after filtering
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, show a message
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(None, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        return filtered_questions[:effective_amount]  # Return only the effective_amount of questions

    def fetch_categories(self):
        """
        Returns hardcoded categories based on the PDF questions.
        """
        # Extract unique categories from the hardcoded questions
        unique_categories = sorted(list(set(q['category'] for q in self.pdf_questions)))
        categories_dict = {i + 1: name for i, name in enumerate(unique_categories)}
        return categories_dict

    def get_category_name(self, category_id):
        """
        Helper to get category name from ID for hardcoded questions.
        """
        # Re-fetch categories to ensure it's up-to-date with hardcoded questions
        all_categories = self.fetch_categories()
        return all_categories.get(category_id)


class MainWindow(QMainWindow):
    """
    The main window of our PyQt5 quiz application.
    """

    def __init__(self):
        """
        Constructor for the MainWindow.
        Initializes the UI components and layout.
        """
        super().__init__()
        self.setWindowTitle("Quiz - quiz.ui")  # Window title from your screenshot
        self.setGeometry(100, 100, 800, 700)  # Adjusted size to fit the UI design

        self.data_requester = DataRequest()
        self.categories = {}
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None

        self.init_ui()
        self.load_categories()
        # Set spinbox max value to the number of hardcoded questions
        self.num_questions_spinbox.setRange(1, len(self.data_requester.pdf_questions))
        self.num_questions_spinbox.setValue(len(self.data_requester.pdf_questions))  # Default to all questions

    def init_ui(self):
        """
        Initializes the user interface elements and their layout based on the provided UI design.
        """
        # Central widget to hold all layouts
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # --- Top Bar Section (Matching your latest screenshot) ---
        top_bar_widget = QWidget()
        top_bar_layout = QHBoxLayout(top_bar_widget)
        top_bar_layout.setAlignment(Qt.AlignLeft)

        # "Type Here" QLineEdit
        self.type_here_input = QLineEdit()
        self.type_here_input.setPlaceholderText("Type Here")
        self.type_here_input.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        top_bar_layout.addWidget(self.type_here_input)

        # Add a stretch to push the "Quizz!" to the right
        top_bar_layout.addStretch(1)

        # Icon placeholder (using a QLabel for text "Quiz" as a placeholder for the icon)
        self.icon_label = QLabel("Quiz")  # Text representing the icon
        self.icon_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0; /* Light grey background for the icon area */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
                font-weight: bold;
                color: #555;
            }
        """)
        top_bar_layout.addWidget(self.icon_label)

        # Quizz! text label
        self.quiz_title_label = QLabel("Quizz!")
        self.quiz_title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #4CAF50; margin-left: 10px;")
        top_bar_layout.addWidget(self.quiz_title_label)

        # Add another stretch to push the "Quizz!" further right if needed, or balance
        top_bar_layout.addStretch(1)

        self.main_layout.addWidget(top_bar_widget)
        self.main_layout.addSpacing(10)  # Add some space after header

        # --- Settings Group Box ---
        self.settings_group_box = QGroupBox("Settings")
        self.settings_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        settings_layout = QVBoxLayout(self.settings_group_box)

        # Number of Questions and Difficulty
        num_difficulty_layout = QHBoxLayout()
        num_difficulty_layout.addWidget(QLabel("Number of Questions"))
        self.num_questions_spinbox = QSpinBox()
        self.num_questions_spinbox.setRange(1, 50)  # Will be updated after categories load
        self.num_questions_spinbox.setValue(10)
        num_difficulty_layout.addWidget(self.num_questions_spinbox)
        num_difficulty_layout.addSpacing(20)

        num_difficulty_layout.addWidget(QLabel("Select Difficulty"))
        self.difficulty_combo = QComboBox()
        # Removed "medium" difficulty option as requested
        self.difficulty_combo.addItems(["Any", "easy", "hard"])
        num_difficulty_layout.addWidget(self.difficulty_combo)
        num_difficulty_layout.addStretch(1)
        settings_layout.addLayout(num_difficulty_layout)

        # Category and Type (Type widgets removed as requested)
        category_type_layout = QHBoxLayout()
        category_type_layout.addWidget(QLabel("Select Category"))
        self.category_combo = QComboBox()
        self.category_combo.addItem("Any", 0)  # Default "Any" category with data 0
        category_type_layout.addWidget(self.category_combo)
        category_type_layout.addStretch(1)  # Stretch to fill the space where 'Select Type' used to be
        settings_layout.addLayout(category_type_layout)

        # Get New Question Button (within settings for now, can be moved)
        self.get_question_button = QPushButton("Get New Question")  # Reverted text
        self.get_question_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db; /* Blue color matching reference */
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
        """)
        self.get_question_button.clicked.connect(self.fetch_and_display_questions)
        settings_layout.addWidget(self.get_question_button)

        self.main_layout.addWidget(self.settings_group_box)
        self.main_layout.addSpacing(20)

        # --- Question Section ---
        self.question_group_box = QGroupBox("Question")
        self.question_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        question_layout = QVBoxLayout(self.question_group_box)

        # Category, Difficulty, and Question Counter
        question_info_layout = QHBoxLayout()
        question_info_layout.addWidget(QLabel("Category:"))
        self.current_category_label = QLabel("N/A")
        self.current_category_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_category_label)
        question_info_layout.addSpacing(20)

        question_info_layout.addWidget(QLabel("Difficulty:"))
        self.current_difficulty_label = QLabel("N/A")
        self.current_difficulty_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_difficulty_label)
        question_info_layout.addStretch(1)

        self.question_counter_label = QLabel("0/0")
        self.question_counter_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        question_info_layout.addWidget(self.question_counter_label)
        question_layout.addLayout(question_info_layout)

        # Question Text
        self.question_text_label = QLabel("Click 'Get New Question' to start the quiz!")
        self.question_text_label.setWordWrap(True)
        self.question_text_label.setStyleSheet("font-size: 18px; margin-top: 15px; margin-bottom: 20px;")
        question_layout.addWidget(self.question_text_label)

        # Answer Radio Buttons
        self.answer_buttons_layout = QVBoxLayout()
        self.radio_buttons = []
        self.answer_button_group = QButtonGroup(self)  # Initialize QButtonGroup
        self.answer_button_group.setExclusive(True)  # Ensure only one radio button can be selected at a time

        for i in range(4):  # Max 4 options for multiple choice
            radio_button = QRadioButton(f"Option {i + 1}")
            self.answer_button_group.addButton(radio_button, i)  # Add button to group with an ID
            self.answer_buttons_layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)
            radio_button.hide()  # Hide initially

        self.answer_button_group.buttonClicked.connect(self.on_answer_selected)  # Connect group signal
        question_layout.addLayout(self.answer_buttons_layout)

        # Action Buttons (Try Again, Check, Next)
        action_buttons_layout = QHBoxLayout()
        self.try_again_button = QPushButton("Try Again")
        self.try_again_button.clicked.connect(self.try_again)
        self.try_again_button.setEnabled(False)  # Disabled initially
        self.try_again_button.setStyleSheet("""
            QPushButton {
                background-color: #ffc107;
                color: #333;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
            QPushButton:pressed {
                background-color: #c69500;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.try_again_button)

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.check_answer)
        self.check_button.setEnabled(False)  # Disabled initially
        self.check_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #138496;
            }
            QPushButton:pressed {
                background-color: #0f6674;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.check_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setEnabled(False)  # Disabled initially
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.next_button)

        question_layout.addLayout(action_buttons_layout)
        self.main_layout.addWidget(self.question_group_box)

        self.main_layout.addStretch(1)  # Pushes content to the top

    def load_categories(self):
        """
        Populates the category combo box from hardcoded questions.
        """
        self.categories = self.data_requester.fetch_categories()
        if self.categories:
            self.category_combo.clear()
            self.category_combo.addItem("Any", 0)  # Add "Any" option first with data 0
            for cat_id, cat_name in sorted(self.categories.items(), key=lambda item: item[1]):
                self.category_combo.addItem(cat_name, cat_id)
        else:
            # If no categories are fetched (e.g., when using hardcoded questions),
            # ensure "Any" is still available and handle gracefully.
            if not self.category_combo.count():
                self.category_combo.addItem("Any", 0)
            print("Categories loaded from local data.")  # Changed message

    def fetch_and_display_questions(self):
        """
        Fetches questions based on selected settings from hardcoded data and displays the first one.
        """
        amount = self.num_questions_spinbox.value()
        category_id = self.category_combo.currentData()
        difficulty = self.difficulty_combo.currentText()
        if difficulty == "Any":
            difficulty = None

        # Removed question_type as it's no longer in the UI
        # question_type = self.type_combo.currentText()
        # if question_type == "Any":
        #     question_type = None

        print(f"--- Fetching Questions from Hardcoded Data ---")
        print(
            f"Requested: Amount={amount}, Category ID={category_id} ({self.category_combo.currentText()}), Difficulty={difficulty}")

        # Fetch questions based on filters from hardcoded data (removed question_type parameter)
        filtered_questions = self.data_requester.fetch_questions(
            amount=None,  # Amount is handled after filtering
            category=category_id,
            difficulty=difficulty,
            question_type=None  # Always pass None for type since it's removed from UI
        )

        # Determine the effective number of questions to display
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, inform the user
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(self, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        # Shuffle and select the effective_amount of questions
        random.shuffle(filtered_questions)
        self.current_questions = filtered_questions[:effective_amount]

        print(f"Actual questions to display: {len(self.current_questions)}")

        if self.current_questions:
            self.current_question_index = -1
            self.next_question()  # Display the first question
            self.get_question_button.setText("Restart Quiz")
        else:
            QMessageBox.warning(self, "No Questions",
                                "Could not find questions with the selected criteria in the local data. Please try different settings.")
            self.reset_quiz_state()

    def display_question(self):
        """
        Displays the current question and its answer options.
        """
        if not self.current_questions or self.current_question_index >= len(self.current_questions):
            self.reset_quiz_state()
            QMessageBox.information(self, "Quiz Finished", "You have completed all questions!")
            return

        question_data = self.current_questions[self.current_question_index]

        self.current_category_label.setText(question_data.get('category', 'N/A'))
        self.current_difficulty_label.setText(question_data.get('difficulty', 'N/A').capitalize())
        self.question_text_label.setText(question_data.get('question', ''))  # Display simplified text
        self.question_counter_label.setText(f"{self.current_question_index + 1}/{len(self.current_questions)}")

        # Prepare answers (correct + incorrect) and shuffle them
        all_answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        random.shuffle(all_answers)

        # Clear previous selections and update radio buttons
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for i, radio_button in enumerate(self.radio_buttons):
            if i < len(all_answers):
                radio_button.setText(all_answers[i])
                radio_button.setChecked(False)
                radio_button.show()
            else:
                radio_button.hide()  # Hide unused radio buttons
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.check_button.setEnabled(False)
        self.try_again_button.setEnabled(False)
        self.next_button.setEnabled(False)  # Only enable after checking or if quiz finishes

        # Enable radio buttons for interaction
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Reset styling

    def on_answer_selected(self, radio_button):
        """
        Handles selection of an answer by a radio button.
        """
        # The `radio_button` argument is automatically passed by QButtonGroup's buttonClicked signal
        self.selected_answer = radio_button.text()
        self.check_button.setEnabled(True)
        print(f"Selected answer: {self.selected_answer}")  # For debugging

    def check_answer(self):
        """
        Checks if the selected answer is correct and provides feedback.
        """
        if self.selected_answer is None:
            QMessageBox.warning(self, "No Answer Selected", "Please select an answer before checking.")
            return

        current_question = self.current_questions[self.current_question_index]
        correct_answer = current_question['correct_answer']

        # Disable radio buttons after checking
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(False)
            if radio_button.text() == correct_answer:
                radio_button.setStyleSheet("QRadioButton { color: green; font-weight: bold; }")
            elif radio_button.text() == self.selected_answer:
                radio_button.setStyleSheet("QRadioButton { color: red; font-weight: bold; }")

        if self.selected_answer == correct_answer:
            QMessageBox.information(self, "Correct!", "Your answer is correct!")
            self.next_button.setEnabled(True)
            self.try_again_button.setEnabled(False)
        else:
            QMessageBox.warning(self, "Incorrect",
                                f"Your answer is incorrect. The correct answer was: {correct_answer}")
            self.try_again_button.setEnabled(True)
            self.next_button.setEnabled(True)  # Allow moving to next question even if incorrect

        self.check_button.setEnabled(False)  # Disable check button after checking
        print("Answer checked.")  # For debugging

    def try_again(self):
        """
        Resets the current question for another attempt.
        """
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Clear styling
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(True)
        self.next_button.setEnabled(False)  # Disable next until checked again
        print("Try Again clicked.")  # For debugging

    def next_question(self):
        """
        Moves to the next question in the list.
        """
        self.current_question_index += (1)
        self.display_question()
        print(f"Moved to question {self.current_question_index + 1}.")  # For debugging

    def reset_quiz_state(self):
        """
        Resets the UI and internal state when the quiz ends or fails to load.
        """
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None
        self.question_text_label.setText("Click 'Get New Question' to start the quiz!")
        self.current_category_label.setText("N/A")
        self.current_difficulty_label.setText("N/A")
        self.question_counter_label.setText("0/0")

        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.hide()
            radio_button.setChecked(False)
            radio_button.setStyleSheet("")
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.get_question_button.setText("Get New Question")
        print("Quiz state reset.")  # For debugging


def main():
    """
    The main function to create and run the PyQt5 application.
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
import sys
import re
import requests  # Still imported but not used for fetching questions
import random
import html
from bs4 import BeautifulSoup  # Still imported but not used for fetching questions

# PyQt5 imports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QWidget, QRadioButton, QMessageBox, QLineEdit, QComboBox, QGroupBox, QSpinBox,
    QButtonGroup  # Import QButtonGroup
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt


# Define a class for managing question data (now hardcoded)
class DataRequest:
    """
    Manages question data, now sourced from a hardcoded list.
    """

    def __init__(self):
        """
        Initializes the hardcoded question data.
        """
        print("DataRequest initialized with hardcoded questions.")

        # Hardcoded questions from your provided PDF images (simplified for QLabel display)
        self.pdf_questions = [
            # Questions from the first PDF image (Digital Logic)
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many two input logic gates are required to construct the logic circuit for the expression F = ABC + A'BC'?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many times will carry be generated and how many times will carry be propagated if 872 is added to 1111 in an 8-bit binary number?",
                "correct_answer": "3,4",
                "incorrect_answers": ["2,2", "3,2", "4,3"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The 2's complement of (0101) base 2 is:",
                "correct_answer": "(1011) base 2",
                "incorrect_answers": ["(0101) base 2", "(1010) base 2", "(0011) base 2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The number of control lines for an 8 to 1 multiplexer is:",
                "correct_answer": "3",
                "incorrect_answers": ["2", "4", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many Flip-Flops are required for Mod-12 counter?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The binary code for Gray code 0100 is equivalent to:",
                "correct_answer": "0111",
                "incorrect_answers": ["0100", "0101", "0010"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A is a Boolean variable then, A+1 equals to:",
                "correct_answer": "1",
                "incorrect_answers": ["A", "0", "A"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The digital logic family which has minimum propagation delay is:",
                "correct_answer": "TTL",
                "incorrect_answers": ["RTL", "DTL", "CMOS"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If segments b, c, f and g are turned on for a seven segment display, the display will show:",
                "correct_answer": "4",
                "incorrect_answers": ["7", "3", "8"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The BCD sum of two decimal numbers, 4 and 6 is:",
                "correct_answer": "1010",
                "incorrect_answers": ["1000", "1001", "1011"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A, B and C are the Boolean variables, which of the following expression is the simplified expression for the given Boolean expression F(A,B,C) = A'BC' + ABC' + ABC?",
                "correct_answer": "A + C",
                "incorrect_answers": ["A + B", "A + C'", "A' + C"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The device which changes from parallel data to serial data is:",
                "correct_answer": "Encoder",
                "incorrect_answers": ["Demultiplexer", "Decoder", "Multiplexer"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A mod-6 up counter counts up to:",
                "correct_answer": "5",
                "incorrect_answers": ["6", "7", "26"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "An asynchronous binary counter constructed with JK flip-flops counts from 0 to 255. How many JK flip-flops are necessary for this counter?",
                "correct_answer": "8",
                "incorrect_answers": ["255", "32", "16"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Flip-flops are memory device which store:",
                "correct_answer": "one bit of information",
                "incorrect_answers": ["two bit of information", "three bit of information", "four bit of information"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following expression is correct for the given K-Map?\n\n(K-Map details: Row 0: 00=1, 01=1, 11=0, 10=0; Row 1: 00=0, 01=0, 11=0, 10=0; Row 2: 00=0, 01=0, 11=0, 10=0; Row 3: 00=1, 01=1, 11=0, 10=0)",
                "correct_answer": "B C'",
                "incorrect_answers": ["A B'", "B C + A'C D'", "B C + A'C D'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following represents the characteristic equation of SR flip flop?",
                "correct_answer": "Q(next) = S + R'Q",
                "incorrect_answers": ["Q(next) = S + RQ", "Q(next) = S + R'Q'", "Q(next) = S + RQ'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The figure below represents the state transition diagram of: (Image of state diagram: 00 <-> 01, 01 -> 11, 11 -> 10, 10 -> 00)",
                "correct_answer": "SR flip-flop",
                "incorrect_answers": ["JK flip-flop", "T flip-flop", "D flip-flop"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A decoder offers N inputs and maximum _______ output lines.",
                "correct_answer": "2^N",
                "incorrect_answers": ["N", "2N", "N^2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A 4-bit parallel input serial output shift register requires _______ D flip-flops and _______ SR gates respectively.",
                "correct_answer": "4 and 6",
                "incorrect_answers": ["4 and 3", "4 and 4", "4 and 2"]
            },
            # New questions from the second PDF image (Electronics)
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",  # Assuming easy as no specific difficulty indicated
                "question": "PN-junction diode is used for:",
                "correct_answer": "rectifier circuit",
                "incorrect_answers": ["amplifier", "oscillator", "bound holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Addition of pentavalent impurity to a pure semiconductor creates many:",
                "correct_answer": "electrons",
                "incorrect_answers": ["holes", "valence electrons", "free electrons"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following parameter will be very high in the CB configuration of a BJT?",
                "correct_answer": "output resistance",
                "incorrect_answers": ["current gain", "voltage gain", "input resistance"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of Rs required for an n-channel JFET with Vp = -10 V, IDSS = 40 mA, and VGS = -5V is:",
                "correct_answer": "250 ohm",
                "incorrect_answers": ["750 ohm", "1155 ohm", "1500 ohm"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of ripple factor in full wave rectifier circuit is nearly equal to:",
                "correct_answer": "0.48",
                "incorrect_answers": ["0.81", "1.21", "0.21"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following is NOT a necessary component in a clamper circuit?",
                "correct_answer": "Resistor",
                "incorrect_answers": ["Diode", "DC supply", "Capacitor"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input impedance of a transistor is:",
                "correct_answer": "very high",
                "incorrect_answers": ["low", "almost zero", "high"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The current amplification factor in CC configuration is:",
                "correct_answer": "1 + beta",
                "incorrect_answers": ["beta", "1/beta", "1 + alpha"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In BJT, the equation IC = alpha IE + ICEO is:",
                "correct_answer": "IC = alpha IE + ICEO",  # Keeping as is since it's an equation
                "incorrect_answers": ["IC = alpha IB + ICEO", "IC = beta IB + ICEO", "IC = beta IE + ICEO"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In a transistor, IC = 100 mA and IE = 100.2 mA, the value of beta is:",
                "correct_answer": "500",
                "incorrect_answers": ["1000", "1010", "100"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "As the temperature of a transistor goes up, the base-emitter resistance will:",
                "correct_answer": "decrease",
                "incorrect_answers": ["increase", "remains constant", "fluctuates"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "NPN transistors are preferred over NPN transistors because they have:",
                "correct_answer": "high mobility of electrons",
                "incorrect_answers": ["high mobility of holes", "high mobility of electrons compares to holes",
                                      "low mobility of holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input/output relationship of CB amplifier is:",
                "correct_answer": "180-degree",
                "incorrect_answers": ["0-degree", "90-degree", "270-degree"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The figure below is an example of: (Image of Op-Amp circuit)",
                "correct_answer": "inverting amplifier",
                "incorrect_answers": ["non-inverting amplifier", "differential amplifier", "voltage follower"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The cross-over distortion does not occur in:",
                "correct_answer": "Class A amplifier",
                "incorrect_answers": ["Class B amplifier", "Class C amplifier", "Class AB amplifier"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?",
                "correct_answer": "62.5 %",
                "incorrect_answers": ["75 %", "125 %", "50 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In case of Class A amplifier, the efficiency can be increased by transformer coupled concept by:",
                "correct_answer": "25 %",
                "incorrect_answers": ["12.5 %", "50 %", "75 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In Class B amplifier, the output current flows for:",
                "correct_answer": "less than half input cycle",
                "incorrect_answers": ["half input cycle", "more than half input cycle", "entire input cycle"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of very high gain, it converts into:",
                "correct_answer": "square wave",
                "incorrect_answers": ["triangular wave", "random wave", "sine wave"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The 'slew rate' of an operational amplifier indicates:",
                "correct_answer": "how fast its output current can be changed.",
                "incorrect_answers": ["how fast its output voltage can be changed.",
                                      "how fast its output power can be changed.",
                                      "how fast its output voltage can be changed."]
            }
        ]

    def fetch_questions(self, amount=None, category=None, difficulty=None, question_type=None):
        """
        Fetches questions from the hardcoded PDF questions list.
        Category, difficulty, and type filters are applied if specified.

        Returns:
            list: A list of question dictionaries based on filters.
        """
        filtered_questions = []
        for q in self.pdf_questions:
            match = True
            # Category filtering: 0 means "Any"
            if category is not None and category != 0 and q.get('category') != self.get_category_name(category):
                match = False
            # Difficulty filtering: "Any" means no filter
            if difficulty and difficulty != "Any" and q.get('difficulty') != difficulty:
                match = False
            # Type filtering: "Any" means no filter (removed from UI, but kept in logic for robustness)
            if question_type and question_type != "Any" and q.get('type') != question_type:
                match = False
            if match:
                filtered_questions.append(q)

        # Shuffle the filtered questions
        random.shuffle(filtered_questions)

        # Ensure 'amount' does not exceed available questions after filtering
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, show a message
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(None, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        return filtered_questions[:effective_amount]  # Return only the effective_amount of questions

    def fetch_categories(self):
        """
        Returns hardcoded categories based on the PDF questions.
        """
        # Extract unique categories from the hardcoded questions
        unique_categories = sorted(list(set(q['category'] for q in self.pdf_questions)))
        categories_dict = {i + 1: name for i, name in enumerate(unique_categories)}
        return categories_dict

    def get_category_name(self, category_id):
        """
        Helper to get category name from ID for hardcoded questions.
        """
        # Re-fetch categories to ensure it's up-to-date with hardcoded questions
        all_categories = self.fetch_categories()
        return all_categories.get(category_id)


class MainWindow(QMainWindow):
    """
    The main window of our PyQt5 quiz application.
    """

    def __init__(self):
        """
        Constructor for the MainWindow.
        Initializes the UI components and layout.
        """
        super().__init__()
        self.setWindowTitle("Quiz - quiz.ui")  # Window title from your screenshot
        self.setGeometry(100, 100, 800, 700)  # Adjusted size to fit the UI design

        self.data_requester = DataRequest()
        self.categories = {}
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None

        self.init_ui()
        self.load_categories()
        # Set spinbox max value to the number of hardcoded questions
        self.num_questions_spinbox.setRange(1, len(self.data_requester.pdf_questions))
        self.num_questions_spinbox.setValue(len(self.data_requester.pdf_questions))  # Default to all questions

    def init_ui(self):
        """
        Initializes the user interface elements and their layout based on the provided UI design.
        """
        # Central widget to hold all layouts
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # --- Top Bar Section (Matching your latest screenshot) ---
        top_bar_widget = QWidget()
        top_bar_layout = QHBoxLayout(top_bar_widget)
        top_bar_layout.setAlignment(Qt.AlignLeft)

        # "Type Here" QLineEdit
        self.type_here_input = QLineEdit()
        self.type_here_input.setPlaceholderText("Type Here")
        self.type_here_input.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        top_bar_layout.addWidget(self.type_here_input)

        # Add a stretch to push the "Quizz!" to the right
        top_bar_layout.addStretch(1)

        # Icon placeholder (using a QLabel for text "Quiz" as a placeholder for the icon)
        self.icon_label = QLabel("Quiz")  # Text representing the icon
        self.icon_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0; /* Light grey background for the icon area */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
                font-weight: bold;
                color: #555;
            }
        """)
        top_bar_layout.addWidget(self.icon_label)

        # Quizz! text label
        self.quiz_title_label = QLabel("Quizz!")
        self.quiz_title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #4CAF50; margin-left: 10px;")
        top_bar_layout.addWidget(self.quiz_title_label)

        # Add another stretch to push the "Quizz!" further right if needed, or balance
        top_bar_layout.addStretch(1)

        self.main_layout.addWidget(top_bar_widget)
        self.main_layout.addSpacing(10)  # Add some space after header

        # --- Settings Group Box ---
        self.settings_group_box = QGroupBox("Settings")
        self.settings_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        settings_layout = QVBoxLayout(self.settings_group_box)

        # Number of Questions and Difficulty
        num_difficulty_layout = QHBoxLayout()
        num_difficulty_layout.addWidget(QLabel("Number of Questions"))
        self.num_questions_spinbox = QSpinBox()
        self.num_questions_spinbox.setRange(1, 50)  # Will be updated after categories load
        self.num_questions_spinbox.setValue(10)
        num_difficulty_layout.addWidget(self.num_questions_spinbox)
        num_difficulty_layout.addSpacing(20)

        num_difficulty_layout.addWidget(QLabel("Select Difficulty"))
        self.difficulty_combo = QComboBox()
        # Removed "medium" difficulty option as requested
        self.difficulty_combo.addItems(["Any", "easy", "hard"])
        num_difficulty_layout.addWidget(self.difficulty_combo)
        num_difficulty_layout.addStretch(1)
        settings_layout.addLayout(num_difficulty_layout)

        # Category and Type (Type widgets removed as requested)
        category_type_layout = QHBoxLayout()
        category_type_layout.addWidget(QLabel("Select Category"))
        self.category_combo = QComboBox()
        self.category_combo.addItem("Any", 0)  # Default "Any" category with data 0
        category_type_layout.addWidget(self.category_combo)
        category_type_layout.addStretch(1)  # Stretch to fill the space where 'Select Type' used to be
        settings_layout.addLayout(category_type_layout)

        # Get New Question Button (within settings for now, can be moved)
        self.get_question_button = QPushButton("Get New Question")  # Reverted text
        self.get_question_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db; /* Blue color matching reference */
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
        """)
        self.get_question_button.clicked.connect(self.fetch_and_display_questions)
        settings_layout.addWidget(self.get_question_button)

        self.main_layout.addWidget(self.settings_group_box)
        self.main_layout.addSpacing(20)

        # --- Question Section ---
        self.question_group_box = QGroupBox("Question")
        self.question_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        question_layout = QVBoxLayout(self.question_group_box)

        # Category, Difficulty, and Question Counter
        question_info_layout = QHBoxLayout()
        question_info_layout.addWidget(QLabel("Category:"))
        self.current_category_label = QLabel("N/A")
        self.current_category_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_category_label)
        question_info_layout.addSpacing(20)

        question_info_layout.addWidget(QLabel("Difficulty:"))
        self.current_difficulty_label = QLabel("N/A")
        self.current_difficulty_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_difficulty_label)
        question_info_layout.addStretch(1)

        self.question_counter_label = QLabel("0/0")
        self.question_counter_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        question_info_layout.addWidget(self.question_counter_label)
        question_layout.addLayout(question_info_layout)

        # Question Text
        self.question_text_label = QLabel("Click 'Get New Question' to start the quiz!")
        self.question_text_label.setWordWrap(True)
        self.question_text_label.setStyleSheet("font-size: 18px; margin-top: 15px; margin-bottom: 20px;")
        question_layout.addWidget(self.question_text_label)

        # Answer Radio Buttons
        self.answer_buttons_layout = QVBoxLayout()
        self.radio_buttons = []
        self.answer_button_group = QButtonGroup(self)  # Initialize QButtonGroup
        self.answer_button_group.setExclusive(True)  # Ensure only one radio button can be selected at a time

        for i in range(4):  # Max 4 options for multiple choice
            radio_button = QRadioButton(f"Option {i + 1}")
            self.answer_button_group.addButton(radio_button, i)  # Add button to group with an ID
            self.answer_buttons_layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)
            radio_button.hide()  # Hide initially

        self.answer_button_group.buttonClicked.connect(self.on_answer_selected)  # Connect group signal
        question_layout.addLayout(self.answer_buttons_layout)

        # Action Buttons (Try Again, Check, Next)
        action_buttons_layout = QHBoxLayout()
        self.try_again_button = QPushButton("Try Again")
        self.try_again_button.clicked.connect(self.try_again)
        self.try_again_button.setEnabled(False)  # Disabled initially
        self.try_again_button.setStyleSheet("""
            QPushButton {
                background-color: #ffc107;
                color: #333;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
            QPushButton:pressed {
                background-color: #c69500;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.try_again_button)

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.check_answer)
        self.check_button.setEnabled(False)  # Disabled initially
        self.check_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #138496;
            }
            QPushButton:pressed {
                background-color: #0f6674;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.check_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setEnabled(False)  # Disabled initially
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.next_button)

        question_layout.addLayout(action_buttons_layout)
        self.main_layout.addWidget(self.question_group_box)

        self.main_layout.addStretch(1)  # Pushes content to the top

    def load_categories(self):
        """
        Populates the category combo box from hardcoded questions.
        """
        self.categories = self.data_requester.fetch_categories()
        if self.categories:
            self.category_combo.clear()
            self.category_combo.addItem("Any", 0)  # Add "Any" option first with data 0
            for cat_id, cat_name in sorted(self.categories.items(), key=lambda item: item[1]):
                self.category_combo.addItem(cat_name, cat_id)
        else:
            # If no categories are fetched (e.g., when using hardcoded questions),
            # ensure "Any" is still available and handle gracefully.
            if not self.category_combo.count():
                self.category_combo.addItem("Any", 0)
            print("Categories loaded from local data.")  # Changed message

    def fetch_and_display_questions(self):
        """
        Fetches questions based on selected settings from hardcoded data and displays the first one.
        """
        amount = self.num_questions_spinbox.value()
        category_id = self.category_combo.currentData()
        difficulty = self.difficulty_combo.currentText()
        if difficulty == "Any":
            difficulty = None

        # Removed question_type as it's no longer in the UI
        # question_type = self.type_combo.currentText()
        # if question_type == "Any":
        #     question_type = None

        print(f"--- Fetching Questions from Hardcoded Data ---")
        print(
            f"Requested: Amount={amount}, Category ID={category_id} ({self.category_combo.currentText()}), Difficulty={difficulty}")

        # Fetch questions based on filters from hardcoded data (removed question_type parameter)
        filtered_questions = self.data_requester.fetch_questions(
            amount=None,  # Amount is handled after filtering
            category=category_id,
            difficulty=difficulty,
            question_type=None  # Always pass None for type since it's removed from UI
        )

        # Determine the effective number of questions to display
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, inform the user
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(self, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        # Shuffle and select the effective_amount of questions
        random.shuffle(filtered_questions)
        self.current_questions = filtered_questions[:effective_amount]

        print(f"Actual questions to display: {len(self.current_questions)}")

        if self.current_questions:
            self.current_question_index = -1
            self.next_question()  # Display the first question
            self.get_question_button.setText("Restart Quiz")
        else:
            QMessageBox.warning(self, "No Questions",
                                "Could not find questions with the selected criteria in the local data. Please try different settings.")
            self.reset_quiz_state()

    def display_question(self):
        """
        Displays the current question and its answer options.
        """
        if not self.current_questions or self.current_question_index >= len(self.current_questions):
            self.reset_quiz_state()
            QMessageBox.information(self, "Quiz Finished", "You have completed all questions!")
            return

        question_data = self.current_questions[self.current_question_index]

        self.current_category_label.setText(question_data.get('category', 'N/A'))
        self.current_difficulty_label.setText(question_data.get('difficulty', 'N/A').capitalize())
        self.question_text_label.setText(question_data.get('question', ''))  # Display simplified text
        self.question_counter_label.setText(f"{self.current_question_index + 1}/{len(self.current_questions)}")

        # Prepare answers (correct + incorrect) and shuffle them
        all_answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        random.shuffle(all_answers)

        # Clear previous selections and update radio buttons
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for i, radio_button in enumerate(self.radio_buttons):
            if i < len(all_answers):
                radio_button.setText(all_answers[i])
                radio_button.setChecked(False)
                radio_button.show()
            else:
                radio_button.hide()  # Hide unused radio buttons
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.check_button.setEnabled(False)
        self.try_again_button.setEnabled(False)
        self.next_button.setEnabled(False)  # Only enable after checking or if quiz finishes

        # Enable radio buttons for interaction
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Reset styling

    def on_answer_selected(self, radio_button):
        """
        Handles selection of an answer by a radio button.
        """
        # The `radio_button` argument is automatically passed by QButtonGroup's buttonClicked signal
        self.selected_answer = radio_button.text()
        self.check_button.setEnabled(True)
        print(f"Selected answer: {self.selected_answer}")  # For debugging

    def check_answer(self):
        """
        Checks if the selected answer is correct and provides feedback.
        """
        if self.selected_answer is None:
            QMessageBox.warning(self, "No Answer Selected", "Please select an answer before checking.")
            return

        current_question = self.current_questions[self.current_question_index]
        correct_answer = current_question['correct_answer']

        # Disable radio buttons after checking
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(False)
            if radio_button.text() == correct_answer:
                radio_button.setStyleSheet("QRadioButton { color: green; font-weight: bold; }")
            elif radio_button.text() == self.selected_answer:
                radio_button.setStyleSheet("QRadioButton { color: red; font-weight: bold; }")

        if self.selected_answer == correct_answer:
            QMessageBox.information(self, "Correct!", "Your answer is correct!")
            self.next_button.setEnabled(True)
            self.try_again_button.setEnabled(False)
        else:
            QMessageBox.warning(self, "Incorrect",
                                f"Your answer is incorrect. The correct answer was: {correct_answer}")
            self.try_again_button.setEnabled(True)
            self.next_button.setEnabled(True)  # Allow moving to next question even if incorrect

        self.check_button.setEnabled(False)  # Disable check button after checking
        print("Answer checked.")  # For debugging

    def try_again(self):
        """
        Resets the current question for another attempt.
        """
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Clear styling
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(True)
        self.next_button.setEnabled(False)  # Disable next until checked again
        print("Try Again clicked.")  # For debugging

    def next_question(self):
        """
        Moves to the next question in the list.
        """
        self.current_question_index += (1)
        self.display_question()
        print(f"Moved to question {self.current_question_index + 1}.")  # For debugging

    def reset_quiz_state(self):
        """
        Resets the UI and internal state when the quiz ends or fails to load.
        """
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None
        self.question_text_label.setText("Click 'Get New Question' to start the quiz!")
        self.current_category_label.setText("N/A")
        self.current_difficulty_label.setText("N/A")
        self.question_counter_label.setText("0/0")

        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.hide()
            radio_button.setChecked(False)
            radio_button.setStyleSheet("")
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.get_question_button.setText("Get New Question")
        print("Quiz state reset.")  # For debugging


def main():
    """
    The main function to create and run the PyQt5 application.
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
import sys
import re
import requests  # Still imported but not used for fetching questions
import random
import html
from bs4 import BeautifulSoup  # Still imported but not used for fetching questions

# PyQt5 imports
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QWidget, QRadioButton, QMessageBox, QLineEdit, QComboBox, QGroupBox, QSpinBox,
    QButtonGroup  # Import QButtonGroup
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt


# Define a class for managing question data (now hardcoded)
class DataRequest:
    """
    Manages question data, now sourced from a hardcoded list.
    """

    def __init__(self):
        """
        Initializes the hardcoded question data.
        """
        print("DataRequest initialized with hardcoded questions.")

        # Hardcoded questions from your provided PDF images (simplified for QLabel display)
        self.pdf_questions = [
            # Questions from the first PDF image (Digital Logic)
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many two input logic gates are required to construct the logic circuit for the expression F = ABC + A'BC'?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many times will carry be generated and how many times will carry be propagated if 872 is added to 1111 in an 8-bit binary number?",
                "correct_answer": "3,4",
                "incorrect_answers": ["2,2", "3,2", "4,3"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The 2's complement of (0101) base 2 is:",
                "correct_answer": "(1011) base 2",
                "incorrect_answers": ["(0101) base 2", "(1010) base 2", "(0011) base 2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The number of control lines for an 8 to 1 multiplexer is:",
                "correct_answer": "3",
                "incorrect_answers": ["2", "4", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "How many Flip-Flops are required for Mod-12 counter?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The binary code for Gray code 0100 is equivalent to:",
                "correct_answer": "0111",
                "incorrect_answers": ["0100", "0101", "0010"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A is a Boolean variable then, A+1 equals to:",
                "correct_answer": "1",
                "incorrect_answers": ["A", "0", "A"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The digital logic family which has minimum propagation delay is:",
                "correct_answer": "TTL",
                "incorrect_answers": ["RTL", "DTL", "CMOS"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If segments b, c, f and g are turned on for a seven segment display, the display will show:",
                "correct_answer": "4",
                "incorrect_answers": ["7", "3", "8"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The BCD sum of two decimal numbers, 4 and 6 is:",
                "correct_answer": "1010",
                "incorrect_answers": ["1000", "1001", "1011"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "If A, B and C are the Boolean variables, which of the following expression is the simplified expression for the given Boolean expression F(A,B,C) = A'BC' + ABC' + ABC?",
                "correct_answer": "A + C",
                "incorrect_answers": ["A + B", "A + C'", "A' + C"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The device which changes from parallel data to serial data is:",
                "correct_answer": "Encoder",
                "incorrect_answers": ["Demultiplexer", "Decoder", "Multiplexer"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A mod-6 up counter counts up to:",
                "correct_answer": "5",
                "incorrect_answers": ["6", "7", "26"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "An asynchronous binary counter constructed with JK flip-flops counts from 0 to 255. How many JK flip-flops are necessary for this counter?",
                "correct_answer": "8",
                "incorrect_answers": ["255", "32", "16"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Flip-flops are memory device which store:",
                "correct_answer": "one bit of information",
                "incorrect_answers": ["two bit of information", "three bit of information", "four bit of information"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following expression is correct for the given K-Map?\n\n(K-Map details: Row 0: 00=1, 01=1, 11=0, 10=0; Row 1: 00=0, 01=0, 11=0, 10=0; Row 2: 00=0, 01=0, 11=0, 10=0; Row 3: 00=1, 01=1, 11=0, 10=0)",
                "correct_answer": "B C'",
                "incorrect_answers": ["A B'", "B C + A'C D'", "B C + A'C D'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "Which of the following represents the characteristic equation of SR flip flop?",
                "correct_answer": "Q(next) = S + R'Q",
                "incorrect_answers": ["Q(next) = S + RQ", "Q(next) = S + R'Q'", "Q(next) = S + RQ'"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "The figure below represents the state transition diagram of: (Image of state diagram: 00 <-> 01, 01 -> 11, 11 -> 10, 10 -> 00)",
                "correct_answer": "SR flip-flop",
                "incorrect_answers": ["JK flip-flop", "T flip-flop", "D flip-flop"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A decoder offers N inputs and maximum _______ output lines.",
                "correct_answer": "2^N",
                "incorrect_answers": ["N", "2N", "N^2"]
            },
            {
                "category": "Digital Logic",
                "type": "multiple",
                "difficulty": "medium",
                "question": "A 4-bit parallel input serial output shift register requires _______ D flip-flops and _______ SR gates respectively.",
                "correct_answer": "4 and 6",
                "incorrect_answers": ["4 and 3", "4 and 4", "4 and 2"]
            },
            # New questions from the second PDF image (Electronics)
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",  # Assuming easy as no specific difficulty indicated
                "question": "PN-junction diode is used for:",
                "correct_answer": "rectifier circuit",
                "incorrect_answers": ["amplifier", "oscillator", "bound holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Addition of pentavalent impurity to a pure semiconductor creates many:",
                "correct_answer": "electrons",
                "incorrect_answers": ["holes", "valence electrons", "free electrons"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following parameter will be very high in the CB configuration of a BJT?",
                "correct_answer": "output resistance",
                "incorrect_answers": ["current gain", "voltage gain", "input resistance"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of Rs required for an n-channel JFET with Vp = -10 V, IDSS = 40 mA, and VGS = -5V is:",
                "correct_answer": "250 ohm",
                "incorrect_answers": ["750 ohm", "1155 ohm", "1500 ohm"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The value of ripple factor in full wave rectifier circuit is nearly equal to:",
                "correct_answer": "0.48",
                "incorrect_answers": ["0.81", "1.21", "0.21"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "Which of the following is NOT a necessary component in a clamper circuit?",
                "correct_answer": "Resistor",
                "incorrect_answers": ["Diode", "DC supply", "Capacitor"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input impedance of a transistor is:",
                "correct_answer": "very high",
                "incorrect_answers": ["low", "almost zero", "high"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The current amplification factor in CC configuration is:",
                "correct_answer": "1 + beta",
                "incorrect_answers": ["beta", "1/beta", "1 + alpha"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In BJT, the equation IC = alpha IE + ICEO is:",
                "correct_answer": "IC = alpha IE + ICEO",  # Keeping as is since it's an equation
                "incorrect_answers": ["IC = alpha IB + ICEO", "IC = beta IB + ICEO", "IC = beta IE + ICEO"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In a transistor, IC = 100 mA and IE = 100.2 mA, the value of beta is:",
                "correct_answer": "500",
                "incorrect_answers": ["1000", "1010", "100"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "As the temperature of a transistor goes up, the base-emitter resistance will:",
                "correct_answer": "decrease",
                "incorrect_answers": ["increase", "remains constant", "fluctuates"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "NPN transistors are preferred over NPN transistors because they have:",
                "correct_answer": "high mobility of electrons",
                "incorrect_answers": ["high mobility of holes", "high mobility of electrons compares to holes",
                                      "low mobility of holes"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The input/output relationship of CB amplifier is:",
                "correct_answer": "180-degree",
                "incorrect_answers": ["0-degree", "90-degree", "270-degree"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The figure below is an example of: (Image of Op-Amp circuit)",
                "correct_answer": "inverting amplifier",
                "incorrect_answers": ["non-inverting amplifier", "differential amplifier", "voltage follower"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The cross-over distortion does not occur in:",
                "correct_answer": "Class A amplifier",
                "incorrect_answers": ["Class B amplifier", "Class C amplifier", "Class AB amplifier"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?",
                "correct_answer": "62.5 %",
                "incorrect_answers": ["75 %", "125 %", "50 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In case of Class A amplifier, the efficiency can be increased by transformer coupled concept by:",
                "correct_answer": "25 %",
                "incorrect_answers": ["12.5 %", "50 %", "75 %"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "In Class B amplifier, the output current flows for:",
                "correct_answer": "less than half input cycle",
                "incorrect_answers": ["half input cycle", "more than half input cycle", "entire input cycle"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of very high gain, it converts into:",
                "correct_answer": "square wave",
                "incorrect_answers": ["triangular wave", "random wave", "sine wave"]
            },
            {
                "category": "Electronics",
                "type": "multiple",
                "difficulty": "easy",
                "question": "The 'slew rate' of an operational amplifier indicates:",
                "correct_answer": "how fast its output current can be changed.",
                "incorrect_answers": ["how fast its output voltage can be changed.",
                                      "how fast its output power can be changed.",
                                      "how fast its output voltage can be changed."]
            }
        ]

    def fetch_questions(self, amount=None, category=None, difficulty=None, question_type=None):
        """
        Fetches questions from the hardcoded PDF questions list.
        Category, difficulty, and type filters are applied if specified.

        Returns:
            list: A list of question dictionaries based on filters.
        """
        filtered_questions = []
        for q in self.pdf_questions:
            match = True
            # Category filtering: 0 means "Any"
            if category is not None and category != 0 and q.get('category') != self.get_category_name(category):
                match = False
            # Difficulty filtering: "Any" means no filter
            if difficulty and difficulty != "Any" and q.get('difficulty') != difficulty:
                match = False
            # Type filtering: "Any" means no filter (removed from UI, but kept in logic for robustness)
            if question_type and question_type != "Any" and q.get('type') != question_type:
                match = False
            if match:
                filtered_questions.append(q)

        # Shuffle the filtered questions
        random.shuffle(filtered_questions)

        # Ensure 'amount' does not exceed available questions after filtering
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, show a message
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(None, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        return filtered_questions[:effective_amount]  # Return only the effective_amount of questions

    def fetch_categories(self):
        """
        Returns hardcoded categories based on the PDF questions.
        """
        # Extract unique categories from the hardcoded questions
        unique_categories = sorted(list(set(q['category'] for q in self.pdf_questions)))
        categories_dict = {i + 1: name for i, name in enumerate(unique_categories)}
        return categories_dict

    def get_category_name(self, category_id):
        """
        Helper to get category name from ID for hardcoded questions.
        """
        # Re-fetch categories to ensure it's up-to-date with hardcoded questions
        all_categories = self.fetch_categories()
        return all_categories.get(category_id)


class MainWindow(QMainWindow):
    """
    The main window of our PyQt5 quiz application.
    """

    def __init__(self):
        """
        Constructor for the MainWindow.
        Initializes the UI components and layout.
        """
        super().__init__()
        self.setWindowTitle("Quiz - quiz.ui")  # Window title from your screenshot
        self.setGeometry(100, 100, 800, 700)  # Adjusted size to fit the UI design

        self.data_requester = DataRequest()
        self.categories = {}
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None

        self.init_ui()
        self.load_categories()
        # Set spinbox max value to the number of hardcoded questions
        self.num_questions_spinbox.setRange(1, len(self.data_requester.pdf_questions))
        self.num_questions_spinbox.setValue(len(self.data_requester.pdf_questions))  # Default to all questions

    def init_ui(self):
        """
        Initializes the user interface elements and their layout based on the provided UI design.
        """
        # Central widget to hold all layouts
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # --- Top Bar Section (Matching your latest screenshot) ---
        top_bar_widget = QWidget()
        top_bar_layout = QHBoxLayout(top_bar_widget)
        top_bar_layout.setAlignment(Qt.AlignLeft)

        # "Type Here" QLineEdit
        self.type_here_input = QLineEdit()
        self.type_here_input.setPlaceholderText("Type Here")
        self.type_here_input.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        top_bar_layout.addWidget(self.type_here_input)

        # Add a stretch to push the "Quizz!" to the right
        top_bar_layout.addStretch(1)

        # Icon placeholder (using a QLabel for text "Quiz" as a placeholder for the icon)
        self.icon_label = QLabel("Quiz")  # Text representing the icon
        self.icon_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0; /* Light grey background for the icon area */
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
                font-weight: bold;
                color: #555;
            }
        """)
        top_bar_layout.addWidget(self.icon_label)

        # Quizz! text label
        self.quiz_title_label = QLabel("Quizz!")
        self.quiz_title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #4CAF50; margin-left: 10px;")
        top_bar_layout.addWidget(self.quiz_title_label)

        # Add another stretch to push the "Quizz!" further right if needed, or balance
        top_bar_layout.addStretch(1)

        self.main_layout.addWidget(top_bar_widget)
        self.main_layout.addSpacing(10)  # Add some space after header

        # --- Settings Group Box ---
        self.settings_group_box = QGroupBox("Settings")
        self.settings_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        settings_layout = QVBoxLayout(self.settings_group_box)

        # Number of Questions and Difficulty
        num_difficulty_layout = QHBoxLayout()
        num_difficulty_layout.addWidget(QLabel("Number of Questions"))
        self.num_questions_spinbox = QSpinBox()
        self.num_questions_spinbox.setRange(1, 50)  # Will be updated after categories load
        self.num_questions_spinbox.setValue(10)
        num_difficulty_layout.addWidget(self.num_questions_spinbox)
        num_difficulty_layout.addSpacing(20)

        num_difficulty_layout.addWidget(QLabel("Select Difficulty"))
        self.difficulty_combo = QComboBox()
        # Removed "medium" difficulty option as requested
        self.difficulty_combo.addItems(["Any", "easy", "hard"])
        num_difficulty_layout.addWidget(self.difficulty_combo)
        num_difficulty_layout.addStretch(1)
        settings_layout.addLayout(num_difficulty_layout)

        # Category and Type (Type widgets removed as requested)
        category_type_layout = QHBoxLayout()
        category_type_layout.addWidget(QLabel("Select Category"))
        self.category_combo = QComboBox()
        self.category_combo.addItem("Any", 0)  # Default "Any" category with data 0
        category_type_layout.addWidget(self.category_combo)
        category_type_layout.addStretch(1)  # Stretch to fill the space where 'Select Type' used to be
        settings_layout.addLayout(category_type_layout)

        # Get New Question Button (within settings for now, can be moved)
        self.get_question_button = QPushButton("Get New Question")  # Reverted text
        self.get_question_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db; /* Blue color matching reference */
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
        """)
        self.get_question_button.clicked.connect(self.fetch_and_display_questions)
        settings_layout.addWidget(self.get_question_button)

        self.main_layout.addWidget(self.settings_group_box)
        self.main_layout.addSpacing(20)

        # --- Question Section ---
        self.question_group_box = QGroupBox("Question")
        self.question_group_box.setStyleSheet(
            "QGroupBox { font-weight: bold; margin-top: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        question_layout = QVBoxLayout(self.question_group_box)

        # Category, Difficulty, and Question Counter
        question_info_layout = QHBoxLayout()
        question_info_layout.addWidget(QLabel("Category:"))
        self.current_category_label = QLabel("N/A")
        self.current_category_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_category_label)
        question_info_layout.addSpacing(20)

        question_info_layout.addWidget(QLabel("Difficulty:"))
        self.current_difficulty_label = QLabel("N/A")
        self.current_difficulty_label.setStyleSheet("font-weight: bold;")
        question_info_layout.addWidget(self.current_difficulty_label)
        question_info_layout.addStretch(1)

        self.question_counter_label = QLabel("0/0")
        self.question_counter_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        question_info_layout.addWidget(self.question_counter_label)
        question_layout.addLayout(question_info_layout)

        # Question Text
        self.question_text_label = QLabel("Click 'Get New Question' to start the quiz!")
        self.question_text_label.setWordWrap(True)
        self.question_text_label.setStyleSheet("font-size: 18px; margin-top: 15px; margin-bottom: 20px;")
        question_layout.addWidget(self.question_text_label)

        # Answer Radio Buttons
        self.answer_buttons_layout = QVBoxLayout()
        self.radio_buttons = []
        self.answer_button_group = QButtonGroup(self)  # Initialize QButtonGroup
        self.answer_button_group.setExclusive(True)  # Ensure only one radio button can be selected at a time

        for i in range(4):  # Max 4 options for multiple choice
            radio_button = QRadioButton(f"Option {i + 1}")
            self.answer_button_group.addButton(radio_button, i)  # Add button to group with an ID
            self.answer_buttons_layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)
            radio_button.hide()  # Hide initially

        self.answer_button_group.buttonClicked.connect(self.on_answer_selected)  # Connect group signal
        question_layout.addLayout(self.answer_buttons_layout)

        # Action Buttons (Try Again, Check, Next)
        action_buttons_layout = QHBoxLayout()
        self.try_again_button = QPushButton("Try Again")
        self.try_again_button.clicked.connect(self.try_again)
        self.try_again_button.setEnabled(False)  # Disabled initially
        self.try_again_button.setStyleSheet("""
            QPushButton {
                background-color: #ffc107;
                color: #333;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
            QPushButton:pressed {
                background-color: #c69500;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.try_again_button)

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.check_answer)
        self.check_button.setEnabled(False)  # Disabled initially
        self.check_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #138496;
            }
            QPushButton:pressed {
                background-color: #0f6674;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.check_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setEnabled(False)  # Disabled initially
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                border: none;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
                box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.3);
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        action_buttons_layout.addWidget(self.next_button)

        question_layout.addLayout(action_buttons_layout)
        self.main_layout.addWidget(self.question_group_box)

        self.main_layout.addStretch(1)  # Pushes content to the top

    def load_categories(self):
        """
        Populates the category combo box from hardcoded questions.
        """
        self.categories = self.data_requester.fetch_categories()
        if self.categories:
            self.category_combo.clear()
            self.category_combo.addItem("Any", 0)  # Add "Any" option first with data 0
            for cat_id, cat_name in sorted(self.categories.items(), key=lambda item: item[1]):
                self.category_combo.addItem(cat_name, cat_id)
        else:
            # If no categories are fetched (e.g., when using hardcoded questions),
            # ensure "Any" is still available and handle gracefully.
            if not self.category_combo.count():
                self.category_combo.addItem("Any", 0)
            print("Categories loaded from local data.")  # Changed message

    def fetch_and_display_questions(self):
        """
        Fetches questions based on selected settings from hardcoded data and displays the first one.
        """
        amount = self.num_questions_spinbox.value()
        category_id = self.category_combo.currentData()
        difficulty = self.difficulty_combo.currentText()
        if difficulty == "Any":
            difficulty = None

        # Removed question_type as it's no longer in the UI
        # question_type = self.type_combo.currentText()
        # if question_type == "Any":
        #     question_type = None

        print(f"--- Fetching Questions from Hardcoded Data ---")
        print(
            f"Requested: Amount={amount}, Category ID={category_id} ({self.category_combo.currentText()}), Difficulty={difficulty}")

        # Fetch questions based on filters from hardcoded data (removed question_type parameter)
        filtered_questions = self.data_requester.fetch_questions(
            amount=None,  # Amount is handled after filtering
            category=category_id,
            difficulty=difficulty,
            question_type=None  # Always pass None for type since it's removed from UI
        )

        # Determine the effective number of questions to display
        effective_amount = min(amount, len(filtered_questions)) if amount else len(filtered_questions)

        # If fewer questions are available than requested, inform the user
        if amount and len(filtered_questions) < amount:
            QMessageBox.information(self, "Info",
                                    f"Only {len(filtered_questions)} questions available for selected criteria. Displaying all {len(filtered_questions)}.")

        # Shuffle and select the effective_amount of questions
        random.shuffle(filtered_questions)
        self.current_questions = filtered_questions[:effective_amount]

        print(f"Actual questions to display: {len(self.current_questions)}")

        if self.current_questions:
            self.current_question_index = -1
            self.next_question()  # Display the first question
            self.get_question_button.setText("Restart Quiz")
        else:
            QMessageBox.warning(self, "No Questions",
                                "Could not find questions with the selected criteria in the local data. Please try different settings.")
            self.reset_quiz_state()

    def display_question(self):
        """
        Displays the current question and its answer options.
        """
        if not self.current_questions or self.current_question_index >= len(self.current_questions):
            self.reset_quiz_state()
            QMessageBox.information(self, "Quiz Finished", "You have completed all questions!")
            return

        question_data = self.current_questions[self.current_question_index]

        self.current_category_label.setText(question_data.get('category', 'N/A'))
        self.current_difficulty_label.setText(question_data.get('difficulty', 'N/A').capitalize())
        self.question_text_label.setText(question_data.get('question', ''))  # Display simplified text
        self.question_counter_label.setText(f"{self.current_question_index + 1}/{len(self.current_questions)}")

        # Prepare answers (correct + incorrect) and shuffle them
        all_answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        random.shuffle(all_answers)

        # Clear previous selections and update radio buttons
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for i, radio_button in enumerate(self.radio_buttons):
            if i < len(all_answers):
                radio_button.setText(all_answers[i])
                radio_button.setChecked(False)
                radio_button.show()
            else:
                radio_button.hide()  # Hide unused radio buttons
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.check_button.setEnabled(False)
        self.try_again_button.setEnabled(False)
        self.next_button.setEnabled(False)  # Only enable after checking or if quiz finishes

        # Enable radio buttons for interaction
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Reset styling

    def on_answer_selected(self, radio_button):
        """
        Handles selection of an answer by a radio button.
        """
        # The `radio_button` argument is automatically passed by QButtonGroup's buttonClicked signal
        self.selected_answer = radio_button.text()
        self.check_button.setEnabled(True)
        print(f"Selected answer: {self.selected_answer}")  # For debugging

    def check_answer(self):
        """
        Checks if the selected answer is correct and provides feedback.
        """
        if self.selected_answer is None:
            QMessageBox.warning(self, "No Answer Selected", "Please select an answer before checking.")
            return

        current_question = self.current_questions[self.current_question_index]
        correct_answer = current_question['correct_answer']

        # Disable radio buttons after checking
        for radio_button in self.radio_buttons:
            radio_button.setEnabled(False)
            if radio_button.text() == correct_answer:
                radio_button.setStyleSheet("QRadioButton { color: green; font-weight: bold; }")
            elif radio_button.text() == self.selected_answer:
                radio_button.setStyleSheet("QRadioButton { color: red; font-weight: bold; }")

        if self.selected_answer == correct_answer:
            QMessageBox.information(self, "Correct!", "Your answer is correct!")
            self.next_button.setEnabled(True)
            self.try_again_button.setEnabled(False)
        else:
            QMessageBox.warning(self, "Incorrect",
                                f"Your answer is incorrect. The correct answer was: {correct_answer}")
            self.try_again_button.setEnabled(True)
            self.next_button.setEnabled(True)  # Allow moving to next question even if incorrect

        self.check_button.setEnabled(False)  # Disable check button after checking
        print("Answer checked.")  # For debugging

    def try_again(self):
        """
        Resets the current question for another attempt.
        """
        self.answer_button_group.setExclusive(False)  # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.setChecked(False)
            radio_button.setEnabled(True)
            radio_button.setStyleSheet("")  # Clear styling
        self.answer_button_group.setExclusive(True)  # Restore exclusive selection

        self.selected_answer = None
        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(True)
        self.next_button.setEnabled(False)  # Disable next until checked again
        print("Try Again clicked.")  # For debugging

    def next_question(self):
        """
        Moves to the next question in the list.
        """
        self.current_question_index += (1)
        self.display_question()
        print(f"Moved to question {self.current_question_index + 1}.")  # For debugging

    def reset_quiz_state(self):
        """
        Resets the UI and internal state when the quiz ends or fails to load.
        """
        self.current_questions = []
        self.current_question_index = -1
        self.selected_answer = None
        self.question_text_label.setText("Click 'Get New Question' to start the quiz!")
        self.current_category_label.setText("N/A")
        self.current_difficulty_label.setText("N/A")
        self.question_counter_label.setText("0/0")

        self.answer_button_group.setExclusive(False) # Temporarily allow no selection to clear
        for radio_button in self.radio_buttons:
            radio_button.hide()
            radio_button.setChecked(False)
            radio_button.setStyleSheet("")
        self.answer_button_group.setExclusive(True) # Restore exclusive selection

        self.try_again_button.setEnabled(False)
        self.check_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.get_question_button.setText("Get New Question")
        print("Quiz state reset.") # For debugging


def main():
    """
    The main function to create and run the PyQt5 application.
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
