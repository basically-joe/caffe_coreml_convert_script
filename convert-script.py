import coremltools

caffe_model = ("CAFFEMODELNAME.caffemodel", "deploy.prototxt")

labels = "LABELSFILENAME.txt"

coreml_model = coremltools.converters.caffe.convert(
    caffe_model,
    class_labels=labels,
    image_input_names="data"
)

coreml_model.save("NAMEOFCOREMLMODEL.mlmodel")