# OCR PDF Reader with Pytesseract

## Introduction

Welcome to the OCR PDF Reader with Pytesseract project! This tool empowers you to extract text from PDF documents, even in cases where the text is challenging to read. Leveraging the Pytesseract library, this tool allows you to specify locations within a PDF where text should be extracted and then saves the extracted text to an Excel file.

## Prerequisites

Before getting started with this project, ensure you have the following prerequisites installed on your system:

- Python
- [Pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (You can download it manually from the provided link)

You can install the required Python libraries using pip:

```bash
pip install pytesseract
pip install Pillow
```

Additionally, you'll need to specify the location of the Tesseract OCR executable by setting the `tesseract_cmd` variable in the code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

1. Clone this repository or download the code to your local machine.

2. Specify the path to the PDF file you want to process:

```python
pdf_file = r''  # Replace with the path to your PDF file
```

3. Set the temporary folder where screenshots will be stored:

```python
temp_dir = r''  # Set your temporary folder for screenshots
```

4. Define the locations from which you want to extract text in the PDF. Each location should be specified as a tuple of (left, top, width, height). You can add multiple locations as needed:

```python
screenshot = [
    (100, 100, 100, 100),  # Location 0
    (200, 200, 200, 100),  # Location 1
    # Add more locations as needed
]
```

5. Specify the path for the output Excel file:

```python
output_excel = r''  # Set the path for the output .xlsx file
```

6. If necessary, adjust the prescale factor:

```python
matrix = fitz.Matrix(1, 1).prescale(3, 3)  # Adjust the prescale if needed
```

7. Run the script, which will capture screenshots from the specified locations, extract text using Pytesseract, and save the results to an Excel file:

```bash
python your_script.py
```

## Output

The extracted text will be saved in an Excel file. The Excel sheet will include the file name and extracted text from each specified screenshot location.

## License

This project is open-source and available under the [MIT License](LICENSE).
```

You can copy and paste this Markdown content into your GitHub repository's README.md file. Make sure to replace the placeholder paths and details with your specific information.
