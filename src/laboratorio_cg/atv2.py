import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Imagem como matriz")

imagem = np.zeros((12, 18, 3), dtype=np.uint8)
imagem[:, 0:6] = (0, 255, 0)
imagem[:, 6:12] = (255, 255, 255)
imagem[:, 12:18] = (0, 255, 0)
st.image(ampliar(imagem))
st.image(imagem)