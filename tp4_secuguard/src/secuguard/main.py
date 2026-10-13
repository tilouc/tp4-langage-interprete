import argparse

from secuguard.analyzer import analyser_mot_de_passe
from secuguard.generator import generer_mot_de_passe


def main():
    parser = argparse.ArgumentParser(description="secuguard : generer ou analyser un mot de passe")
    parser.add_argument("-c", "--check", type=str, help="mot de passe a analyser")
    parser.add_argument("-l", "--length", type=int, default=12, help="longueur du mot de passe (defaut : 12)")
    parser.add_argument("--no-digits", action="store_false", dest="avec_chiffres", help="sans chiffres")
    parser.add_argument("--no-symbols", action="store_false", dest="avec_symboles", help="sans symboles")
    args = parser.parse_args()

    if args.check is not None:
        print(analyser_mot_de_passe(args.check))
    else:
        print("Mot de passe genere :", generer_mot_de_passe(args.length, args.avec_chiffres, args.avec_symboles))


if __name__ == "__main__":
    main()
