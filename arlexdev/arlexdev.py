"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from arlexdev.pages.index import index

from .styles import styles


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    theme=rx.theme(
        panel_background="solid",
        accent_color="gray",
        gray_color="gray",
        radius="large"
    )
)

title = "Arlexdev | Full Stack Developer | Desarrollo de Software"
description = "Soy Alex Huarina (arlexdev), Desarrollador Full Stack. Creo soluciones web únicas con +2 años de experiencia en software."
preview = "./preview.png"

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"char_set": "UTF-8"},
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview}
    ]
)
