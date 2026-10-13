import random
import string


def generer_mot_de_passe(longueur: int = 12, avec_chiffres: bool = True, avec_symboles: bool = True) -> str:
    alphabet = string.ascii_letters
    if avec_chiffres:
        alphabet += string.digits
    if avec_symboles:
        alphabet += string.punctuation
    return "".join(random.choice(alphabet) for _ in range(longueur))
