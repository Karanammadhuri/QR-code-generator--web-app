from django.shortcuts import render, redirect
from .forms import QRCodeDataForm
import qrcode

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img_path = f'static/qr_codes/{data}.png'
            img.save(img_path)
            return render(request, 'qr_code_generator/generate.html', {'qr_code_path': img_path})
    else:
        form = QRCodeDataForm()
    return render(request, 'qr_code_generator/index.html', {'form': form})
