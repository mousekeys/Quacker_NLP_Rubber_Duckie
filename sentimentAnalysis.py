from mediapipe.tasks import python
from mediapipe.tasks.python import text

model_path='bert_classifier.tflite'

iptext='The world is cruel'

base_options = python.BaseOptions(model_asset_path=model_path)
options = text.TextClassifierOptions(base_options=base_options)

with python.text.TextClassifier.create_from_options(options) as classifier:
  classification_result = classifier.classify(iptext)

top_category = classification_result.classifications[0].categories[0]
print(f'{top_category.category_name} ({top_category.score:.2f})')