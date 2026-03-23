bruto = float(input())


if 0 > bruto <= 1000:
    impuesto = bruto * 0
    print("Impuesto: {:.1f}".format(impuesto))
elif 1001 >= bruto <= 5000:
    apagar =(bruto - 1000)*0.1
    print("Impuesto: {:.1f}".format(apagar))
else:
    apagar = (bruto-5000)*0.2 + (4000 * 0.1)
    print("Impuesto: {:.1f}".format(apagar))