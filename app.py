import streamlit as st
import requests
import time


# Função para obter um novo meme
def get_a_meme():
    response = requests.get("https://meme-api.com/gimme")
    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_meme():
    # Obtenha e exiba o meme
    meme_response = get_a_meme()
    if meme_response and not meme_response["nsfw"]:
        st.image(meme_response["url"], caption=meme_response["title"])
    else:
        st.error("Falha ao carregar o meme, tente novamente")


def main():
    st.title("Um site sério de memes")

    # Exibe o meme
    display_meme()

    # Redefine a página após 10 segundos para buscar um novo meme
    if (
        "time_last_updated" not in st.session_state
        or time.time() - st.session_state["time_last_updated"] > 10
    ):
        st.session_state["time_last_updated"] = time.time()
        time.sleep(10)
        st.experimental_rerun()


if __name__ == "__main__":
    main()
