from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="ImageAI/data-images/mytest/hololens-yolo")
trainer.setTrainConfig(object_names_array=["hololens"], batch_size=32, num_experiments=100, train_from_pretrained_model="yolov3.pt")
# In the above,when training for detecting multiple objects,
#set object_names_array=["object1", "object2", "object3",..."objectz"]
# Also batch_size=16 if 32 does not work
trainer.trainModel()