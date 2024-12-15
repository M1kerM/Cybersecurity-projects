import re

# Liste noire des mots de passe courants
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "letmein", "monkey", "football", "iloveyou", "admin"
]

def check_password_strength(password):
    issues = []

    # Vérification de la longueur
    if len(password) < 8:
        issues.append("Le mot de passe doit contenir au moins 8 caractères.")

    # Vérification des caractères
    if not re.search(r'[A-Z]', password):
        issues.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    if not re.search(r'[a-z]', password):
        issues.append("Le mot de passe doit contenir au moins une lettre minuscule.")
    if not re.search(r'\d', password):
        issues.append("Le mot de passe doit contenir au moins un chiffre.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        issues.append("Le mot de passe doit contenir au moins un caractère spécial (!@#$%^&*(), etc.).")

    # Vérification de la liste noire
    if password.lower() in COMMON_PASSWORDS:
        issues.append("Le mot de passe est trop courant.")

    # Vérification des variations simples
    simple_variations = [password.lower(), password.upper(), password.capitalize()]
    if any(variant in COMMON_PASSWORDS for variant in simple_variations):
        issues.append("Le mot de passe est une variante trop simple d'un mot de passe commun.")

    return issues if issues else ["Le mot de passe est fort."]

# Exemple d'utilisation
password = input("Entrez un mot de passe à tester : ")
result = check_password_strength(password)

print("\n".join(result))

