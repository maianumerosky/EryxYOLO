def assert_labels_size(dataset):

    first_dataset_element_labels = dataset[0][1]
    labels_size = list(first_dataset_element_labels.size())
    AMOUNT_OF_GRIDCELLS = 7  # S
    CLASSES_PLUS_BOUNDING_BOXES = 81  # 5*B + Number of classes
    expected_labels_size = [AMOUNT_OF_GRIDCELLS, AMOUNT_OF_GRIDCELLS, CLASSES_PLUS_BOUNDING_BOXES]
    if labels_size == expected_labels_size:
        print(" Correct label size ", labels_size)
    else:
        print("Error in labels size")