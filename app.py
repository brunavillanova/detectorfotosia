from flask import Flask, render_template, request
import os
import torch
from torchvision import transforms
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# carregar modelo
modelo = torch.hub.load(
    "pytorch/vision:v0.10.0",
    "resnet18",
    pretrained=True
)

modelo.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])


def detectar_ia(caminho):

    imagem = Image.open(caminho).convert("RGB")
    img = transform(imagem).unsqueeze(0)

    with torch.no_grad():
        output = modelo(img)

    prob = torch.softmax(output, dim=1)
    chance = prob.max().item()*100

    if chance > 50:
        return f"Imagem provavelmente IA ({chance:.2f}%)"
    else:
        return f"Imagem provavelmente real ({chance:.2f}%)"


@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        arquivo = request.files["imagem"]
        caminho = os.path.join(app.config["UPLOAD_FOLDER"], arquivo.filename)

        arquivo.save(caminho)

        resultado = detectar_ia(caminho)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)