import os
from dotenv import load_dotenv
from lowatt_grdf.api import API
from lowatt_grdf.models import DeclareAccess

load_dotenv()

def main():
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    pce = os.environ.get("PCE")

    print("CLIENT_ID :",client_id)
    print("CLIENT_SECRET :",client_secret)
    print("PCE :",pce)

    api = API(client_id, client_secret)

    try:
        # Authenticate and get the access token
        print("# ---------------------------------------------------------------------------- #\n#                                AUTHENTICATION                                #\n# ---------------------------------------------------------------------------- #\n")
        access_token = api.access_token
        print("TOKEN :",access_token)

        # Check if we have access to the API
        print("\n# ---------------------------------------------------------------------------- #\n#                              CHECK API ACCESS                                #\n# ---------------------------------------------------------------------------- #\n")
        api.check_consent_validation()

        # Declare access to a PCE
        print("\n# ---------------------------------------------------------------------------- #\n#                              DECLARE ACCESS                                  #\n# ---------------------------------------------------------------------------- #\n")
        access = DeclareAccess(
            pce=pce,
            raison_sociale="NOBATEK/INEF4",
            code_postal="64100",
            courriel_titulaire="",
            date_consentement_declaree="2023-11-20",
            date_debut_droit_acces="2023-01-01",
            date_fin_droit_acces="2024-02-20",
            perim_donnees_conso_debut="2023-01-01",
            perim_donnees_conso_fin="2024-02-20",
        )
        api.declare_acces(access)

        # Access right without PCE
        print("\n# ---------------------------------------------------------------------------- #\n#                              ACCESS RIGHT WITHOUT PCE                        #\n# ---------------------------------------------------------------------------- #\n")
        droits = api.droits_acces()
        for droit in droits:
            print(droit)

        # Access right with PCE
        print("\n# ---------------------------------------------------------------------------- #\n#                              ACCESS RIGHT WITH PCE                           #\n# ---------------------------------------------------------------------------- #\n")
        droits = api.droits_acces(pce)
        for droit in droits:
            print(droit)

        # Specific access right
        print("\n# ---------------------------------------------------------------------------- #\n#                              SPECIFIC ACCESS RIGHT                           #\n# ---------------------------------------------------------------------------- #\n")
        # To implement

        # Get published consumption data
        print("\n# ---------------------------------------------------------------------------- #\n#                              PUBLISHED CONSUMPION DATA                       #\n# ---------------------------------------------------------------------------- #\n")
        for releve in api.donnees_consos_publiees(pce, from_date="2023-01-01", to_date="2023-12-01"):
            conso = releve["consommation"]
            print(conso["date_debut_consommation"], conso["date_fin_consommation"], conso["energie"])

        # Get informative consumption data
        print("\n# ---------------------------------------------------------------------------- #\n#                              INFORMATIVE CONSUMPION DATA                    #\n# ---------------------------------------------------------------------------- #\n")
        for releve in api.donnees_consos_informatives(pce, from_date="2023-01-01", to_date="2023-12-01"):
            conso = releve["consommation"]
            print(conso["date_debut_consommation"], conso["date_fin_consommation"], conso["energie"])

        # Get contract data
        print("\n# ---------------------------------------------------------------------------- #\n#                              CONTRACT DATA                                  #\n# ---------------------------------------------------------------------------- #\n")
        contract = api.donnees_contractuelles(pce)
        print(contract)

        # Get technical data
        print("\n# ---------------------------------------------------------------------------- #\n#                              TECHNICAL DATA                                 #\n# ---------------------------------------------------------------------------- #\n")
        technical = api.donnees_techniques(pce)
        print(technical)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
