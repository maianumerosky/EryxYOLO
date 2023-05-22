import torchvision
import matplotlib.pyplot as plt
import torch

img_size = 448

class_dict ={0:"fondo",
1:"metal_1",
2:"metal_2",
3:"metal_alargado",
4:"plastico_der",
5:"plastico_izq",
6:"sonrisa_chica",
7:"sonrisa_grande",
8:"sticker"}

def get_object_class(class_tensor):
    """
    Given a tensor with the class probabilities, returns a string with the name of the most likely class
    """
    index = torch.argmax(class_tensor).item()
    return class_dict[index]


def torch_to_pil(img):
  return torchvision.transforms.ToPILImage()(img).convert('RGB')

def draw_img_and_bbox_from_true_labels(img, labels):
    """
    Takes img and labels from the dataset class and draws a PIL image with the bounding boxes for the labeled data.
    """
    fig, ax = plt.subplots()

    ax.imshow(torch_to_pil(img))
    ax.axis("off")

    #ahora las bounding box
    img_size = 448
    grid_labels = labels[3,3,:]

    for i in range(7):
        for j in range(7):
            grid_labels = labels[i,j,:]
            draw_grid_bbox(grid_labels, ax)
            
            
def draw_grid_bbox(grid_labels, ax):
    """
    Draws the true bounding box for a single grid cell. Takes the grid labels in the format 2B + C and an axes object. Draws the box and writes the class and confidence.
    """
    x = grid_labels[0] * img_size
    y = grid_labels[1] * img_size
    w = grid_labels[2] * img_size
    h = grid_labels[3] * img_size

    confidence = grid_labels[4]
    object_class = grid_labels[10:]
    x0 = x - w/2
    x1 = x + w/2
    y0 = y - h/2
    y1 = y + h/2

    object_class_name = get_object_class(object_class)
    if confidence > 0.5:
        ax.plot([x0,x0], [y0, y1], c = "y")
        ax.plot([x1,x1], [y0, y1], c = "y")
        ax.plot([x0,x1], [y0, y0], c = "y")
        ax.plot([x0,x1], [y1, y1], c = "y")
        ax.text(x0,y1+ 20, f"{object_class_name} {confidence.item()}")


def draw_prediction_grid_bbox(grid_labels, ax, threshold = 0.5):
    """
    Draws the bounding box for a single grid cell of a prediction. Takes the grid labels in the format 2B + C and an axes object. Checks which box to draw. Draws the box and writes the class and confidence.
    """
    bbox_index = 0
    if grid_labels[4] <= grid_labels[9]:
        bbox_index = 5 
    x = grid_labels[bbox_index] * 448
    y = grid_labels[bbox_index+1] * 448
    w = grid_labels[bbox_index+2] * 448
    h = grid_labels[bbox_index+3] * 448

    confidence = grid_labels[bbox_index+4]
    object_class = grid_labels[10:]
    x0 = x - w/2
    x1 = x + w/2
    y0 = y - h/2
    y1 = y + h/2

    object_class_name = get_object_class(object_class)
    if confidence > threshold:
        ax.plot([x0,x0], [y0, y1], c = "y")
        ax.plot([x1,x1], [y0, y1], c = "y")
        ax.plot([x0,x1], [y0, y0], c = "y")
        ax.plot([x0,x1], [y1, y1], c = "y")
        ax.text(x0,y1+ 20, f"{object_class_name} {confidence.item()}")