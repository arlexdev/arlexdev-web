import reflex as rx
from ..styles import styles

def about() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Sobre mí",
                        size=rx.breakpoints(
                            initial="6",
                            sm="7",
                            lg="8"
                        ),
                        weight="bold",
                        as_="h2"
                    ),
                    justify="center",
                    width="100%",
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.flex(
                                rx.vstack(
                                    rx.image(
                                        src="/foto_de_perfil.svg",
                                        width="500px",
                                        height="auto",
                                        alt="Foto de perfil Arlexdev",
                                        mask_image="linear-gradient(to bottom, #111111 80%, transparent)"
                                    )
                                ),
                                rx.vstack(
                                    rx.text("Mi nombre es Alex Hernan Huarina Chura"),
                                    rx.text("Soy egresado de Ingeniería de Sistemas de la Universidad Tecnológica Boliviana, apasionado por la tecnología y el desarrollo web. Me especializo en frontend, backend y ciberseguridad, siempre actualizado con las últimas tendencias tecnológicas.",color_scheme="gray"),
                                    rx.text("Actualmente, busco enfocar mis conocimientos y energía en convertirme en Software Engineer para crear soluciones innovadoras y eficientes.",color_scheme="gray"),
                                    width="100%"
                                ),
                                flex_direction=["column", "row"],
                                align_items="center",
                                spacing="8",
                            ),
                            align="center",
                            width="100%",
                        ),
                        spacing="6",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    border="1px solid #2A2A2A",
                    border_radius="12px",
                    width="100%",
                    bg="#090909"
                ),
                margin=rx.breakpoints(
                    initial="1.5em",
                    sm="2.5em",
                    lg="3.5em"
                ),
                spacing="8"
            ),
            style=styles.max_width_style,
            width="100%",
            size="2",
            id="sobre-mi",
        ),
        width="100%"
    )
