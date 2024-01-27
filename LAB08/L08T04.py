
autot = {
    "pkb-345": "Tesla",
    "eps-843": "BMW",
    "oja-197": "Mercedes-benz",
    "paf-744": "Honda",
    "wga-762": "Ferrari",
    "oww-793": "Porsche",
    "psf-894": "Bugatti",
    "joe-795": "Audi",
    "hes-795": "Volkswagen",
    "paw-258": "Lotus",
}

key = list(autot.keys())    
key.sort()
lajiteltu = {i:autot[i] for i in key}
for x,y in lajiteltu.items():
    print(x,y)

