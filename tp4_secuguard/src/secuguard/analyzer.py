import string

from colorama import Fore, Style, init

init(autoreset=True)


def analyser_mot_de_passe(mot_de_passe: str) -> str:
    a_lettres = any(c in string.ascii_letters for c in mot_de_passe)
    a_chiffres = any(c in string.digits for c in mot_de_passe)
    a_symboles = any(c in string.punctuation for c in mot_de_passe)
    nb_types = a_lettres + a_chiffres + a_symboles

    if len(mot_de_passe) >= 12 and a_lettres and a_chiffres and a_symboles:
        return Fore.GREEN + "[FORT] Mot de passe tres solide." + Style.RESET_ALL
    if len(mot_de_passe) >= 8 and nb_types >= 2:
        return Fore.YELLOW + "[MOYEN] Mot de passe correct mais ameliorable." + Style.RESET_ALL
    return Fore.RED + "[FAIBLE] Mot de passe trop court et prévisible." + Style.RESET_ALL
