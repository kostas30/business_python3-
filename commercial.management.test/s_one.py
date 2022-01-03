import os
import sys

date_lis = []  # ημερομηνια  εισαγωγης
stock_lis = []  # ποσοτητα  εισαγωγης
valus_lis = []  # αξια   εισαγωγης
def stock_add():
        date_in = input('εισαγετε την ημερομηνια :')
        
        stock_in = int(input('Εισαγετε  την ποσοτητα  που εχετε αγοραση :'))
        valus_in = float(input('Ποια  ειναι η τιμη εισαγωγη την αποθηκη :'))
        date_lis.append(date_in)
        stock_lis.append(stock_in)
        valus_lis.append(valus_in)
        print('Η  εισαγωγες  την αποθηκη εγιναν; {} και ηποστητα: {} και η τιμη :{}   '.format(date_lis, stock_lis,
                                                                                           valus_lis))
        return date_lis, stock_lis, valus_lis
stock_add()
