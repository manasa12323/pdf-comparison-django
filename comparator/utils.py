from PyPDF2 import PdfReader

def are_pdfs_equal(file1_path, file2_path):
    # Byte comparison - will work for absolute duplicates only
    with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
        return f1.read() == f2.read()
