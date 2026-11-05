import collections 

noms = ["Jannot", "Emery", 'Isaac', "Seth", 'Héritier', 'Jolie', "Gerlas", "Merveille", 'Jules', 'Louise', 'Héritier', 'Clément', "Joël", 'Neema', "Héritier", "Jolie"]




compteur = collections.Counter(noms)

print(compteur)
frequent = compteur.most_common(1)

print(f"Le nom le plus fréquent est «{frequent[0][0]}», car il a apparu {frequent[0][1]} fois")

