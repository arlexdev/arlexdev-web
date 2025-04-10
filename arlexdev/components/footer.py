import reflex as rx
import datetime

from ..components.stroke import stroke
from ..styles import styles

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"),
        href=href,
        underline="none",
        color="#gray",
        _hover= {
            "color": "#FFFFFF"
        }
    )


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Últimos Proyectos", size="4", weight="bold", as_="h3"
        ),
        footer_item("Sistema de Gestión Integral de Membresías", "/#"),
        #footer_item("Web Development", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Arlexdev", size="4", weight="bold", as_="h3"
        ),
        footer_item("Experiencia", "/#experiencia"),
        footer_item("Proyectos", "/#proyectos"),
        footer_item("Sobre mí", "/#sobre-mi"),
        footer_item("Formación", "/#formación"),
        footer_item("Contacto", "/#contacto"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(image: str, href: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="24px",
            height="24px",
            _hover={"opacity": "0.8"},
            alt="Redes sociales"
        ),
        href=href,
        is_external=True,
    )



def socials() -> rx.Component:
    return rx.flex(
        social_link("/social/linkedin.svg", "https://www.linkedin.com/in/arlexdev/"),
        social_link("/social/github.svg", "https://github.com/arlexdev/"),
        social_link("/social/x.svg", "https://x.com/arlexdev/"),
        social_link("/social/instagram.svg", "https://www.instagram.com/arlex.dev/"),
        spacing="3",
        justify=rx.breakpoints(
            initial="center",
            sm="start",
            lg="start"
        ),
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.divider(bg="#222222"),
        rx.center(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            rx.image(
                                src="/logo.svg",
                                width="50px",
                                height="50px",
                                alt="Logo Arlexdev"
                            ),
                            align_items="center",
                        ),
                        rx.vstack(
                            rx.text("Encuéntrame en:",size="2",color_scheme="gray"),
                            socials(),
                            align_items=[
                                "center",
                                "center",
                                "start",
                            ],
                            width="100%",
                        ),
                        rx.hstack(
                            rx.text(
                                f" © 2024 - {datetime.date.today().year} Desarrollado con",
                                size="3",
                                white_space="nowrap",
                                color_scheme="gray"
                            ),
                            rx.icon("heart",size=20),
                            rx.text("v3.0",color_scheme="gray"),
                            align="center",
                            justify="center",
                            spacing="1",
                            width="100%",
                        ),
                        spacing="7",
                        align_items=[
                            "center",
                            "center",
                            "start",
                        ],
                    ),
                    footer_items_1(),
                    footer_items_2(),
                    justify="between",
                    spacing="6",
                    flex_direction=["column", "column", "row"],
                    width="100%",
                ),
                stroke(),
                spacing="8",
                padding=rx.breakpoints(
                    initial="1.5em",
                    sm="2.5em",
                    lg="4.5em",
                ),
                style=styles.max_width_style,
            ),
            bg="#090909",
            #bg="#111111",
            width="100%",
        ),
        width="100%",
    )
