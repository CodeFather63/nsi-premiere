from nsi_ui import *



monnaie1 = "EUR"
monnaie2 = "USD"
taux = 1.20


def convert():
    """ Convertit le montant saisi dans les deux monnaies """
    m = get_float(montant)

    r1 = m * taux
    r2 = m / taux
    set_text(conv1, str(m) + str(monnaie1) + " = " + str(r1) + str(monnaie2))
    set_text(conv2, str(m) + str(monnaie2) + " = " + str(r2) + str(monnaie1))

# Construire l'interface
montant = entry("Montant")
button("Convertir",convert)
begin_vertical()
conv1 = label('conversion')
conv2 = label('conversion')
end_vertical()
main_loop()



