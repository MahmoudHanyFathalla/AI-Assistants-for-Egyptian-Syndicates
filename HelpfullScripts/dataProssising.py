import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_files(input_directory, output_csv_directory, output_json_directory, output_pdf_directory):
    # Create output directories if they do not exist
    os.makedirs(output_csv_directory, exist_ok=True)
    os.makedirs(output_json_directory, exist_ok=True)
    os.makedirs(output_pdf_directory, exist_ok=True)

    # Iterate over all files in the input directory
    for root, directories, files in os.walk(input_directory):
        for filename in files:
            if filename.lower().endswith('.xlsx'):
                # Construct the full file path
                filepath = os.path.join(root, filename)
                # Read the Excel file using openpyxl engine
                excel_data = pd.read_excel(filepath, engine='openpyxl')
                
                # Save as CSV
                csv_filename = filename.replace('.xlsx', '.csv')
                csv_filepath = os.path.join(output_csv_directory, csv_filename)
                excel_data.to_csv(csv_filepath, index=False)

                # Save as JSON
                json_filename = filename.replace('.xlsx', '.json')
                json_filepath = os.path.join(output_json_directory, json_filename)
                excel_data.to_json(json_filepath, orient='records', lines=True)

                # Save as PDF
                pdf_filename = filename.replace('.xlsx', '.pdf')
                pdf_filepath = os.path.join(output_pdf_directory, pdf_filename)
                save_dataframe_to_pdf(excel_data, pdf_filepath)

                print(f"Converted {filename} to CSV, JSON, and PDF formats.")

def save_dataframe_to_pdf(df, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    c.drawString(30, height - 40, "Data from Excel Sheet")
    
    x_offset = 30
    y_offset = height - 60
    padding = 15

    for column in df.columns:
        c.drawString(x_offset, y_offset, column)
        x_offset += 100
    
    x_offset = 30
    y_offset -= padding

    for index, row in df.iterrows():
        x_offset = 30
        for item in row:
            c.drawString(x_offset, y_offset, str(item))
            x_offset += 100
        y_offset -= padding
        if y_offset < 40:  # Add new page if content exceeds one page
            c.showPage()
            y_offset = height - 40

    c.save()

# Example usage
input_directory = "C:\\Users\\hp\\Downloads\\All"
output_csv_directory = "C:\\Users\\hp\\Downloads\\All_CSV"
output_json_directory = "C:\\Users\\hp\\Downloads\\All_JSON"
output_pdf_directory = "C:\\Users\\hp\\Downloads\\All_PDF"

convert_files(input_directory, output_csv_directory, output_json_directory, output_pdf_directory)
