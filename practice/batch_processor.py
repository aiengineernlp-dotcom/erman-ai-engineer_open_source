# batch_processor.py

"""
ML Mini Batch processor.
Use case: Simulate the corps training loop batch logic used in Pytorch Dataloader, before using the framework

#=========
Petit Batch processor.
Cas usage: Ici on veut simmuler le dataloader de Pytorch. cella permet ce comprendre comment les donnees
sont DECOUPEES et MELANGEES avant d'entrer dans le modele. L'idee est de transformmer un dataset complet
en petit morceau (mini batches) pour obtimiser la memoire et l'apprentissage [2,3]


"""

import random

random.seed(42)


def create_dataset(n_samples: int) -> list[
    dict]:
    '''Generate a synthetic classification dataset'''
    return [
        {
            "id": i,
            "features": [round(random.gauss(0, 1), 4) for _ in range(5)],  #
            "label": random.choice([0, 1])
        }
        for i in range(n_samples)
    ]


def shuffle_dataset(dataset: list) -> list:  # cette fonction melange les donnnes crees
    '''Shuffle dataset - standart before each epoch '''
    shuffled = dataset[:]  # copie independante
    random.shluffle(shuffled)
    return shuffled


def create_batches(dataset: list, batch_size: int) -> list[list]:
    '''
    split dataset into mini batches:

    Args:
        datasets : Full dataset as a list
        batch_size: Size of each batch
    Returns:
        List of Batches (each batch is a list of samples)
    '''

    return [
        dataset[i:i + batch_size]
        for i in range(0, len(dataset), batch_size)
    ]


def simulate_forward_pass(batch: list) -> float:
    """Simulate a forward pass  -  returns mock loss."""
    labels = [sample['label'] for sample in batch] # label c'est la cible de notre dictionnaire

    # mock loss : proportion de 1s dans le batch (simulation)
    loss = sum(labels) / len(labels)

    return round(loss + random.uniform(-0.1, 0.1), 4)


def train_epoch(dataset: list, batch_size: int, epoch: int) -> dict:
    """
    Run one full training epoch.

    Args:
        dataset : Full training dataset
        batch_size: Mini-batch size
        epoch : Current epoch number

    Returns:
        Epoch statistics dict
    """
    shuffled = shuffle_dataset(dataset)
    batches = create_batches(shuffled, batch_size)
    losses = []

    print(f"\n  EPOCHS {epoch}")
    print(f"  {'Batch':>6} | {'Size':>5} | {'Loss':>8} | {'Progress'}")
    print(f"  {'-' * 45}")

    for idx, batch in enumerate(batches, 1):
        loss = simulate_forward_pass(batch)
        losses.append(loss)

        progress = idx / len(batches)
        bar_len = 20
        filled = int(bar_len * progress)
        bar = "█" * filled + "░" * (bar_len - filled)

        print(f"   {idx:>6} | {len(batches):>5} | {loss:>8.4f} | [{bar}] {progress:.0%}")

    mean_loss = sum(losses) / len(losses)

    return {
        "epoch": epoch,
        "n_batches": len(batches),
        "mean_loss": round(mean_loss, 4),
        "min_loss": min(losses),
        "max_loss": max(losses)
    }

    # SIMULATION COMPLETE


DATASET_SIZE = 150  # Ttous mon dataset
BATCH_SIZE = 32  # la taille du lot
N_EPOCHS = 3  # le nombre de fois que l'IA va voir mon DATASET_SIZE

print("=" * 55)
print(f"{'MINI BATCH TRAINING SIMULATION':^55}")
print(f"    Dataset : {DATASET_SIZE} samples | Batche: {BATCH_SIZE} | Epochs: {N_EPOCHS}")
print("=" * 55)

dataset = create_dataset(DATASET_SIZE)
epoch_stats = []

for epoch in range(1, N_EPOCHS + 1):
    stats = train_epoch(dataset, BATCH_SIZE, epoch)
    epoch_stats.append(stats)

print(f"\n {'=' * 55}")
print(f"{'TRAINING SUMMARY':^55}")
print(f"{'=' * 55}")
print(f"{'Epoch':>5} | {'Batches':>8} | {'Mean Loss':>10} | {'Min':>7} | {'Max':>7}")
print(f"{'-' * 50}")

for s in epoch_stats:
    print(f" {s['epoch']:>6} | {s['n_batches']:>8} | ",
          f"{s['mean_loss']:>10.4f} | {s['min_loss']:>7.4f} | {s['max_loss']:>7.4f}")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
# "Voici un code [nom du langage, ex: Python]. Je veux le masteriser caractère par caractère. Ne te contente pas d'un résumé :
# Analyse ligne par ligne chaque fonction en expliquant la syntaxe technique (le 'comment').
# Explique l'intention d'ingénierie derrière chaque bloc (le 'pourquoi' on fait ça ainsi).
# Identifie les pièges invisibles (mémoire, performance, erreurs courantes).
# Propose un défi ou une question de logique après chaque section pour valider ma compréhension.
# Voici le code : [COLLE TON CODE ICI]"