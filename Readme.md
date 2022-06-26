# Mar del Chat - Grupo 1 #
	Trabajo Final del Bootcamp Backend .NET / C#  - DEV PLACE Tech Academy.
	Este proyecto se trata de un servicio de chat en tiempo real implementado con tecnologia .Net contra SQL Server mediante APIs
	en el BackEnd consumidas por la interfaz de usuario ...en el FrontEnd. El mismo se centra en el diseño y desarrollo de un servidor 
	que proporciona soporte mediante ¿endpoints?(para no repetir APIs) a una aplicación llamada ??, la cual permite la interacción 
	entre distintos usuarios registrados que se pueden unir mediante salas de chat individuales o grupales.
	El usuario se debe registrar en el FrontEnd para comenzar a chatear con otro usuario mediante una sala individual o puede 
	acceder a una sala grupal donde hay mas usuarios. Las salas no son persistentes, son destruidas al finalizar la sesión todos
	los usuarios que la integran.
- Persistencia de datos en cuanto a login y registro de usuarios
- Soporte multi clientes (testeada con 100 usuarios conectados)
- Deteccion de escritura en tiempo real
- Deteccion del ingreso y salida de cualquier usuario al chat
- Multi plataforma
	
## Tecnologías y Herramientas ##
	Para el desarrollo de la parte Backend de este proyecto se han utilizado principalmente los lenguajes y tecnologías C#, SQL,
	.NET y herramientas SignalR?¿. Esta implementado usando la metodologia de Arquitectura de Capas
	Para el lado del FrontEnd, se ha utilizado la metodología de desarrollo ... 
![](https://docs.microsoft.com/es-es/dotnet/architecture/cloud-native/media/direct-client-to-service-communication.png)
Fuente: https://docs.microsoft.com/es-es/dotnet/architecture/cloud-native/front-end-communication

## Integrantes Grupo 1 ##
- Lucas Varela 
- Damian Bosatta 
- Nicolas Francolino 
- Fabian Labrunee 

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
## Forma de Uso o Configuracion Local ##
Por ejemplo...
Una vez clonado este repositorio se debe acceder mediante la terminal al mismo y ejecutar el comando composer update, esto instalara las dependecias de php que tiene el proyecto.

Seguidamente vamos se procede a compilar el webpack, para esto dentro de la terminal en el mismo proyecto ejecutamos el siguiente comando npm install

Debemos configurar las bases de datos y nuestro pushear ID dentro del archivo .env , y para finalizar corremos nuestro chat local utilizando el comando php artisan serve
## Glosario ##
- Back-end: La parte de una aplicación que almacena y manipula datos.
- Front-end: Es una interfaz a través de la cual los usuarios comunes pueden acceder a un programa. 
- Arquitectura de Capas: es la organización donde los componentes funcionales están separados jerárquicamente por capas. Cada capa solo está conectada con su superior y su inferior mediante interfaces.
- Framework: es una plataforma para el desarrollo de aplicaciones de software. Proporciona una base sobre la cual los desarrolladores de software pueden construir programas para una plataforma específica. 
- API: se refiere a la Interfaz de Programación de Aplicaciones. Es la plataforma que utiliza un programa para acceder a diferentes servicios en el sistema informático. 
