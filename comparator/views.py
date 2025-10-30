from django.shortcuts import render, redirect
from .forms import PDFComparisionForm
from .utils import are_pdfs_equal

def upload_pdf(request):
    result = None
    if request.method == 'POST':
        form = PDFComparisionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # Get file paths from the just-saved instance
            file1_path = instance.pdf_file_1.path
            file2_path = instance.pdf_file_2.path
            # Perform the comparison
            result = are_pdfs_equal(file1_path, file2_path)
            # Pass result to the success template
            return render(request, 'upload_success.html', {'result': result})
    else:
        form = PDFComparisionForm()
    return render(request, 'upload_pdf.html', {'form': form})
