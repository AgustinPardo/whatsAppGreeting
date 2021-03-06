def main():

    app = QApplication([])
    window = QWidget()
    window.setMinimumSize(QSize(500, 250))#500 150
    window.setWindowTitle("WhastApp greet!")
    layout = QGridLayout()

    layout.addWidget(QLabel('Response greet:'), 0, 0)
    response_msg=QLineEdit('')
    layout.addWidget(response_msg, 0, 1)

    layout.addWidget(QLabel('Words to capture:'), 1, 0)
    word_capture=QTextEdit('')
    layout.addWidget(word_capture, 1, 1)

    def btnAction():

        # Remove the prior layout
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)

        # parse the input text
        response_msg_texy=response_msg.text()
        word_capture_list=word_capture.toPlainText().split("\n")
        word_capture_list=[i for i in word_capture_list if i  != '']

        # Run the app

        try:
            driver = appCore.Driver()
            panel = appCore.Panel(driver.driver, driver.getUser(), word_capture_list, response_msg_texy)
            panel.greetChats()
            driver.disconnect()

        except TimeoutException as exception:
            # Add text to the layout
            layout.addWidget(QLabel('Log-in to WhatsApp web please and restart the app!'), 1, 0, 1, 3)

        except InvalidArgumentException as exception:
            # Add text to the layout
            layout.addWidget(QLabel('Close all the Browser windows cotrolled by Selenium and re-start the execution!'), 1, 0, 1, 3)

        return 0

    btn = QPushButton('Send Greets!')
    word_capture_list= btn.clicked.connect(btnAction)
    layout.addWidget(btn, 2, 1)

    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()