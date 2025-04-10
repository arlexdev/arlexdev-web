import reflex as rx
from ..styles import styles

def hero() -> rx.Component:
    return rx.box(
        # Fondo decorativo
        rx.box(
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
            background="linear-gradient(to right, #2A2A2A 1px, transparent 1px), linear-gradient(to bottom, #2A2A2A 1px, transparent 1px)",
            background_size="40px 40px",
            z_index="0"
        ),
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background_color="black",
            mask_image="radial-gradient(ellipse at center, transparent 20%, black)",
            webkit_mask_image="radial-gradient(ellipse at center, transparent 20%, black)",
            z_index="0"
        ),
        rx.center(
            rx.section(
                rx.vstack(
                    # Badge de disponibilidad
                    rx.link(
                        rx.badge(
                            rx.hstack(
                                rx.box(
                                    background_color="var(--green-9)",
                                    border_radius="50%",
                                    width="10px",
                                    height="10px",
                                    aria_label="Indicador de disponibilidad"
                                ),
                                rx.text("Disponible para nuevos proyectos"),
                                spacing="2",
                                align="center"
                            ),
                            color_scheme="green",
                            variant="surface",
                            radius="full",
                            size=rx.breakpoints(
                            initial="2",
                            sm="3",
                            lg="3"
                            ),
                        ),
                        href="https://www.linkedin.com/in/arlexdev/",
                        is_external=True,
                        aria_label="Ver perfil de LinkedIn"
                    ),
                    rx.vstack(
                        # Encabezado principal
                        rx.heading(
                            "Desarrollador Full Stack",
                            size=rx.breakpoints(
                                initial="7",
                                sm="8",
                                lg="9"
                            ),
                            background_image="linear-gradient(to bottom, #FFFFFF, #ffffffaf)",
                            background_clip="text",
                            color="transparent",
                            align="center",
                            weight="bold",
                            as_="h1"
                        ),
                        # Descripción
                        rx.heading(
                            "Con más de 2 años de experiencia en la creación de aplicaciones web únicas, desde La Paz, Bolivia.",
                            width=rx.breakpoints(
                                initial="300px",
                                sm="400px",
                                md="500px",
                                lg="600px"
                            ),
                            size="5",
                            color_scheme="gray",
                            role="presentation",
                            as_="h2",
                            weight="regular",
                            align="center"
                        ),
                        # Botones de redes sociales

                        rx.hstack(
                            rx.button(
                                rx.text(
                                    "Contáctame",
                                    size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                    ),
                                ),
                                on_click=lambda: rx.redirect("https://mail.google.com/mail/u/0/?fs=1&tf=cm&to=arlexdev@gmail.com", is_external=True),
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
                            rx.button(
                                rx.text(
                                    "Ver Proyectos",
                                    size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                    ),
                                ),
                                size=rx.breakpoints(
                                    initial="3",
                                    sm="4",
                                    lg="4"
                                ),
                                on_click=lambda: rx.redirect("#proyectos"),
                                background_color="#000000",
                                border="1px solid #2A2A2A",
                                _hover={
                                    "background_color": "#090909",
                                    "color": "#FFFFFF"
                                }
                            ),

                            width="100%",
                            justify="center",
                            align="center",
                            role="group",
                            aria_label="Enlaces a redes sociales"
                        ),
                        align="center",
                        justify="center",
                        spacing="6"
                    ),
                    margin=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    spacing="5",
                    justify="center",
                    align="center"
                ),
                padding_top="5rem",
                style=styles.max_width_style,
                width="100%",
                size="2"
            ),
            width="100%",
            position="relative"
        ),
        position="relative",
        width="100%",
        height="100%"
    )
