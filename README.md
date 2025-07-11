# 🖼️ mymeme

**mymeme** is a lightweight Python package that lets you create stylish memes by overlaying bold, colorful text on your images (JPG or PNG). It automatically wraps long text, centers it at the top, and gives your image a meme-like flair --> all with a single function.

---

## 📦 Installation

Install from [PyPI](https://pypi.org/project/mymeme):

```bash
pip install mymeme
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/Farooquekk/mymeme.git
```

---

## 🚀 Usage

```python
from mymeme import create_meme

# Generate a meme from an image

image_path = "input.png"
top_text = "Anaconda?"
bottom_text = "No it's python!!"
create_meme(
    image_path,  
    top_text,
    bottom_text
)
# output will be output_meme.png
```

🔷𝑆𝑢𝑝𝑝𝑜𝑟𝑡𝑠 `.𝑗𝑝𝑔`, `.𝑝𝑛𝑔` <br/>
🔷𝐴𝑢𝑡𝑜𝑚𝑎𝑡𝑖𝑐𝑎𝑙𝑙𝑦 𝑤𝑟𝑎𝑝𝑠 𝑙𝑜𝑛𝑔 𝑙𝑖𝑛𝑒𝑠 <br/>
🔷𝑇𝑒𝑥𝑡 𝑖𝑠 𝑏𝑜𝑙𝑑, 𝑐𝑒𝑛𝑡𝑒𝑟𝑒𝑑, 𝑎𝑛𝑑 𝑠𝑡𝑦𝑙𝑒𝑑 <br/>
🔷𝑂𝑛𝑙𝑦 𝑡𝑜𝑝 𝑡𝑒𝑥𝑡 𝑖𝑠 𝑠ℎ𝑜𝑤𝑛 (𝑐𝑙𝑎𝑠𝑠𝑖𝑐 𝑚𝑒𝑚𝑒 𝑠𝑡𝑦𝑙𝑒) 

---

## ✨ Features

- 🧠 **Auto-wraps long lines**
- 🎯 **Text is centered at the top**
- 🎨 **Bold font and modern color**
- 🖼️ **JPG and PNG support**
- ⚡ **Minimal API (1-line usage)**
- 🐍 **No dependencies except Pillow**

---

## 🧪 Project Structure

```mymeme/
├── mymeme/
│   └── __init__.py
│   └── meme.py
├── tests/
│   └── 
├── README.md
├── LICENSE
├── setup.py
├── pyproject.toml
```

---

## 👨‍💻 Development

Clone the repo:

```bash
git clone https://github.com/Farooquekk/mymeme.git
cd mymeme
```

Install in development mode:

```bash
pip install -e .
```




---

## 🔗 Links

- 📦 PyPI: [https://pypi.org/project/mymeme](https://pypi.org/project/mymeme)
- 💻 GitHub: [https://github.com/Farooquekk/mymeme](https://github.com/Farooquekk/mymeme)
- 📄 License: [MIT](https://choosealicense.com/licenses/mit/)

---

## 📄 License

MIT License
© 2025 Farooque Sajjad
