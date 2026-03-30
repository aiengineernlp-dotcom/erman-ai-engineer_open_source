"""
Basic ML metrics calculator avec pure python
CAs usage : Coomprendre c'est quoi l'accuracy/error moyenne avant sklearn
"""


def calculate_matrics(y_true: list[int], y_pred: list[int]) -> dict[str, float]:
    assert len(y_true) == len(
        y_pred), "Lists doivent avoir la meme taille"  # mesure de securite. si elle n'est pas remplie le programme stop
    n = len(y_true)

    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    true_pos = sum(1 for t, p, in zip(y_true, y_pred) if t == 1 and p == 1)
    false_pos = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    false_neg = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)

    precision = true_pos / (true_pos + false_pos) if true_pos + false_pos > 0 else 0.0
    recall = true_pos / (true_pos + false_neg) if true_pos + false_neg > 0 else 0.0

    return {

    }