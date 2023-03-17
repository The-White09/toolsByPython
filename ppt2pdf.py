import subprocess
import os


# Function to convert PPT to PDF
def ppt_to_pdf(input_ppt, output_pdf):
    # Call unoconv to convert the PPT to PDF
    subprocess.run(["unoconv", "-f", "pdf", "-o", output_pdf, input_ppt])


# Find all files ending with pptx
pptx_files = [f for f in os.listdir() if f.endswith('.pptx')]

# Loop through all pptx files and convert them to PDF
for input_ppt in pptx_files:
    # Set the output PDF file name
    output_pdf = input_ppt.replace('.pptx', '.pdf')

    # Call the function to convert PPT to PDF
    ppt_to_pdf(input_ppt, output_pdf)
