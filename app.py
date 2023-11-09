import requests

import streamlit as st

URL_MEME = "https://meme-api.com/gimme"


@st.cache_data(ttl=10)
def get_a_meme():
    return requests.get(URL_MEME).json()


def main():
    st.title("Um site sério de memes")

    imagem_meme = st.empty()

    while True:
        meme_response = get_a_meme()
        if meme_response and not meme_response["nsfw"]:
            imagem_meme.image(meme_response["url"], caption=meme_response["title"])
        else:
            st.error("Falha ao carregar o meme, tente novamente")


if __name__ == "__main__":
    main()
