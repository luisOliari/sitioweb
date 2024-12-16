import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#config
st.set_page_config(page_title="Datos en Movimiento",page_icon="🤖",layout="wide")

def load_lottieurl(lottie_file):
    r = requests.get(lottie_file)
    if r.status_code !=200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="oliariluis@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"


# intro

with st.container():
    st.header("Hola, somos Datos en movimiento 🖐")
    st.title("Aprendemos Inteligencia Artificial para nuestra vida cotidiana")
    st.write("Somos unos apasionados de la tecnologia y la innovación, especializados en el sector de la digitalización y automatización de negocios")
    #st.write("[Saber más>](https://luisoliari.com.uy")

#sobre nosotros

with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 🔍")
        st.write(
               """
            Seguramente nosotros te vamos a poder ayudar sobre los siguientes objetivos:
        
            -Educar sobre IA: Brindar conocimientos prácticos sobre inteligencia artificial para su aplicación en la vida diaria y en el ámbito laboral.
            
            -Desmitificar la IA: Eliminar mitos y simplificar conceptos complejos de inteligencia artificial para hacerlos accesibles a todos.
            
            -Fomentar la Innovación: Inspirar a los usuarios a adoptar herramientas de IA para mejorar procesos personales y profesionales.
            
            -Desarrollar Habilidades: Enseñar técnicas y metodologías que permitan a las personas utilizar la inteligencia artificial con confianza y eficacia.
            
            -Crear Comunidad: Construir una comunidad activa de personas interesadas en aprender y compartir experiencias sobre inteligencia artificial.
            
            -Impulsar el Crecimiento Profesional: Ayudar a los usuarios a aplicar la inteligencia artificial para potenciar sus carreras y negocios.

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***
            """
        )
      #st.write("[Mas sobre nosotros>]https://luisoliari.com.uy/about/)")
    with animation_column:
        st_lottie(load_lottieurl(lottie_file), height=400)

#Servicios

with st.container():
    st.write("---")
    st.header("Servicios ⚒")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes\luis_logo.png")
        st.image(image, use_container_width=True)
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir infrormación en diferentes formatos de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesamientos diarios.
            """
        )
        #st.write("[ver servicios >](https://luisoliari.com.uy/servicios/)")
        
with st.container():
    st.write("---")
    #st.header("Servicios ⚒")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/luis_blanco.png")
        st.image(image, use_container_width=True)
    with text_column:
        st.subheader("Automatización de tareas")
        st.write(
            """
            Si realizas cualquier tipo de tarea repetitiva como por ejemplo redactar email, comenzar a realizar informes, generar ideas de logos, generar imagnes además puedes sacar ideas para realizar actividades.
            """
        )
        #st.write("[Ver servicios >](https://valerapp.com/services/)")
        

with st.container():
    st.write("---")
    #st.header("Servicios ⚒")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes\luis_celeste.png")
        st.image(image, use_container_width=True)
    with text_column:
        st.subheader("Visualización de datos")
        st.write(
            """
            Si sientes que no tienes una visión clara de los datos, la mejor forma de tomar decisiones en la vida cotidiana y en el trabajo es mediante la visualización de los datos. 
            """
        )
        #st.write("[ver servicios >](https://luisoliari.com.uy/servicios/)")        

# contacto 

with st.container():
    st.write("---")
    st.header("contacta con nosotros 📑")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Tu nombre" required>
     <input type="email" name="email" placeholder = "Tu email" required>
     <textarea name="message" name="menssage"  placeholder = "Tu menssage aqui" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
