from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse et calcule l'expression mathématique fournie.

    Args:
        expr (str): L'expression sous forme de chaîne (ex: "10 + 5").

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'expression est invalide, vide ou contient plusieurs opérateurs.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")  # Suppression des espaces pour faciliter le traitement

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur unique dans l'expression
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Rejet si plusieurs opérateurs sont trouvés
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # L'opérateur ne peut pas être au début ou à la fin (expression mal formée)
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        # Conversion des opérandes en nombres flottants
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère l'affichage et le traitement du formulaire de calcul.
    
    Traite les requêtes GET pour afficher la page et POST pour effectuer le calcul.

    Returns:
        str: Le rendu HTML de la page avec le résultat éventuel.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)