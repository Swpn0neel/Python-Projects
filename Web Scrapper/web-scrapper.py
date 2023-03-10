import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QFileDialog

class WebScraper(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and dimensions
        self.setWindowTitle('Web Scraper- by Swapnoneel')
        self.setGeometry(100, 100, 600, 400)

        # Create the web address input field and label
        self.url_label = QLabel('Enter Web Address:', self)
        self.url_label.move(50, 50)
        self.url_field = QLineEdit(self)
        self.url_field.move(200, 50)
        self.url_field.resize(300, 30)

        # Create the scrape button
        self.scrape_button = QPushButton('Scrape', self)
        self.scrape_button.move(250, 100)
        self.scrape_button.clicked.connect(self.scrape_data)

        # Create the output text field and label
        self.output_label = QLabel('Output:', self)
        self.output_label.move(50, 150)
        self.output_field = QTextEdit(self)
        self.output_field.move(50, 180)
        self.output_field.resize(500, 150)

        # Create the save button
        self.save_button = QPushButton('Save', self)
        self.save_button.move(250, 350)
        self.save_button.clicked.connect(self.save_output)

    def scrape_data(self):
        # Get the URL entered by the user
        url = self.url_field.text()

        # Send a GET request to the URL and store the response
        response = requests.get(url)

        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the links on the page and add them to the output field
        output_text = ''
        for link in soup.find_all('a'):
            output_text += link.text.strip() + ' ' + link.get('href') + '\n'
        self.output_field.setText(output_text)

    def save_output(self):
        # Open a file dialog and get the file name and path to save the output to
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')

        # If a file was selected, write the output to the file
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.output_field.toPlainText())
            QMessageBox.information(self, 'File Saved', 'Output saved successfully!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebScraper()
    window.show()
    sys.exit(app.exec_())
