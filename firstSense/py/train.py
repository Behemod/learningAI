from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="firstSense/res/hololens-yolo")
trainer.setTrainConfig(object_names_array=["hololens"], batch_size=32, num_experiments=200, train_from_pretrained_model="")
# In the above,when training for detecting multiple objects,
#set object_names_array=["object1", "object2", "object3",..."objectz"]
# Also batch_size=16 if 32 does not work
# First try yolov3_hololens-yolo_mAP-0.57985_epoch-66.pt
# Was using pretrained model yolov3.pt
trainer.trainModel()