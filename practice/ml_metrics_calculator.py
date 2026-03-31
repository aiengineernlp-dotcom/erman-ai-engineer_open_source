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

        "total_samples":n,
        "correct":correct,
        "accuracy":correct/n,
        "error_rate":1-(correct/n),
        "true_positive":true_pos,
        "false_positive":false_pos,
        "false_negative":false_neg,
        "precision":precision,
        "recall":recall
    }

def display_metrics(metrics: dict[str, float])-> None:
    """Display in a professional format"""
    print("\n" + "=" * 140)
    print(f"{'ML MODEL EVALUATION REPORT':^55}")
    print("=" * 140)
    print(f"  Samples:{metrics['total_samples']}  ")
    print(f"  Correct:{metrics['correct']}")
    print(f"  Accuracy:{metrics['accuracy']:.2%}")
    print(f"  Error Rate:{metrics['error_rate']:.2%}")
    print("=" * 140)
    print(f"  True Positive:{metrics['true_positive']}")
    print(f"  False Positive:{metrics['false_positive']}")
    print(f"  False Negative:{metrics['false_negative']}")
    print("=" * 140)
    print(f"  Precision:{metrics['precision']:.4f}")
    print(f"  Recall:{metrics['recall']:.4f}")
    print("=" * 140)




y_true = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]  # réalité
y_pred = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0]  # prédictions modèle
metrics = calculate_matrics(y_true, y_pred)
display_metrics(metrics)