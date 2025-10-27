from django.shortcuts import render, redirect
from .forms import PDFComparisionForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFComparisionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = PDFComparisionForm()
    return render(request, 'upload_pdf.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
