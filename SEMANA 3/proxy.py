#Julio anthony engels ruiz coto - 1284719
#eddie alejandro giron carranza - 1307419

#Este programa define una estructura que permite a la clase YouTubeManager interactuar con la clase ThirdPartyYouTubeClass 
#a traves de un proxy, la clase CachedYouTubeClass. La ventaja es que YouTubeManager(cliente) no necesita saber nada acerca de esta 
#relacion, y CachedYouTubeClass puede manejar la logica de la cache para mejorar el rendimiento.

# Estamos importando los modulos necesarios para trabajar con clases abstractas en Python.
from abc import ABC, abstractmethod

# Definimos una interfaz ThirdPartyYouTubeLib utilizando la clase abstracta base (ABC). Esta interfaz declara los metodos que deben implementar 
# las clases concretas.
class ThirdPartyYouTubeLib(ABC):
    #@abstractmethod se utiliza para indicar que list_videos,
    #get_video_info y download_video deben implementarse en cualquier clase que implemente ThirdPartyYouTubeLib.
    @abstractmethod #para definir metodos abstractos en la clase base abstracta
    def list_videos(self):
        pass #pass se utiliza en los metodos de la interfaz ThirdPartyYouTubeLib porque estos metodos son abstractos. 
             #Los metodos abstractos son aquellos que tienen una declaracion pero no una implementacion en la clase base (en este caso, la interfaz).

    @abstractmethod
    def get_video_info(self, id): #self para referirse a los atributos y metodos del objeto actual.
        pass

    @abstractmethod
    def download_video(self, id):
        pass

# Creamos una clase concreta ThirdPartyYouTubeClass que implementa la interfaz ThirdPartyYouTubeLib.
# Esta es la clase real que realizara las operaciones necesarias.
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self):
        return "Returning list of videos"

    def get_video_info(self, id):
        return f"Returning info of video {id}"

    def download_video(self, id):
        return f"Downloading video {id}"

# La clase CachedYouTubeClass es el proxy. Tambien implementa la interfaz ThirdPartyYouTubeLib.
# Almacena una referencia al objeto de servicio (ThirdPartyYouTubeClass) y mantiene una cache de los resultados.
class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service):
        self.service = service
        self.list_cache = None
        self.video_cache = dict()
        self.video_download_cache = dict()

    def list_videos(self):
        if not self.list_cache:
            self.list_cache = self.service.list_videos()
        return self.list_cache

    def get_video_info(self, id):
        if id not in self.video_cache:
            self.video_cache[id] = self.service.get_video_info(id)
        return self.video_cache[id]

    def download_video(self, id):
        if id not in self.video_download_cache:
            self.video_download_cache[id] = self.service.download_video(id)
        return self.video_download_cache[id]
    
    def reset_cache(self):
        self.list_cache = None
        self.video_cache.clear()
        self.video_download_cache.clear()


# YouTubeManager es la clase cliente que interactua con la interfaz ThirdPartyYouTubeLib.
# Esta clase no sabe si esta interactuando con el objeto de servicio real (ThirdPartyYouTubeClass) o el proxy (CachedYouTubeClass).
class YouTubeManager:
    def __init__(self, service):
        self.service = service

    def render_video_page(self, id):
        info = self.service.get_video_info(id)
        print(info)

    def render_list_panel(self):
        list = self.service.list_videos()
        print(list)

    def react_on_user_input(self):
        self.render_video_page('123')
        self.render_list_panel()

# La clase Application muestra como se puede configurar y utilizar el proxy. 
class Application:
    def init(self):
        a_youtube_service = ThirdPartyYouTubeClass()
        a_youtube_proxy = CachedYouTubeClass(a_youtube_service)
        manager = YouTubeManager(a_youtube_proxy)
        manager.react_on_user_input()

        # resetea el  cache y reaccionar de nuevo
        print("\nResetting cache and getting data again:\n")
        a_youtube_proxy.reset_cache()
        manager.react_on_user_input()

# Aqui instanciamos la clase Application y llamamos al metodo init para poner en marcha el programa.
app = Application()
app.init()

