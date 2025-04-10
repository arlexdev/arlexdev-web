import reflex as rx
from ..styles import styles

def works() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    #rx.icon(
                    #    "folder-open-dot",
                    #    size=30
                    #),
                    rx.heading(
                        "Proyectos",
                        size=rx.breakpoints(
                            initial="6",
                            sm="7",
                            lg="8"
                        ),
                        weight="bold",
                        as_="h2"
                    ),
                    width="100%",
                    justify="center"
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Iglesia Nacional Evangélica Los Amigos",
                                color_scheme="gray",
                                size="4"
                            ),
                            rx.image(
                                src="/icons/logo_iglesia.svg",
                                width="40px",
                                height="auto",
                                border_radius="50%",
                                alt="Logo Iglesia Nacional Evangélica Los Amigos"
                            ),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.flex(
                            rx.vstack(
                                rx.image(
                                    src="/project_1.webp",
                                    width="900px",
                                    height="auto",
                                    alt="Foto sistema de Gestión Integral de Membresías ",
                                    border_radius="10px"
                                ),
                            ),
                            rx.vstack(
                                rx.heading(
                                    "Sistema de Gestión Integral de Membresías"
                                ),
                                rx.flex(
                                    rx.badge(
                                        rx.text("Reflex"),
                                        variant="soft",
                                        color_scheme="violet",
                                        size="2"
                                    ),
                                    rx.badge(
                                        rx.text("Python"),
                                        variant="soft",
                                        color_scheme="yellow",
                                        size="2"
                                    ),
                                    rx.badge(
                                        rx.text("SQLite"),
                                        variant="soft",
                                        color_scheme="blue",
                                        size="2"
                                    ),
                                    rx.badge(
                                        rx.text("SQLModel"),
                                        variant="soft",
                                        color_scheme="purple",
                                        size="2"
                                    ),
                                    rx.badge(
                                        rx.text("Folium"),
                                        color_scheme="green",
                                        variant="soft",
                                        size="2"
                                    ),
                                    wrap="wrap",
                                    spacing="4",
                                    width="100%"
                                ),
                                rx.text(
                                    "Aplicación web moderna y eficiente desarrollada en Python para la administración integral de miembros de la organización.",
                                    color_scheme="gray"
                                ),
                                rx.button(
                                    rx.text(
                                        "Ver más",
                                        size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                        ),
                                    ),
                                    on_click=lambda: rx.redirect("/project_ED", is_external=False),
                                    size=rx.breakpoints(
                                        initial="3",
                                        sm="4",
                                        lg="4"
                                    ),
                                    background_color="#FFFFFF",
                                    border="1px solid #2A2A2A",
                                    color="#000000",
                                    _hover={"opacity": "0.8"},
                                ),
                                width="100%",
                            ),
                            flex_direction=["column", "row"],
                            align_items="center",
                            spacing="8"
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
                    #bg="#111111"
                ),
                margin=rx.breakpoints(
                    initial="1.5em",
                    sm="2.5em",
                    lg="3.5em"
                ),
                spacing="8",
            ),
            style=styles.max_width_style,
            id="proyectos",
            size="2",
        ),
        width="100%"
    )
