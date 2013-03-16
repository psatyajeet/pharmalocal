PharmaSave

Fields:
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    order_date = models.CharField(max_length=200)
    birth_date = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    medication = models.CharField(max_length=200)
    prescriber_name= models.CharField(max_length=200)
    prescriber_phone_number= models.CharField(max_length=12)
    paper=models.BooleanField('Paper prescription')
    zipcode=models.CharField(max_length=200)