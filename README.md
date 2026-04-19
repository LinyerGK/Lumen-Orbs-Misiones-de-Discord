# Lumen Orbs 🎮 — Discord Quest Simulator (by Linyer)

Lumen Orbs es una herramienta de simulación de alto rendimiento diseñada para automatizar el progreso de las **Discord Quests**. Utiliza un motor de procesos fantasma (Ghost Engine) y Rich Presence para simular actividad real de juego sin consumir recursos significativos.

![Lumen Orbs UI](https://i.imgur.com/vH9x7vC.png) *(Placeholder para captura de pantalla)*

## ✨ Características principaless
- **Ghost Engine**: Crea ejecutables temporales con metadatos específicos para que Discord detecte el juego exacto requerido por la misión.
- **RPC Dinámico**: Simula estadísticas de juego (puntuación, kills, tiempo de sesión) para evitar detecciones de inactividad.
- **Base de Datos Integrada**: Incluye IDs oficiales de juegos populares como *Skate*, *Fortnite*, *Apex Legends*, entre otros.
- **Interfaz Moderna**: Construida con CustomTkinter para una estética oscura y premium.
- **Seguridad**: No requiere tu token de Discord. Funciona mediante detección local de procesos.

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/lumen-orbs.git
   cd lumen-orbs
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   python src/main.py
   ```

## 🛠️ Cómo completar misiones (Skate, etc.)

1. Asegúrate de haber **Aceptado** la misión en el menú de Discord.
2. Selecciona el juego en Lumen Orbs e inicia la simulación.
3. **Importante**: Algunas misiones requieren "Transmitir a un amigo". Únete a un canal de voz y comparte la ventana de `Skate` que abre Lumen.
4. El progreso comenzará a subir automáticamente cada pocos minutos.

## 📁 Estructura del Proyecto

- `src/gui`: Interfaz gráfica de usuario.
- `src/core`: Motores de procesos y lógica RPC.
- `assets/`: Recursos visuales e iconos.
- `games.json`: Base de datos de aplicaciones detectables.

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---
*Desarrollado con ❤️ por **Linyer** para la comunidad de Discord.*
