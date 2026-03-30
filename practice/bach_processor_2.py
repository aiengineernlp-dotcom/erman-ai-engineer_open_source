# # batch_processor_ml_version_2
#
# import  random
# random.seed(42)
#
# def create_dataset(n_sample:int)->list[dict]:
#     return [
#         {
#             "id": id,
#             "feature" :[
#                 round(random.gauss(0,1),4) for _ in range(5)
#             ]
#             ,
#             "label": random.choice([0,1])
#
#         } for i in range(n_sample)
#
#     ]
#
# def create_shuffled_dataset(dataset:list)->list:
#     # copie de mon dataset pour la comparaison
#     shuffled_dataset = dataset[:]
#     random.shuffle(shuffled_dataset)
#     return shuffled_dataset
#
# def create_batches(dataset:list, batch_size:int)->list:
#     return [
#         dataset[i:i+ batch_size] for i in range(0,len(dataset), batch_size)
#     ]
#
#
# def simulate_forward_pass(batch:list)->float:
#     # parcourrir les batches et retirer les labels like sample
#     labels = [sample ["label"] for sample in batch ]
#     loss = sum(labels) / len(labels)
#     return round(loss+ random.uniform(-0.1,0.1),4)
#
#
# def train_epoch(dataset:list, batch_size:int,epochs:int)->dict:
#
#     shuffled = create_shuffled_dataset(dataset)
#     batches = create_batches(dataset,batch_size)
#     loss = []
#
#     print(f"\n EPOCHS: {epochs}")
#     print(f"\n    {'Batch':>6} | {'Size':>8} | {'Loss':>8} | Progress")
#     print("=" * 140)
#     pass
#
#
#
#
#


