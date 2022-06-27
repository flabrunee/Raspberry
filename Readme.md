# Mar del Chat #

## Integrantes Grupo 1 ##
- Lucas Varela 
- Damian Bosatta 
- Nicolas Francolino 
- Fabian Labrunee 
## Introducción ##
Trabajo Final del Bootcamp Backend .NET / C#  - DEV PLACE Tech Academy.
	Este proyecto se trata de un servicio de chat en tiempo real implementado con tecnologia .Net contra SQL Server mediante APIs
	en el BackEnd consumidas por la interfaz de usuario ...en el FrontEnd. El mismo se centra en el diseño y desarrollo de un servidor 
	que proporciona soporte mediante ¿endpoints?(para no repetir APIs) a una aplicación llamada ??, la cual permite la interacción 
	entre distintos usuarios registrados que pueden interactuar con otros mediante salas de chat individuales o grupales.
	El usuario se debe registrar en el FrontEnd para comenzar a chatear con otro usuario mediante una sala individual o puede 
	acceder a una sala grupal donde hay mas usuarios. Las salas no son persistentes, son destruidas al finalizar la sesión todos
	los usuarios que la integran.
- Persistencia de datos en cuanto a login y registro de usuarios
- Soporte multi clientes
- Deteccion de escritura en tiempo real
- Deteccion del ingreso y salida de cualquier usuario al chat
- Multi plataforma
	
## Tecnologías y Herramientas ##
Se utilizó Visual Studio Community 2022 como herramienta de programacion
### Para el desarrollo de la parte Backend se utilizaron principalmente los siguientes lenguajes y tecnologías: ###
- C#  
- SQL Server  
- .NET Framework 6.0  

### Para el FrontEnd, se utilizó la herramienta de desarrollo SignalR ###  
SignalR es una librería o framework de desarrollo que permite conectar en nuestras aplicaciones, la capa de backend con el lado cliente, en ambas direcciones, y sobre todo en tiempo real sin necesidad de recargar pantalla.
Con SignalR podemos conectar a un servicio tanto clientes como digamos, pudiendo escalar el servicio bajo demanda.
Las conexiones al servicio se realizan con autenticación multifactor, gracias a la clave de acceso, que nos devuelve un token de sesión válido para que las aplicaciones clientes consuman el servicio.
Esta herramienta permite desarrollar una aplicacion sobre una conexion virtualmente siempre abierta, creando la sensación de estar trabajando en una conexion continua. Del lado del servidor se puede detectar cuando se ha conectado o desconectado un nuevo cliente, se puede recibir mensajes de los mismos y enviar mensajes a los clientes conectados, en definitiva, todo lo necesario para poder crear aplicaciones asincronas multiusuario.
![](https://www.compartimoss.com/static/cf87d91c43f165c7e0cd338d055e275c/2bef9/image3.png)
##### Fuente: https://www.compartimoss.com/revistas/numero-36/eventos-real-time-con-azure-signalr-en-asp-net-core/ #####

## Implementacion ## 
El proyecto está desarrollado usando la metodologia de Arquitectura de N-Capas la cual se presta a reutilización de código por parte de distintas capas de presentación.  
MVC?  
Algun patron?  

	
![](https://docs.microsoft.com/es-es/dotnet/architecture/cloud-native/media/direct-client-to-service-communication.png)
##### Fuente: https://docs.microsoft.com/es-es/dotnet/architecture/cloud-native/front-end-communication #####

## Estructura del sistema Backend ##
(sin archivos)
```
├───API_CoreBusiness  
│   ├───Authentication  
│   │   ├───Request  
│   │   └───Response  
│   ├───Entities  
├───API_DataCore  
│   ├───PluginInterfaces  
│   └───Repository  
├───API_GenericCore  
│   ├───GenericRepository  
│   │   └───Interfaces  
├───API_LoggerCore  
│   ├───CustomLogger  
│   ├───Middleware  
│   └───Properties  
├───API_UsesCases  
│   ├───Services  
│   └───UnitOfWork  
└───MarDelChat  
    ├───Controllers  
    ├───Migrations  
    └───Properties  
```
(con archivos)
```
│   
├───API_CoreBusiness
│   │   API_CoreBusiness.csproj
│   │   ApplicationDbContext.cs 
│   │   
│   ├───Authentication
│   │   ├───Request
│   │   │       UserRequest.cs
│   │   │       
│   │   └───Response
│   │           UserResponse.cs
│   └───Entities
│           Chat.cs
│           ChatType.cs
│           ChatUsuario.cs
│           Contactos.cs
│           Mensaje.cs
│           Role.cs
│           Usuario.cs 
│    
├───API_DataCore 
│   │           
│   ├───PluginInterfaces
│   │       IChatRepository.cs
│   │       IChatUsuarioRepository.cs
│   │       IContactoRepository.cs
│   │       IMensajeRepository.cs
│   │       IUsuarioRepository.cs
│   │       
│   └───Repository
│           ChatRepository.cs
│           ChatUsuarioRepository.cs
│           ContactoRepository.cs
│           MensajeRepository.cs
│           UsuarioRepository.cs
│           
├───API_GenericCore
│   │   API_GenericCore.csproj
│   │   
│   ├───bin
│   │   └───Debug
│   │       └───net6.0
│   └───GenericRepository
│       │   GenericRepository.cs
│       │   
│       └───Interfaces
│               IGenericRepository.cs
│                
├───API_LoggerCore
│   │   API_MiddlewareCore.csproj
│   │   
│   ├───CustomLogger
│   │       CustomLogger.cs
│   │       
│   ├───Middleware
│   │       CustomMiddleware.cs
│   └───Properties
│           launchSettings.json
│           
├───API_UsesCases
│   │           
│   ├───Services
│   │       IUserService.cs
│   │       UserService.cs
│   │       
│   └───UnitOfWork
│           IUnitOfWork.cs
│           UnitOfWork.cs
│           
└───MarDelChat
    │   .gitattributes
    │   appsettings.Development.json
    │   appsettings.json
    │   MarDelChat.csproj
    │   Program.cs
    │
    ├───Controllers
    │       ChatController.cs
    │       ContactoController.cs
    │       LoginController.cs 
    │       
    └───Properties
            launchSettings.json
```
## Requisitos / Pre-requisitos ##
-Net Framework 4.5 ??
-Algo mas?

## Forma de Uso o Configuracion Local o Despliegue ##
Por ejemplo...
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo.
Una vez clonado este repositorio se debe acceder mediante la terminal al mismo y ejecutar el comando composer update, esto instalara las dependecias de php que tiene el proyecto.
Seguidamente vamos se procede a compilar el webpack, para esto dentro de la terminal en el mismo proyecto ejecutamos el siguiente comando npm install
Debemos configurar las bases de datos y nuestro pushear ID dentro del archivo .env , y para finalizar corremos nuestro chat local utilizando el comando php artisan serve

## Glosario ##
- Back-end: La parte de una aplicación que almacena y manipula datos.
- Front-end: Es una interfaz a través de la cual los usuarios comunes pueden acceder a un programa. 
- Arquitectura de Capas: es la organización donde los componentes funcionales están separados jerárquicamente por capas. Cada capa solo está conectada con su superior y su inferior mediante interfaces.
- Framework: es una plataforma para el desarrollo de aplicaciones de software. Proporciona una base sobre la cual los desarrolladores de software pueden construir programas para una plataforma específica. 
- API: se refiere a la Interfaz de Programación de Aplicaciones. Es la plataforma que utiliza un programa para acceder a diferentes servicios en el sistema informático. 
