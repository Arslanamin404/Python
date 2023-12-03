# visit pypdf module docs
#! Link: https://pypdf2.readthedocs.io/en/3.0.0/user/merging-pdfs.html


from pypdf import PdfMerger

# Create an instance of PdfMerger
merger = PdfMerger()

# List of PDF file paths to be merged
pdf_to_merge = [
    "PDF's\\test-01.pdf",
    "PDF's\\test-02.pdf",
    "PDF's\\test-03.pdf"
]

# Iterate through the list of PDFs and append them to the merger
for pdf in pdf_to_merge:
    merger.append(pdf)

# Write the merged PDF to a new file
merger.write("PDF's\Merged-PDF.pdf")

# Close the merger instance
merger.close()
