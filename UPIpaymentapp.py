#Install library named qr code and pillow

import qrcode

upi_id=input("Enter your UPI ID= ")
#payment url as 
#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#create qr code for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save the qr code to image file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#display the qr code and for this we have to install image viewer library i.e. PIL/pillow

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()